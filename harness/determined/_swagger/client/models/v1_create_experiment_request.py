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


class V1CreateExperimentRequest(object):
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
        'model_definition': 'list[V1File]',
        'config': 'str',
        'validate_only': 'bool',
        'parent_id': 'int'
    }

    attribute_map = {
        'model_definition': 'modelDefinition',
        'config': 'config',
        'validate_only': 'validateOnly',
        'parent_id': 'parentId'
    }

    def __init__(self, model_definition=None, config=None, validate_only=None, parent_id=None):  # noqa: E501
        """V1CreateExperimentRequest - a model defined in Swagger"""  # noqa: E501

        self._model_definition = None
        self._config = None
        self._validate_only = None
        self._parent_id = None
        self.discriminator = None

        if model_definition is not None:
            self.model_definition = model_definition
        if config is not None:
            self.config = config
        if validate_only is not None:
            self.validate_only = validate_only
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def model_definition(self):
        """Gets the model_definition of this V1CreateExperimentRequest.  # noqa: E501

        Experiment context.  # noqa: E501

        :return: The model_definition of this V1CreateExperimentRequest.  # noqa: E501
        :rtype: list[V1File]
        """
        return self._model_definition

    @model_definition.setter
    def model_definition(self, model_definition):
        """Sets the model_definition of this V1CreateExperimentRequest.

        Experiment context.  # noqa: E501

        :param model_definition: The model_definition of this V1CreateExperimentRequest.  # noqa: E501
        :type: list[V1File]
        """

        self._model_definition = model_definition

    @property
    def config(self):
        """Gets the config of this V1CreateExperimentRequest.  # noqa: E501

        Experiment config (YAML).  # noqa: E501

        :return: The config of this V1CreateExperimentRequest.  # noqa: E501
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this V1CreateExperimentRequest.

        Experiment config (YAML).  # noqa: E501

        :param config: The config of this V1CreateExperimentRequest.  # noqa: E501
        :type: str
        """

        self._config = config

    @property
    def validate_only(self):
        """Gets the validate_only of this V1CreateExperimentRequest.  # noqa: E501

        Only validate instead of creating the experiment. A dry run.  # noqa: E501

        :return: The validate_only of this V1CreateExperimentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._validate_only

    @validate_only.setter
    def validate_only(self, validate_only):
        """Sets the validate_only of this V1CreateExperimentRequest.

        Only validate instead of creating the experiment. A dry run.  # noqa: E501

        :param validate_only: The validate_only of this V1CreateExperimentRequest.  # noqa: E501
        :type: bool
        """

        self._validate_only = validate_only

    @property
    def parent_id(self):
        """Gets the parent_id of this V1CreateExperimentRequest.  # noqa: E501

        Parent experiment id.  # noqa: E501

        :return: The parent_id of this V1CreateExperimentRequest.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this V1CreateExperimentRequest.

        Parent experiment id.  # noqa: E501

        :param parent_id: The parent_id of this V1CreateExperimentRequest.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

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
        if issubclass(V1CreateExperimentRequest, dict):
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
        if not isinstance(other, V1CreateExperimentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
