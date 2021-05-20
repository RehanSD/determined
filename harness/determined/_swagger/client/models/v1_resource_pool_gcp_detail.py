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


class V1ResourcePoolGcpDetail(object):
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
        'project': 'str',
        'zone': 'str',
        'boot_disk_size': 'int',
        'boot_disk_source_image': 'str',
        'label_key': 'str',
        'label_value': 'str',
        'name_prefix': 'str',
        'network': 'str',
        'subnetwork': 'str',
        'external_ip': 'bool',
        'network_tags': 'list[str]',
        'service_account_email': 'str',
        'service_account_scopes': 'list[str]',
        'machine_type': 'str',
        'gpu_type': 'str',
        'gpu_num': 'int',
        'preemptible': 'bool',
        'operation_timeout_period': 'float'
    }

    attribute_map = {
        'project': 'project',
        'zone': 'zone',
        'boot_disk_size': 'bootDiskSize',
        'boot_disk_source_image': 'bootDiskSourceImage',
        'label_key': 'labelKey',
        'label_value': 'labelValue',
        'name_prefix': 'namePrefix',
        'network': 'network',
        'subnetwork': 'subnetwork',
        'external_ip': 'externalIp',
        'network_tags': 'networkTags',
        'service_account_email': 'serviceAccountEmail',
        'service_account_scopes': 'serviceAccountScopes',
        'machine_type': 'machineType',
        'gpu_type': 'gpuType',
        'gpu_num': 'gpuNum',
        'preemptible': 'preemptible',
        'operation_timeout_period': 'operationTimeoutPeriod'
    }

    def __init__(self, project=None, zone=None, boot_disk_size=None, boot_disk_source_image=None, label_key=None, label_value=None, name_prefix=None, network=None, subnetwork=None, external_ip=None, network_tags=None, service_account_email=None, service_account_scopes=None, machine_type=None, gpu_type=None, gpu_num=None, preemptible=None, operation_timeout_period=None):  # noqa: E501
        """V1ResourcePoolGcpDetail - a model defined in Swagger"""  # noqa: E501

        self._project = None
        self._zone = None
        self._boot_disk_size = None
        self._boot_disk_source_image = None
        self._label_key = None
        self._label_value = None
        self._name_prefix = None
        self._network = None
        self._subnetwork = None
        self._external_ip = None
        self._network_tags = None
        self._service_account_email = None
        self._service_account_scopes = None
        self._machine_type = None
        self._gpu_type = None
        self._gpu_num = None
        self._preemptible = None
        self._operation_timeout_period = None
        self.discriminator = None

        self.project = project
        self.zone = zone
        self.boot_disk_size = boot_disk_size
        self.boot_disk_source_image = boot_disk_source_image
        self.label_key = label_key
        self.label_value = label_value
        self.name_prefix = name_prefix
        self.network = network
        if subnetwork is not None:
            self.subnetwork = subnetwork
        self.external_ip = external_ip
        if network_tags is not None:
            self.network_tags = network_tags
        self.service_account_email = service_account_email
        self.service_account_scopes = service_account_scopes
        self.machine_type = machine_type
        self.gpu_type = gpu_type
        self.gpu_num = gpu_num
        self.preemptible = preemptible
        self.operation_timeout_period = operation_timeout_period

    @property
    def project(self):
        """Gets the project of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The project of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this V1ResourcePoolGcpDetail.


        :param project: The project of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def zone(self):
        """Gets the zone of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The zone of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this V1ResourcePoolGcpDetail.


        :param zone: The zone of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if zone is None:
            raise ValueError("Invalid value for `zone`, must not be `None`")  # noqa: E501

        self._zone = zone

    @property
    def boot_disk_size(self):
        """Gets the boot_disk_size of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The boot_disk_size of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: int
        """
        return self._boot_disk_size

    @boot_disk_size.setter
    def boot_disk_size(self, boot_disk_size):
        """Sets the boot_disk_size of this V1ResourcePoolGcpDetail.


        :param boot_disk_size: The boot_disk_size of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: int
        """
        if boot_disk_size is None:
            raise ValueError("Invalid value for `boot_disk_size`, must not be `None`")  # noqa: E501

        self._boot_disk_size = boot_disk_size

    @property
    def boot_disk_source_image(self):
        """Gets the boot_disk_source_image of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The boot_disk_source_image of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._boot_disk_source_image

    @boot_disk_source_image.setter
    def boot_disk_source_image(self, boot_disk_source_image):
        """Sets the boot_disk_source_image of this V1ResourcePoolGcpDetail.


        :param boot_disk_source_image: The boot_disk_source_image of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if boot_disk_source_image is None:
            raise ValueError("Invalid value for `boot_disk_source_image`, must not be `None`")  # noqa: E501

        self._boot_disk_source_image = boot_disk_source_image

    @property
    def label_key(self):
        """Gets the label_key of this V1ResourcePoolGcpDetail.  # noqa: E501

        Key for labeling the Determined agent instances.  # noqa: E501

        :return: The label_key of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._label_key

    @label_key.setter
    def label_key(self, label_key):
        """Sets the label_key of this V1ResourcePoolGcpDetail.

        Key for labeling the Determined agent instances.  # noqa: E501

        :param label_key: The label_key of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if label_key is None:
            raise ValueError("Invalid value for `label_key`, must not be `None`")  # noqa: E501

        self._label_key = label_key

    @property
    def label_value(self):
        """Gets the label_value of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The label_value of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._label_value

    @label_value.setter
    def label_value(self, label_value):
        """Sets the label_value of this V1ResourcePoolGcpDetail.


        :param label_value: The label_value of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if label_value is None:
            raise ValueError("Invalid value for `label_value`, must not be `None`")  # noqa: E501

        self._label_value = label_value

    @property
    def name_prefix(self):
        """Gets the name_prefix of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The name_prefix of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._name_prefix

    @name_prefix.setter
    def name_prefix(self, name_prefix):
        """Sets the name_prefix of this V1ResourcePoolGcpDetail.


        :param name_prefix: The name_prefix of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if name_prefix is None:
            raise ValueError("Invalid value for `name_prefix`, must not be `None`")  # noqa: E501

        self._name_prefix = name_prefix

    @property
    def network(self):
        """Gets the network of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The network of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this V1ResourcePoolGcpDetail.


        :param network: The network of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def subnetwork(self):
        """Gets the subnetwork of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The subnetwork of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._subnetwork

    @subnetwork.setter
    def subnetwork(self, subnetwork):
        """Sets the subnetwork of this V1ResourcePoolGcpDetail.


        :param subnetwork: The subnetwork of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """

        self._subnetwork = subnetwork

    @property
    def external_ip(self):
        """Gets the external_ip of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The external_ip of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: bool
        """
        return self._external_ip

    @external_ip.setter
    def external_ip(self, external_ip):
        """Sets the external_ip of this V1ResourcePoolGcpDetail.


        :param external_ip: The external_ip of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: bool
        """
        if external_ip is None:
            raise ValueError("Invalid value for `external_ip`, must not be `None`")  # noqa: E501

        self._external_ip = external_ip

    @property
    def network_tags(self):
        """Gets the network_tags of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The network_tags of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._network_tags

    @network_tags.setter
    def network_tags(self, network_tags):
        """Sets the network_tags of this V1ResourcePoolGcpDetail.


        :param network_tags: The network_tags of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: list[str]
        """

        self._network_tags = network_tags

    @property
    def service_account_email(self):
        """Gets the service_account_email of this V1ResourcePoolGcpDetail.  # noqa: E501

        Email of the service account for the Determined agent instances.  # noqa: E501

        :return: The service_account_email of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._service_account_email

    @service_account_email.setter
    def service_account_email(self, service_account_email):
        """Sets the service_account_email of this V1ResourcePoolGcpDetail.

        Email of the service account for the Determined agent instances.  # noqa: E501

        :param service_account_email: The service_account_email of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if service_account_email is None:
            raise ValueError("Invalid value for `service_account_email`, must not be `None`")  # noqa: E501

        self._service_account_email = service_account_email

    @property
    def service_account_scopes(self):
        """Gets the service_account_scopes of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The service_account_scopes of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_account_scopes

    @service_account_scopes.setter
    def service_account_scopes(self, service_account_scopes):
        """Sets the service_account_scopes of this V1ResourcePoolGcpDetail.


        :param service_account_scopes: The service_account_scopes of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: list[str]
        """
        if service_account_scopes is None:
            raise ValueError("Invalid value for `service_account_scopes`, must not be `None`")  # noqa: E501

        self._service_account_scopes = service_account_scopes

    @property
    def machine_type(self):
        """Gets the machine_type of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The machine_type of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this V1ResourcePoolGcpDetail.


        :param machine_type: The machine_type of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if machine_type is None:
            raise ValueError("Invalid value for `machine_type`, must not be `None`")  # noqa: E501

        self._machine_type = machine_type

    @property
    def gpu_type(self):
        """Gets the gpu_type of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The gpu_type of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        """Sets the gpu_type of this V1ResourcePoolGcpDetail.


        :param gpu_type: The gpu_type of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: str
        """
        if gpu_type is None:
            raise ValueError("Invalid value for `gpu_type`, must not be `None`")  # noqa: E501

        self._gpu_type = gpu_type

    @property
    def gpu_num(self):
        """Gets the gpu_num of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The gpu_num of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: int
        """
        return self._gpu_num

    @gpu_num.setter
    def gpu_num(self, gpu_num):
        """Sets the gpu_num of this V1ResourcePoolGcpDetail.


        :param gpu_num: The gpu_num of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: int
        """
        if gpu_num is None:
            raise ValueError("Invalid value for `gpu_num`, must not be `None`")  # noqa: E501

        self._gpu_num = gpu_num

    @property
    def preemptible(self):
        """Gets the preemptible of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The preemptible of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: bool
        """
        return self._preemptible

    @preemptible.setter
    def preemptible(self, preemptible):
        """Sets the preemptible of this V1ResourcePoolGcpDetail.


        :param preemptible: The preemptible of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: bool
        """
        if preemptible is None:
            raise ValueError("Invalid value for `preemptible`, must not be `None`")  # noqa: E501

        self._preemptible = preemptible

    @property
    def operation_timeout_period(self):
        """Gets the operation_timeout_period of this V1ResourcePoolGcpDetail.  # noqa: E501


        :return: The operation_timeout_period of this V1ResourcePoolGcpDetail.  # noqa: E501
        :rtype: float
        """
        return self._operation_timeout_period

    @operation_timeout_period.setter
    def operation_timeout_period(self, operation_timeout_period):
        """Sets the operation_timeout_period of this V1ResourcePoolGcpDetail.


        :param operation_timeout_period: The operation_timeout_period of this V1ResourcePoolGcpDetail.  # noqa: E501
        :type: float
        """
        if operation_timeout_period is None:
            raise ValueError("Invalid value for `operation_timeout_period`, must not be `None`")  # noqa: E501

        self._operation_timeout_period = operation_timeout_period

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
        if issubclass(V1ResourcePoolGcpDetail, dict):
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
        if not isinstance(other, V1ResourcePoolGcpDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
