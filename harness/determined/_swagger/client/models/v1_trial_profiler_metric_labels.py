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


class V1TrialProfilerMetricLabels(object):
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
        'trial_id': 'int',
        'name': 'str',
        'agent_id': 'str',
        'gpu_uuid': 'str',
        'metric_type': 'TrialProfilerMetricLabelsProfilerMetricType'
    }

    attribute_map = {
        'trial_id': 'trialId',
        'name': 'name',
        'agent_id': 'agentId',
        'gpu_uuid': 'gpuUuid',
        'metric_type': 'metricType'
    }

    def __init__(self, trial_id=None, name=None, agent_id=None, gpu_uuid=None, metric_type=None):  # noqa: E501
        """V1TrialProfilerMetricLabels - a model defined in Swagger"""  # noqa: E501

        self._trial_id = None
        self._name = None
        self._agent_id = None
        self._gpu_uuid = None
        self._metric_type = None
        self.discriminator = None

        self.trial_id = trial_id
        self.name = name
        if agent_id is not None:
            self.agent_id = agent_id
        if gpu_uuid is not None:
            self.gpu_uuid = gpu_uuid
        if metric_type is not None:
            self.metric_type = metric_type

    @property
    def trial_id(self):
        """Gets the trial_id of this V1TrialProfilerMetricLabels.  # noqa: E501

        The ID of the trial.  # noqa: E501

        :return: The trial_id of this V1TrialProfilerMetricLabels.  # noqa: E501
        :rtype: int
        """
        return self._trial_id

    @trial_id.setter
    def trial_id(self, trial_id):
        """Sets the trial_id of this V1TrialProfilerMetricLabels.

        The ID of the trial.  # noqa: E501

        :param trial_id: The trial_id of this V1TrialProfilerMetricLabels.  # noqa: E501
        :type: int
        """
        if trial_id is None:
            raise ValueError("Invalid value for `trial_id`, must not be `None`")  # noqa: E501

        self._trial_id = trial_id

    @property
    def name(self):
        """Gets the name of this V1TrialProfilerMetricLabels.  # noqa: E501

        The name of the metric.  # noqa: E501

        :return: The name of this V1TrialProfilerMetricLabels.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1TrialProfilerMetricLabels.

        The name of the metric.  # noqa: E501

        :param name: The name of this V1TrialProfilerMetricLabels.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def agent_id(self):
        """Gets the agent_id of this V1TrialProfilerMetricLabels.  # noqa: E501

        The agent ID associated with the metric.  # noqa: E501

        :return: The agent_id of this V1TrialProfilerMetricLabels.  # noqa: E501
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this V1TrialProfilerMetricLabels.

        The agent ID associated with the metric.  # noqa: E501

        :param agent_id: The agent_id of this V1TrialProfilerMetricLabels.  # noqa: E501
        :type: str
        """

        self._agent_id = agent_id

    @property
    def gpu_uuid(self):
        """Gets the gpu_uuid of this V1TrialProfilerMetricLabels.  # noqa: E501

        The GPU UUID associated with the metric.  # noqa: E501

        :return: The gpu_uuid of this V1TrialProfilerMetricLabels.  # noqa: E501
        :rtype: str
        """
        return self._gpu_uuid

    @gpu_uuid.setter
    def gpu_uuid(self, gpu_uuid):
        """Sets the gpu_uuid of this V1TrialProfilerMetricLabels.

        The GPU UUID associated with the metric.  # noqa: E501

        :param gpu_uuid: The gpu_uuid of this V1TrialProfilerMetricLabels.  # noqa: E501
        :type: str
        """

        self._gpu_uuid = gpu_uuid

    @property
    def metric_type(self):
        """Gets the metric_type of this V1TrialProfilerMetricLabels.  # noqa: E501

        The type of the metric.  # noqa: E501

        :return: The metric_type of this V1TrialProfilerMetricLabels.  # noqa: E501
        :rtype: TrialProfilerMetricLabelsProfilerMetricType
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this V1TrialProfilerMetricLabels.

        The type of the metric.  # noqa: E501

        :param metric_type: The metric_type of this V1TrialProfilerMetricLabels.  # noqa: E501
        :type: TrialProfilerMetricLabelsProfilerMetricType
        """

        self._metric_type = metric_type

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
        if issubclass(V1TrialProfilerMetricLabels, dict):
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
        if not isinstance(other, V1TrialProfilerMetricLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
