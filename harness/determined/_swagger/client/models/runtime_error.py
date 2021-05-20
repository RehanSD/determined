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


class RuntimeError(object):
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
        'error': 'str',
        'code': 'int',
        'message': 'str',
        'details': 'list[ProtobufAny]'
    }

    attribute_map = {
        'error': 'error',
        'code': 'code',
        'message': 'message',
        'details': 'details'
    }

    def __init__(self, error=None, code=None, message=None, details=None):  # noqa: E501
        """RuntimeError - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._code = None
        self._message = None
        self._details = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if details is not None:
            self.details = details

    @property
    def error(self):
        """Gets the error of this RuntimeError.  # noqa: E501


        :return: The error of this RuntimeError.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RuntimeError.


        :param error: The error of this RuntimeError.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def code(self):
        """Gets the code of this RuntimeError.  # noqa: E501


        :return: The code of this RuntimeError.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RuntimeError.


        :param code: The code of this RuntimeError.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this RuntimeError.  # noqa: E501


        :return: The message of this RuntimeError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RuntimeError.


        :param message: The message of this RuntimeError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def details(self):
        """Gets the details of this RuntimeError.  # noqa: E501


        :return: The details of this RuntimeError.  # noqa: E501
        :rtype: list[ProtobufAny]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this RuntimeError.


        :param details: The details of this RuntimeError.  # noqa: E501
        :type: list[ProtobufAny]
        """

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
        if issubclass(RuntimeError, dict):
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
        if not isinstance(other, RuntimeError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
