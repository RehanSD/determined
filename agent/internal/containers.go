package internal

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	dcontainer "github.com/docker/docker/api/types/container"
	"github.com/docker/docker/client"
	"github.com/labstack/echo/v4"
	"github.com/pkg/errors"

	"github.com/determined-ai/determined/master/pkg/actor"
	proto "github.com/determined-ai/determined/master/pkg/agent"
	cproto "github.com/determined-ai/determined/master/pkg/container"
	"github.com/determined-ai/determined/master/pkg/device"
	"github.com/determined-ai/determined/master/pkg/model"
)

const (
	dockerContainerTypeLabel    = "ai.determined.container.type"
	dockerContainerTypeValue    = "task-container"
	dockerContainerIDLabel      = "ai.determined.container.id"
	dockerContainerParentLabel  = "ai.determined.container.parent"
	dockerContainerDevicesLabel = "ai.determined.container.devices"
	dockerAgentLabel            = "ai.determined.container.agent"
	dockerClusterLabel          = "ai.determined.container.cluster"
	dockerMasterLabel           = "ai.determined.container.master"
)

type containerManager struct {
	Options       Options           `json:"-"`
	MasterInfo    proto.MasterInfo  `json:"-"`
	GlobalEnvVars []string          `json:"global_env_vars"`
	Labels        map[string]string `json:"labels"`
	Devices       []device.Device   `json:"devices"`

	fluentPort int
	docker     *client.Client
}

func newContainerManager(a *agent, fluentPort int) (*containerManager, error) {
	return &containerManager{
		MasterInfo: a.MasterSetAgentOptions.MasterInfo,
		Options:    a.Options,
		Devices:    a.Devices,
		fluentPort: fluentPort,
	}, nil
}

func (c *containerManager) Receive(ctx *actor.Context) error {
	switch msg := ctx.Message().(type) {
	case actor.PreStart:
		d, err := client.NewClientWithOpts(client.FromEnv)
		if err != nil {
			return err
		}
		c.docker = d

		masterScheme := httpInsecureScheme
		if c.Options.Security.TLS.Enabled {
			masterScheme = httpSecureScheme
		}

		masterHost := c.Options.ContainerMasterHost
		if masterHost == "" {
			masterHost = c.Options.MasterHost
		}

		masterPort := c.Options.ContainerMasterPort
		if masterPort == 0 {
			masterPort = c.Options.MasterPort
		}

		c.GlobalEnvVars = []string{
			fmt.Sprintf("DET_CLUSTER_ID=%s", c.MasterInfo.ClusterID),
			fmt.Sprintf("DET_MASTER_ID=%s", c.MasterInfo.MasterID),
			fmt.Sprintf("DET_MASTER=%s://%s:%d", masterScheme, masterHost, masterPort),
			fmt.Sprintf("DET_MASTER_HOST=%s", masterHost),
			fmt.Sprintf("DET_MASTER_ADDR=%s", masterHost),
			fmt.Sprintf("DET_MASTER_PORT=%d", masterPort),
			fmt.Sprintf("DET_AGENT_ID=%s", c.Options.AgentID),
		}

		if a := c.Options.Security.TLS.MasterCertName; a != "" {
			c.GlobalEnvVars = append(c.GlobalEnvVars, fmt.Sprintf("DET_MASTER_CERT_NAME=%s", a))
		}

		c.Labels = map[string]string{
			dockerContainerTypeLabel: dockerContainerTypeValue,
			dockerAgentLabel:         c.Options.AgentID,
			dockerClusterLabel:       c.MasterInfo.ClusterID,
			dockerMasterLabel:        c.MasterInfo.MasterID,
		}

	case proto.ContainerLog, proto.ContainerStateChanged, model.TrialLog:
		ctx.Tell(ctx.Self().Parent(), msg)

	case proto.StartContainer:
		msg.Spec = c.overwriteSpec(msg.Container, msg.Spec)
		if ref, ok := ctx.ActorOf(msg.Container.ID, newContainerActor(msg, c.docker)); !ok {
			ctx.Log().Warnf("container already created: %s", msg.Container.ID)
			if ctx.ExpectingResponse() {
				ctx.Respond(errors.Errorf("container already created: %s", msg.Container.ID))
			}
		} else if ctx.ExpectingResponse() {
			ctx.Respond(ctx.Ask(ref, getContainerSummary{}))
		}

	case proto.SignalContainer:
		if ref := ctx.Child(msg.ContainerID); ref != nil {
			ctx.Tell(ref, msg)
		} else {
			ctx.Log().Warnf("error signaling container with %s, container not found: %s",
				msg.Signal, msg.ContainerID)
		}

	case echo.Context:
		c.handleAPIRequest(ctx, msg)

	case actor.PostStop:
		ctx.Log().Info("container manager shut down")

	default:
		return actor.ErrUnexpectedMessage(ctx)
	}
	return nil
}

