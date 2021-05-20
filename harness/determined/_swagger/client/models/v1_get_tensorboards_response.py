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


class V1GetTensorboardsResponse(object):
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
        'tensorboards': 'list[V1Tensorboard]',
        'pagination': 'V1Pagination'
    }

    attribute_map = {
        'tensorboards': 'tensorboards',
        'pagination': 'pagination'
    }

    def __init__(self, tensorboards=None, pagination=None):  # noqa: E501
        """V1GetTensorboardsResponse - a model defined in Swagger"""  # noqa: E501

        self._tensorboards = None
        self._pagination = None
        self.discriminator = None

        if tensorboards is not None:
            self.tensorboards = tensorboards
        if pagination is not None:
            self.pagination = pagination

    @property
    def tensorboards(self):
        """Gets the tensorboards of this V1GetTensorboardsResponse.  # noqa: E501

        The list of returned tensorboards.  # noqa: E501

        :return: The tensorboards of this V1GetTensorboardsResponse.  # noqa: E501
        :rtype: list[V1Tensorboard]
        """
        return self._tensorboards

    @tensorboards.setter
    def tensorboards(self, tensorboards):
        """Sets the tensorboards of this V1GetTensorboardsResponse.

        The list of returned tensorboards.  # noqa: E501

        :param tensorboards: The tensorboards of this V1GetTensorboardsResponse.  # noqa: E501
        :type: list[V1Tensorboard]
        """

        self._tensorboards = tensorboards

    @property
    def pagination(self):
        """Gets the pagination of this V1GetTensorboardsResponse.  # noqa: E501

        Pagination information of the full dataset.  # noqa: E501

        :return: The pagination of this V1GetTensorboardsResponse.  # noqa: E501
        :rtype: V1Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this V1GetTensorboardsResponse.

        Pagination information of the full dataset.  # noqa: E501

        :param pagination: The pagination of this V1GetTensorboardsResponse.  # noqa: E501
        :type: V1Pagination
        """

        self._pagination = pagination

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
        if issubclass(V1GetTensorboardsResponse, dict):
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
        if not isinstance(other, V1GetTensorboardsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
