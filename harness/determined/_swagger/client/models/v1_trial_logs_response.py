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


class V1TrialLogsResponse(object):
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
        'id': 'str',
        'timestamp': 'datetime',
        'message': 'str',
        'level': 'V1LogLevel'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'message': 'message',
        'level': 'level'
    }

    def __init__(self, id=None, timestamp=None, message=None, level=None):  # noqa: E501
        """V1TrialLogsResponse - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._timestamp = None
        self._message = None
        self._level = None
        self.discriminator = None

        self.id = id
        self.timestamp = timestamp
        self.message = message
        self.level = level

    @property
    def id(self):
        """Gets the id of this V1TrialLogsResponse.  # noqa: E501

        The ID of the trial log.  # noqa: E501

        :return: The id of this V1TrialLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1TrialLogsResponse.

        The ID of the trial log.  # noqa: E501

        :param id: The id of this V1TrialLogsResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this V1TrialLogsResponse.  # noqa: E501

        The timestamp of the log.  # noqa: E501

        :return: The timestamp of this V1TrialLogsResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this V1TrialLogsResponse.

        The timestamp of the log.  # noqa: E501

        :param timestamp: The timestamp of this V1TrialLogsResponse.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def message(self):
        """Gets the message of this V1TrialLogsResponse.  # noqa: E501

        The log message.  # noqa: E501

        :return: The message of this V1TrialLogsResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1TrialLogsResponse.

        The log message.  # noqa: E501

        :param message: The message of this V1TrialLogsResponse.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def level(self):
        """Gets the level of this V1TrialLogsResponse.  # noqa: E501

        The level of the log.  # noqa: E501

        :return: The level of this V1TrialLogsResponse.  # noqa: E501
        :rtype: V1LogLevel
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this V1TrialLogsResponse.

        The level of the log.  # noqa: E501

        :param level: The level of this V1TrialLogsResponse.  # noqa: E501
        :type: V1LogLevel
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

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
        if issubclass(V1TrialLogsResponse, dict):
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
        if not isinstance(other, V1TrialLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
