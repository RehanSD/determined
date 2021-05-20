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


class V1ValidationHistoryEntry(object):
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
        'end_time': 'datetime',
        'searcher_metric': 'float'
    }

    attribute_map = {
        'trial_id': 'trialId',
        'end_time': 'endTime',
        'searcher_metric': 'searcherMetric'
    }

    def __init__(self, trial_id=None, end_time=None, searcher_metric=None):  # noqa: E501
        """V1ValidationHistoryEntry - a model defined in Swagger"""  # noqa: E501

        self._trial_id = None
        self._end_time = None
        self._searcher_metric = None
        self.discriminator = None

        self.trial_id = trial_id
        self.end_time = end_time
        self.searcher_metric = searcher_metric

    @property
    def trial_id(self):
        """Gets the trial_id of this V1ValidationHistoryEntry.  # noqa: E501

        The id for the trial associated with this validation entry.  # noqa: E501

        :return: The trial_id of this V1ValidationHistoryEntry.  # noqa: E501
        :rtype: int
        """
        return self._trial_id

    @trial_id.setter
    def trial_id(self, trial_id):
        """Sets the trial_id of this V1ValidationHistoryEntry.

        The id for the trial associated with this validation entry.  # noqa: E501

        :param trial_id: The trial_id of this V1ValidationHistoryEntry.  # noqa: E501
        :type: int
        """
        if trial_id is None:
            raise ValueError("Invalid value for `trial_id`, must not be `None`")  # noqa: E501

        self._trial_id = trial_id

    @property
    def end_time(self):
        """Gets the end_time of this V1ValidationHistoryEntry.  # noqa: E501

        The time at which the completed validation was reported.  # noqa: E501

        :return: The end_time of this V1ValidationHistoryEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this V1ValidationHistoryEntry.

        The time at which the completed validation was reported.  # noqa: E501

        :param end_time: The end_time of this V1ValidationHistoryEntry.  # noqa: E501
        :type: datetime
        """
        if end_time is None:
            raise ValueError("Invalid value for `end_time`, must not be `None`")  # noqa: E501

        self._end_time = end_time

    @property
    def searcher_metric(self):
        """Gets the searcher_metric of this V1ValidationHistoryEntry.  # noqa: E501

        The value of the `searcher.metric`, indicated by the experiment config, for the validation.  # noqa: E501

        :return: The searcher_metric of this V1ValidationHistoryEntry.  # noqa: E501
        :rtype: float
        """
        return self._searcher_metric

    @searcher_metric.setter
    def searcher_metric(self, searcher_metric):
        """Sets the searcher_metric of this V1ValidationHistoryEntry.

        The value of the `searcher.metric`, indicated by the experiment config, for the validation.  # noqa: E501

        :param searcher_metric: The searcher_metric of this V1ValidationHistoryEntry.  # noqa: E501
        :type: float
        """
        if searcher_metric is None:
            raise ValueError("Invalid value for `searcher_metric`, must not be `None`")  # noqa: E501

        self._searcher_metric = searcher_metric

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
        if issubclass(V1ValidationHistoryEntry, dict):
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
        if not isinstance(other, V1ValidationHistoryEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
