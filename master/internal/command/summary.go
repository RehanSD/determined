package command

import (
	"time"

	"github.com/determined-ai/determined/master/internal/task"
	"github.com/determined-ai/determined/master/pkg/actor"
	"github.com/determined-ai/determined/master/pkg/ptrs"

	"github.com/determined-ai/determined/master/pkg/container"
	"github.com/determined-ai/determined/master/pkg/model"
)

type (
	// getSummary is an actor message for getting the summary of the command.
	getSummary struct {
		userFilter string
	}
)

type (
	// commandOwner describes the owner of a command.
	commandOwner struct {
		ID       model.UserID `json:"id"`
		Username string       `json:"username"`
	}

	// summary holds an immutable snapshot of the command.
	summary struct {
		RegisteredTime time.Time              `json:"registered_time"`
		Owner          commandOwner           `json:"owner"`
		ID             model.TaskID           `json:"id"`
		AllocationID   model.AllocationID     `json:"allocation_id"`
		Config         model.CommandConfig    `json:"config"`
		State          string                 `json:"state"`
		ServiceAddress *string                `json:"service_address"`
		Addresses      []container.Address    `json:"addresses"`
		ExitStatus     *string                `json:"exit_status"`
		Misc           map[string]interface{} `json:"misc"`
		IsReady        bool                   `json:"is_ready"`
		AgentUserGroup *model.AgentUserGroup  `json:"agent_user_group"`
		ResourcePool   string                 `json:"resource_pool"`
	}
)

// summary returns a new summary of the command.
func (c *command) summary(ctx *actor.Context) summary {
	var exitStatus *string
	if c.exitStatus != nil {
		exitStatus = ptrs.StringPtr(c.exitStatus.Err.Error())
	}

	resp, _ := ctx.Ask(c.allocation, task.AllocationState{}).GetOrElseTimeout(
		task.AllocationState{},
		5*time.Second,
	)
	state := resp.(task.AllocationState)

	var addresses []container.Address
	for _, cAddrs := range state.Addresses {
		addresses = append(addresses, cAddrs...)
		break
	}

	return summary{
		RegisteredTime: c.registeredTime,
		Owner: commandOwner{
			ID:       c.Base.Owner.ID,
			Username: c.Base.Owner.Username,
		},
		ID:             c.taskID,
		Config:         c.Config,
		State:          state.State.String(),
		ServiceAddress: c.serviceAddress,
		Addresses:      addresses,
		ExitStatus:     exitStatus,
		Misc:           c.Metadata,
		IsReady:        state.Ready,
		AgentUserGroup: c.Base.AgentUserGroup,
		ResourcePool:   c.Config.Resources.ResourcePool,
	}
}
