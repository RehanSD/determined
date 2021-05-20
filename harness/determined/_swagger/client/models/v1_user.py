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


class V1User(object):
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
        'id': 'int',
        'username': 'str',
        'admin': 'bool',
        'active': 'bool',
        'agent_user_group': 'V1AgentUserGroup'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'admin': 'admin',
        'active': 'active',
        'agent_user_group': 'agentUserGroup'
    }

    def __init__(self, id=None, username=None, admin=None, active=None, agent_user_group=None):  # noqa: E501
        """V1User - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._username = None
        self._admin = None
        self._active = None
        self._agent_user_group = None
        self.discriminator = None

        self.id = id
        self.username = username
        self.admin = admin
        self.active = active
        if agent_user_group is not None:
            self.agent_user_group = agent_user_group

    @property
    def id(self):
        """Gets the id of this V1User.  # noqa: E501

        The user ID.  # noqa: E501

        :return: The id of this V1User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1User.

        The user ID.  # noqa: E501

        :param id: The id of this V1User.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def username(self):
        """Gets the username of this V1User.  # noqa: E501

        The user login name of the user.  # noqa: E501

        :return: The username of this V1User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this V1User.

        The user login name of the user.  # noqa: E501

        :param username: The username of this V1User.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def admin(self):
        """Gets the admin of this V1User.  # noqa: E501

        Bool denoting whether the account is an admin account.  # noqa: E501

        :return: The admin of this V1User.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this V1User.

        Bool denoting whether the account is an admin account.  # noqa: E501

        :param admin: The admin of this V1User.  # noqa: E501
        :type: bool
        """
        if admin is None:
            raise ValueError("Invalid value for `admin`, must not be `None`")  # noqa: E501

        self._admin = admin

    @property
    def active(self):
        """Gets the active of this V1User.  # noqa: E501

        Bool denoting whether the account is active.  # noqa: E501

        :return: The active of this V1User.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this V1User.

        Bool denoting whether the account is active.  # noqa: E501

        :param active: The active of this V1User.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def agent_user_group(self):
        """Gets the agent_user_group of this V1User.  # noqa: E501

        The user and group on the agent host machine.  # noqa: E501

        :return: The agent_user_group of this V1User.  # noqa: E501
        :rtype: V1AgentUserGroup
        """
        return self._agent_user_group

    @agent_user_group.setter
    def agent_user_group(self, agent_user_group):
        """Sets the agent_user_group of this V1User.

        The user and group on the agent host machine.  # noqa: E501

        :param agent_user_group: The agent_user_group of this V1User.  # noqa: E501
        :type: V1AgentUserGroup
        """

        self._agent_user_group = agent_user_group

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
        if issubclass(V1User, dict):
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
        if not isinstance(other, V1User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