func (c *containerManager) handleAPIRequest(ctx *actor.Context, apiCtx echo.Context) {
	switch apiCtx.Request().Method {
	case echo.GET:
		ctx.Respond(apiCtx.JSON(http.StatusOK,
			ctx.AskAll(getContainerSummary{}, ctx.Children()...)))
	default:
		ctx.Respond(echo.ErrMethodNotAllowed)
	}
}

func (c *containerManager) overwriteSpec(cont cproto.Container, spec cproto.Spec) cproto.Spec {
	return overwriteSpec(cont, spec, c.GlobalEnvVars, c.Labels, c.fluentPort)
}

func overwriteSpec(
	cont cproto.Container,
	spec cproto.Spec,
	globalEnvVars []string,
	labels map[string]string,
	fluentPort int,
) cproto.Spec {
	spec.RunSpec.HostConfig.AutoRemove = true
	spec.RunSpec.ContainerConfig.Env = append(
		spec.RunSpec.ContainerConfig.Env, globalEnvVars...)
	spec.RunSpec.ContainerConfig.Env = append(
		spec.RunSpec.ContainerConfig.Env, containerEnvVars(cont)...)
	if spec.RunSpec.ContainerConfig.Labels == nil {
		spec.RunSpec.ContainerConfig.Labels = make(map[string]string)
	}
	for key, value := range labels {
		spec.RunSpec.ContainerConfig.Labels[key] = value
	}
	spec.RunSpec.ContainerConfig.Labels[dockerContainerIDLabel] = cont.ID.String()
	spec.RunSpec.ContainerConfig.Labels[dockerContainerParentLabel] = cont.Parent.String()
	var slotIds []string
	for _, d := range cont.Devices {
		slotIds = append(slotIds, strconv.Itoa(d.ID))
	}
	spec.RunSpec.ContainerConfig.Labels[dockerContainerDevicesLabel] = strings.Join(slotIds, ",")

	spec.RunSpec.HostConfig.DeviceRequests = append(
		spec.RunSpec.HostConfig.DeviceRequests, gpuDeviceRequests(cont)...)

	if spec.RunSpec.UseFluentLogging {
		spec.RunSpec.HostConfig.LogConfig = dcontainer.LogConfig{
			Type: "fluentd",
			Config: map[string]string{
				"fluentd-address":              "localhost:" + strconv.Itoa(fluentPort),
				"fluentd-sub-second-precision": "true",
				"mode":                         "non-blocking",
				"max-buffer-size":              "10m",
				"env":                          strings.Join(fluentEnvVarNames, ","),
				"labels":                       dockerContainerParentLabel,
			},
		}
	}

	return spec
}

func gpuDeviceRequests(cont cproto.Container) []dcontainer.DeviceRequest {
	gpuUUIDs := cont.GPUDeviceUUIDs()
	if len(gpuUUIDs) == 0 {
		return nil
	}
	return []dcontainer.DeviceRequest{
		{
			Driver:       "nvidia",
			Capabilities: [][]string{{"gpu", "compute", "utility"}},
			DeviceIDs:    gpuUUIDs,
		},
	}
}

func containerEnvVars(cont cproto.Container) []string {
	var slotIds []string
	for _, d := range cont.Devices {
		slotIds = append(slotIds, strconv.Itoa(d.ID))
	}
	return []string{
		fmt.Sprintf("DET_CONTAINER_ID=%s", cont.ID),
		fmt.Sprintf("DET_SLOT_IDS=[%s]", strings.Join(slotIds, ",")),
	}
}
