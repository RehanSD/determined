# coding: utf-8

"""
    Determined API (Beta)

    Determined helps deep learning teams train models more quickly, easily share GPU resources, and effectively collaborate. Determined allows deep learning engineers to focus on building and training models at scale, without needing to worry about DevOps or writing custom code for common tasks like fault tolerance or experiment tracking.  You can think of Determined as a platform that bridges the gap between tools like TensorFlow and PyTorch --- which work great for a single researcher with a single GPU --- to the challenges that arise when doing deep learning at scale, as teams, clusters, and data sets all increase in size.  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: community@determined.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1ResourcePool(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'type': 'V1ResourcePoolType',
        'num_agents': 'int',
        'slots_available': 'int',
        'slots_used': 'int',
        'cpu_container_capacity': 'int',
        'cpu_containers_running': 'int',
        'default_gpu_pool': 'bool',
        'default_cpu_pool': 'bool',
        'preemptible': 'bool',
        'min_agents': 'int',
        'max_agents': 'int',
        'slots_per_agent': 'int',
        'cpu_container_capacity_per_agent': 'int',
        'scheduler_type': 'V1SchedulerType',
        'scheduler_fitting_policy': 'V1FittingPolicy',
        'location': 'str',
        'image_id': 'str',
        'instance_type': 'str',
        'master_url': 'str',
        'master_cert_name': 'str',
        'startup_script': 'str',
        'container_startup_script': 'str',
        'agent_docker_network': 'str',
        'agent_docker_runtime': 'str',
        'agent_docker_image': 'str',
        'agent_fluent_image': 'str',
        'max_idle_agent_period': 'float',
        'max_agent_starting_period': 'float',
        'details': 'V1ResourcePoolDetail'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'num_agents': 'numAgents',
        'slots_available': 'slotsAvailable',
        'slots_used': 'slotsUsed',
        'cpu_container_capacity': 'cpuContainerCapacity',
        'cpu_containers_running': 'cpuContainersRunning',
        'default_gpu_pool': 'defaultGpuPool',
        'default_cpu_pool': 'defaultCpuPool',
        'preemptible': 'preemptible',
        'min_agents': 'minAgents',
        'max_agents': 'maxAgents',
        'slots_per_agent': 'slotsPerAgent',
        'cpu_container_capacity_per_agent': 'cpuContainerCapacityPerAgent',
        'scheduler_type': 'schedulerType',
        'scheduler_fitting_policy': 'schedulerFittingPolicy',
        'location': 'location',
        'image_id': 'imageId',
        'instance_type': 'instanceType',
        'master_url': 'masterUrl',
        'master_cert_name': 'masterCertName',
        'startup_script': 'startupScript',
        'container_startup_script': 'containerStartupScript',
        'agent_docker_network': 'agentDockerNetwork',
        'agent_docker_runtime': 'agentDockerRuntime',
        'agent_docker_image': 'agentDockerImage',
        'agent_fluent_image': 'agentFluentImage',
        'max_idle_agent_period': 'maxIdleAgentPeriod',
        'max_agent_starting_period': 'maxAgentStartingPeriod',
        'details': 'details'
    }

    def __init__(self, name=None, description=None, type=None, num_agents=None, slots_available=None, slots_used=None, cpu_container_capacity=None, cpu_containers_running=None, default_gpu_pool=None, default_cpu_pool=None, preemptible=None, min_agents=None, max_agents=None, slots_per_agent=None, cpu_container_capacity_per_agent=None, scheduler_type=None, scheduler_fitting_policy=None, location=None, image_id=None, instance_type=None, master_url=None, master_cert_name=None, startup_script=None, container_startup_script=None, agent_docker_network=None, agent_docker_runtime=None, agent_docker_image=None, agent_fluent_image=None, max_idle_agent_period=None, max_agent_starting_period=None, details=None):  # noqa: E501
        """V1ResourcePool - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._type = None
        self._num_agents = None
        self._slots_available = None
        self._slots_used = None
        self._cpu_container_capacity = None
        self._cpu_containers_running = None
        self._default_gpu_pool = None
        self._default_cpu_pool = None
        self._preemptible = None
        self._min_agents = None
        self._max_agents = None
        self._slots_per_agent = None
        self._cpu_container_capacity_per_agent = None
        self._scheduler_type = None
        self._scheduler_fitting_policy = None
        self._location = None
        self._image_id = None
        self._instance_type = None
        self._master_url = None
        self._master_cert_name = None
        self._startup_script = None
        self._container_startup_script = None
        self._agent_docker_network = None
        self._agent_docker_runtime = None
        self._agent_docker_image = None
        self._agent_fluent_image = None
        self._max_idle_agent_period = None
        self._max_agent_starting_period = None
        self._details = None
        self.discriminator = None

        self.name = name
        self.description = description
        self.type = type
        self.num_agents = num_agents
        self.slots_available = slots_available
        self.slots_used = slots_used
        self.cpu_container_capacity = cpu_container_capacity
        self.cpu_containers_running = cpu_containers_running
        self.default_gpu_pool = default_gpu_pool
        self.default_cpu_pool = default_cpu_pool
        self.preemptible = preemptible
        self.min_agents = min_agents
        self.max_agents = max_agents
        if slots_per_agent is not None:
            self.slots_per_agent = slots_per_agent
        self.cpu_container_capacity_per_agent = cpu_container_capacity_per_agent
        self.scheduler_type = scheduler_type
        self.scheduler_fitting_policy = scheduler_fitting_policy
        self.location = location
        self.image_id = image_id
        self.instance_type = instance_type
        self.master_url = master_url
        self.master_cert_name = master_cert_name
        self.startup_script = startup_script
        self.container_startup_script = container_startup_script
        self.agent_docker_network = agent_docker_network
        self.agent_docker_runtime = agent_docker_runtime
        self.agent_docker_image = agent_docker_image
        self.agent_fluent_image = agent_fluent_image
        self.max_idle_agent_period = max_idle_agent_period
        self.max_agent_starting_period = max_agent_starting_period
        self.details = details

    @property
    def name(self):
        """Gets the name of this V1ResourcePool.  # noqa: E501

        The unique name of the resource pool.  # noqa: E501

        :return: The name of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1ResourcePool.

        The unique name of the resource pool.  # noqa: E501

        :param name: The name of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this V1ResourcePool.  # noqa: E501


        :return: The description of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1ResourcePool.


        :param description: The description of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def type(self):
        """Gets the type of this V1ResourcePool.  # noqa: E501


        :return: The type of this V1ResourcePool.  # noqa: E501
        :rtype: V1ResourcePoolType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1ResourcePool.


        :param type: The type of this V1ResourcePool.  # noqa: E501
        :type: V1ResourcePoolType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def num_agents(self):
        """Gets the num_agents of this V1ResourcePool.  # noqa: E501


        :return: The num_agents of this V1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._num_agents

    @num_agents.setter
    def num_agents(self, num_agents):
        """Sets the num_agents of this V1ResourcePool.


        :param num_agents: The num_agents of this V1ResourcePool.  # noqa: E501
        :type: int
        """
        if num_agents is None:
            raise ValueError("Invalid value for `num_agents`, must not be `None`")  # noqa: E501

        self._num_agents = num_agents

    @property
    def slots_available(self):
        """Gets the slots_available of this V1ResourcePool.  # noqa: E501


        :return: The slots_available of this V1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._slots_available

    @slots_available.setter
    def slots_available(self, slots_available):
        """Sets the slots_available of this V1ResourcePool.


        :param slots_available: The slots_available of this V1ResourcePool.  # noqa: E501
        :type: int
        """
        if slots_available is None:
            raise ValueError("Invalid value for `slots_available`, must not be `None`")  # noqa: E501

        self._slots_available = slots_available

    @property
    def slots_used(self):
        """Gets the slots_used of this V1ResourcePool.  # noqa: E501


        :return: The slots_used of this V1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._slots_used

    @slots_used.setter
    def slots_used(self, slots_used):
        """Sets the slots_used of this V1ResourcePool.


        :param slots_used: The slots_used of this V1ResourcePool.  # noqa: E501
        :type: int
        """
        if slots_used is None:
            raise ValueError("Invalid value for `slots_used`, must not be `None`")  # noqa: E501

        self._slots_used = slots_used

    @property
    def cpu_container_capacity(self):
        """Gets the cpu_container_capacity of this V1ResourcePool.  # noqa: E501


        :return: The cpu_container_capacity of this V1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._cpu_container_capacity

    @cpu_container_capacity.setter
    def cpu_container_capacity(self, cpu_container_capacity):
        """Sets the cpu_container_capacity of this V1ResourcePool.


        :param cpu_container_capacity: The cpu_container_capacity of this V1ResourcePool.  # noqa: E501
        :type: int
        """
        if cpu_container_capacity is None:
            raise ValueError("Invalid value for `cpu_container_capacity`, must not be `None`")  # noqa: E501

        self._cpu_container_capacity = cpu_container_capacity

    @property
    def cpu_containers_running(self):
        """Gets the cpu_containers_running of this V1ResourcePool.  # noqa: E501


        :return: The cpu_containers_running of this V1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._cpu_containers_running

    @cpu_containers_running.setter
    def cpu_containers_running(self, cpu_containers_running):
        """Sets the cpu_containers_running of this V1ResourcePool.


        :param cpu_containers_running: The cpu_containers_running of this V1ResourcePool.  # noqa: E501
        :type: int
        """
        if cpu_containers_running is None:
            raise ValueError("Invalid value for `cpu_containers_running`, must not be `None`")  # noqa: E501

        self._cpu_containers_running = cpu_containers_running

    @property
    def default_gpu_pool(self):
        """Gets the default_gpu_pool of this V1ResourcePool.  # noqa: E501


        :return: The default_gpu_pool of this V1ResourcePool.  # noqa: E501
        :rtype: bool
        """
        return self._default_gpu_pool

    @default_gpu_pool.setter
    def default_gpu_pool(self, default_gpu_pool):
        """Sets the default_gpu_pool of this V1ResourcePool.


        :param default_gpu_pool: The default_gpu_pool of this V1ResourcePool.  # noqa: E501
        :type: bool
        """
        if default_gpu_pool is None:
            raise ValueError("Invalid value for `default_gpu_pool`, must not be `None`")  # noqa: E501

        self._default_gpu_pool = default_gpu_pool

    @property
    def default_cpu_pool(self):
        """Gets the default_cpu_pool of this V1ResourcePool.  # noqa: E501


        :return: The default_cpu_pool of this V1ResourcePool.  # noqa: E501
        :rtype: bool
        """
        return self._default_cpu_pool

    @default_cpu_pool.setter
    def default_cpu_pool(self, default_cpu_pool):
        """Sets the default_cpu_pool of this V1ResourcePool.


        :param default_cpu_pool: The default_cpu_pool of this V1ResourcePool.  # noqa: E501
        :type: bool
        """
        if default_cpu_pool is None:
            raise ValueError("Invalid value for `default_cpu_pool`, must not be `None`")  # noqa: E501

        self._default_cpu_pool = default_cpu_pool

    @property
    def preemptible(self):
        """Gets the preemptible of this V1ResourcePool.  # noqa: E501

        Is this resource pool using preemptible/spot instances? Only meaningful in an AWS or GCP resource pool.  # noqa: E501

        :return: The preemptible of this V1ResourcePool.  # noqa: E501
        :rtype: bool
        """
        return self._preemptible

    @preemptible.setter
    def preemptible(self, preemptible):
        """Sets the preemptible of this V1ResourcePool.

        Is this resource pool using preemptible/spot instances? Only meaningful in an AWS or GCP resource pool.  # noqa: E501

        :param preemptible: The preemptible of this V1ResourcePool.  # noqa: E501
        :type: bool
        """
        if preemptible is None:
            raise ValueError("Invalid value for `preemptible`, must not be `None`")  # noqa: E501

        self._preemptible = preemptible

    @property
    def min_agents(self):
        """Gets the min_agents of this V1ResourcePool.  # noqa: E501

        When using dynamic agents, the minimum number of agents that can exist in the resource pool.  # noqa: E501

        :return: The min_agents of this V1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._min_agents

    @min_agents.setter
    def min_agents(self, min_agents):
        """Sets the min_agents of this V1ResourcePool.

        When using dynamic agents, the minimum number of agents that can exist in the resource pool.  # noqa: E501

        :param min_agents: The min_agents of this V1ResourcePool.  # noqa: E501
        :type: int
        """
        if min_agents is None:
            raise ValueError("Invalid value for `min_agents`, must not be `None`")  # noqa: E501

        self._min_agents = min_agents

    @property
    def max_agents(self):
        """Gets the max_agents of this V1ResourcePool.  # noqa: E501

        When using dynamic agents, the maximum number of agents that can exist in the resource pool.  # noqa: E501

        :return: The max_agents of this V1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._max_agents

    @max_agents.setter
    def max_agents(self, max_agents):
        """Sets the max_agents of this V1ResourcePool.

        When using dynamic agents, the maximum number of agents that can exist in the resource pool.  # noqa: E501

        :param max_agents: The max_agents of this V1ResourcePool.  # noqa: E501
        :type: int
        """
        if max_agents is None:
            raise ValueError("Invalid value for `max_agents`, must not be `None`")  # noqa: E501

        self._max_agents = max_agents

    @property
    def slots_per_agent(self):
        """Gets the slots_per_agent of this V1ResourcePool.  # noqa: E501

        The number of slots that exists on an dynamic agent.  # noqa: E501

        :return: The slots_per_agent of this V1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._slots_per_agent

    @slots_per_agent.setter
    def slots_per_agent(self, slots_per_agent):
        """Sets the slots_per_agent of this V1ResourcePool.

        The number of slots that exists on an dynamic agent.  # noqa: E501

        :param slots_per_agent: The slots_per_agent of this V1ResourcePool.  # noqa: E501
        :type: int
        """

        self._slots_per_agent = slots_per_agent

    @property
    def cpu_container_capacity_per_agent(self):
        """Gets the cpu_container_capacity_per_agent of this V1ResourcePool.  # noqa: E501


        :return: The cpu_container_capacity_per_agent of this V1ResourcePool.  # noqa: E501
        :rtype: int
        """
        return self._cpu_container_capacity_per_agent

    @cpu_container_capacity_per_agent.setter
    def cpu_container_capacity_per_agent(self, cpu_container_capacity_per_agent):
        """Sets the cpu_container_capacity_per_agent of this V1ResourcePool.


        :param cpu_container_capacity_per_agent: The cpu_container_capacity_per_agent of this V1ResourcePool.  # noqa: E501
        :type: int
        """
        if cpu_container_capacity_per_agent is None:
            raise ValueError("Invalid value for `cpu_container_capacity_per_agent`, must not be `None`")  # noqa: E501

        self._cpu_container_capacity_per_agent = cpu_container_capacity_per_agent

    @property
    def scheduler_type(self):
        """Gets the scheduler_type of this V1ResourcePool.  # noqa: E501


        :return: The scheduler_type of this V1ResourcePool.  # noqa: E501
        :rtype: V1SchedulerType
        """
        return self._scheduler_type

    @scheduler_type.setter
    def scheduler_type(self, scheduler_type):
        """Sets the scheduler_type of this V1ResourcePool.


        :param scheduler_type: The scheduler_type of this V1ResourcePool.  # noqa: E501
        :type: V1SchedulerType
        """
        if scheduler_type is None:
            raise ValueError("Invalid value for `scheduler_type`, must not be `None`")  # noqa: E501

        self._scheduler_type = scheduler_type

    @property
    def scheduler_fitting_policy(self):
        """Gets the scheduler_fitting_policy of this V1ResourcePool.  # noqa: E501

        The fitting policy of the scheduler.  # noqa: E501

        :return: The scheduler_fitting_policy of this V1ResourcePool.  # noqa: E501
        :rtype: V1FittingPolicy
        """
        return self._scheduler_fitting_policy

    @scheduler_fitting_policy.setter
    def scheduler_fitting_policy(self, scheduler_fitting_policy):
        """Sets the scheduler_fitting_policy of this V1ResourcePool.

        The fitting policy of the scheduler.  # noqa: E501

        :param scheduler_fitting_policy: The scheduler_fitting_policy of this V1ResourcePool.  # noqa: E501
        :type: V1FittingPolicy
        """
        if scheduler_fitting_policy is None:
            raise ValueError("Invalid value for `scheduler_fitting_policy`, must not be `None`")  # noqa: E501

        self._scheduler_fitting_policy = scheduler_fitting_policy

    @property
    def location(self):
        """Gets the location of this V1ResourcePool.  # noqa: E501

        The location of the resource pool. For AWS this returns the region and for GCP this return the zone.  # noqa: E501

        :return: The location of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this V1ResourcePool.

        The location of the resource pool. For AWS this returns the region and for GCP this return the zone.  # noqa: E501

        :param location: The location of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def image_id(self):
        """Gets the image_id of this V1ResourcePool.  # noqa: E501

        The VM image used for the agents when using dynamic agents.  # noqa: E501

        :return: The image_id of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this V1ResourcePool.

        The VM image used for the agents when using dynamic agents.  # noqa: E501

        :param image_id: The image_id of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if image_id is None:
            raise ValueError("Invalid value for `image_id`, must not be `None`")  # noqa: E501

        self._image_id = image_id

    @property
    def instance_type(self):
        """Gets the instance_type of this V1ResourcePool.  # noqa: E501

        The instance type of the agents when using dynamic agents. For AWS this is the Instance Type. For GCP this is the machine type combined with the number and types of GPUs. To work with this data programattically, we recommend working with the ResourcePool.details.aws.instanceType and ResourcePool.details.gcp.machineType/gpuType/gpuNum.  # noqa: E501

        :return: The instance_type of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this V1ResourcePool.

        The instance type of the agents when using dynamic agents. For AWS this is the Instance Type. For GCP this is the machine type combined with the number and types of GPUs. To work with this data programattically, we recommend working with the ResourcePool.details.aws.instanceType and ResourcePool.details.gcp.machineType/gpuType/gpuNum.  # noqa: E501

        :param instance_type: The instance_type of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if instance_type is None:
            raise ValueError("Invalid value for `instance_type`, must not be `None`")  # noqa: E501

        self._instance_type = instance_type

    @property
    def master_url(self):
        """Gets the master_url of this V1ResourcePool.  # noqa: E501


        :return: The master_url of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._master_url

    @master_url.setter
    def master_url(self, master_url):
        """Sets the master_url of this V1ResourcePool.


        :param master_url: The master_url of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if master_url is None:
            raise ValueError("Invalid value for `master_url`, must not be `None`")  # noqa: E501

        self._master_url = master_url

    @property
    def master_cert_name(self):
        """Gets the master_cert_name of this V1ResourcePool.  # noqa: E501


        :return: The master_cert_name of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._master_cert_name

    @master_cert_name.setter
    def master_cert_name(self, master_cert_name):
        """Sets the master_cert_name of this V1ResourcePool.


        :param master_cert_name: The master_cert_name of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if master_cert_name is None:
            raise ValueError("Invalid value for `master_cert_name`, must not be `None`")  # noqa: E501

        self._master_cert_name = master_cert_name

    @property
    def startup_script(self):
        """Gets the startup_script of this V1ResourcePool.  # noqa: E501

        The startup script for the agent. This runs on the node the agent runs on.  # noqa: E501

        :return: The startup_script of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._startup_script

    @startup_script.setter
    def startup_script(self, startup_script):
        """Sets the startup_script of this V1ResourcePool.

        The startup script for the agent. This runs on the node the agent runs on.  # noqa: E501

        :param startup_script: The startup_script of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if startup_script is None:
            raise ValueError("Invalid value for `startup_script`, must not be `None`")  # noqa: E501

        self._startup_script = startup_script

    @property
    def container_startup_script(self):
        """Gets the container_startup_script of this V1ResourcePool.  # noqa: E501

        The startup script for the agent's container. This runs in the container determined-agent runs in.  # noqa: E501

        :return: The container_startup_script of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._container_startup_script

    @container_startup_script.setter
    def container_startup_script(self, container_startup_script):
        """Sets the container_startup_script of this V1ResourcePool.

        The startup script for the agent's container. This runs in the container determined-agent runs in.  # noqa: E501

        :param container_startup_script: The container_startup_script of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if container_startup_script is None:
            raise ValueError("Invalid value for `container_startup_script`, must not be `None`")  # noqa: E501

        self._container_startup_script = container_startup_script

    @property
    def agent_docker_network(self):
        """Gets the agent_docker_network of this V1ResourcePool.  # noqa: E501

        The Docker network to use for the agent when using dynamic agents.  # noqa: E501

        :return: The agent_docker_network of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._agent_docker_network

    @agent_docker_network.setter
    def agent_docker_network(self, agent_docker_network):
        """Sets the agent_docker_network of this V1ResourcePool.

        The Docker network to use for the agent when using dynamic agents.  # noqa: E501

        :param agent_docker_network: The agent_docker_network of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if agent_docker_network is None:
            raise ValueError("Invalid value for `agent_docker_network`, must not be `None`")  # noqa: E501

        self._agent_docker_network = agent_docker_network

    @property
    def agent_docker_runtime(self):
        """Gets the agent_docker_runtime of this V1ResourcePool.  # noqa: E501


        :return: The agent_docker_runtime of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._agent_docker_runtime

    @agent_docker_runtime.setter
    def agent_docker_runtime(self, agent_docker_runtime):
        """Sets the agent_docker_runtime of this V1ResourcePool.


        :param agent_docker_runtime: The agent_docker_runtime of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if agent_docker_runtime is None:
            raise ValueError("Invalid value for `agent_docker_runtime`, must not be `None`")  # noqa: E501

        self._agent_docker_runtime = agent_docker_runtime

    @property
    def agent_docker_image(self):
        """Gets the agent_docker_image of this V1ResourcePool.  # noqa: E501


        :return: The agent_docker_image of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._agent_docker_image

    @agent_docker_image.setter
    def agent_docker_image(self, agent_docker_image):
        """Sets the agent_docker_image of this V1ResourcePool.


        :param agent_docker_image: The agent_docker_image of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if agent_docker_image is None:
            raise ValueError("Invalid value for `agent_docker_image`, must not be `None`")  # noqa: E501

        self._agent_docker_image = agent_docker_image

    @property
    def agent_fluent_image(self):
        """Gets the agent_fluent_image of this V1ResourcePool.  # noqa: E501


        :return: The agent_fluent_image of this V1ResourcePool.  # noqa: E501
        :rtype: str
        """
        return self._agent_fluent_image

    @agent_fluent_image.setter
    def agent_fluent_image(self, agent_fluent_image):
        """Sets the agent_fluent_image of this V1ResourcePool.


        :param agent_fluent_image: The agent_fluent_image of this V1ResourcePool.  # noqa: E501
        :type: str
        """
        if agent_fluent_image is None:
            raise ValueError("Invalid value for `agent_fluent_image`, must not be `None`")  # noqa: E501

        self._agent_fluent_image = agent_fluent_image

    @property
    def max_idle_agent_period(self):
        """Gets the max_idle_agent_period of this V1ResourcePool.  # noqa: E501

        The maximum idle period of agents in seconds. The master waits for this period of time before shutting down idle agents.  # noqa: E501

        :return: The max_idle_agent_period of this V1ResourcePool.  # noqa: E501
        :rtype: float
        """
        return self._max_idle_agent_period

    @max_idle_agent_period.setter
    def max_idle_agent_period(self, max_idle_agent_period):
        """Sets the max_idle_agent_period of this V1ResourcePool.

        The maximum idle period of agents in seconds. The master waits for this period of time before shutting down idle agents.  # noqa: E501

        :param max_idle_agent_period: The max_idle_agent_period of this V1ResourcePool.  # noqa: E501
        :type: float
        """
        if max_idle_agent_period is None:
            raise ValueError("Invalid value for `max_idle_agent_period`, must not be `None`")  # noqa: E501

        self._max_idle_agent_period = max_idle_agent_period

    @property
    def max_agent_starting_period(self):
        """Gets the max_agent_starting_period of this V1ResourcePool.  # noqa: E501

        The maximum starting period of agents in seconds. The master waits for this period of time for starting agents before retrying.  # noqa: E501

        :return: The max_agent_starting_period of this V1ResourcePool.  # noqa: E501
        :rtype: float
        """
        return self._max_agent_starting_period

    @max_agent_starting_period.setter
    def max_agent_starting_period(self, max_agent_starting_period):
        """Sets the max_agent_starting_period of this V1ResourcePool.

        The maximum starting period of agents in seconds. The master waits for this period of time for starting agents before retrying.  # noqa: E501

        :param max_agent_starting_period: The max_agent_starting_period of this V1ResourcePool.  # noqa: E501
        :type: float
        """
        if max_agent_starting_period is None:
            raise ValueError("Invalid value for `max_agent_starting_period`, must not be `None`")  # noqa: E501

        self._max_agent_starting_period = max_agent_starting_period

    @property
    def details(self):
        """Gets the details of this V1ResourcePool.  # noqa: E501


        :return: The details of this V1ResourcePool.  # noqa: E501
        :rtype: V1ResourcePoolDetail
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this V1ResourcePool.


        :param details: The details of this V1ResourcePool.  # noqa: E501
        :type: V1ResourcePoolDetail
        """
        if details is None:
            raise ValueError("Invalid value for `details`, must not be `None`")  # noqa: E501

        self._details = details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V1ResourcePool, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1ResourcePool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
