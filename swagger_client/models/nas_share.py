# coding: utf-8

"""
    Nodeum API

    Nodeum API  # Filter parameters When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NasShare(object):
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
        'nas_id': 'int',
        'nas_pool_id': 'int',
        'path': 'str',
        'options': 'str',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'id': 'id',
        'nas_id': 'nas_id',
        'nas_pool_id': 'nas_pool_id',
        'path': 'path',
        'options': 'options',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, id=None, nas_id=None, nas_pool_id=None, path=None, options=None, username=None, password=None):  # noqa: E501
        """NasShare - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._nas_id = None
        self._nas_pool_id = None
        self._path = None
        self._options = None
        self._username = None
        self._password = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if nas_id is not None:
            self.nas_id = nas_id
        if nas_pool_id is not None:
            self.nas_pool_id = nas_pool_id
        if path is not None:
            self.path = path
        if options is not None:
            self.options = options
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def id(self):
        """Gets the id of this NasShare.  # noqa: E501


        :return: The id of this NasShare.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NasShare.


        :param id: The id of this NasShare.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def nas_id(self):
        """Gets the nas_id of this NasShare.  # noqa: E501


        :return: The nas_id of this NasShare.  # noqa: E501
        :rtype: int
        """
        return self._nas_id

    @nas_id.setter
    def nas_id(self, nas_id):
        """Sets the nas_id of this NasShare.


        :param nas_id: The nas_id of this NasShare.  # noqa: E501
        :type: int
        """

        self._nas_id = nas_id

    @property
    def nas_pool_id(self):
        """Gets the nas_pool_id of this NasShare.  # noqa: E501


        :return: The nas_pool_id of this NasShare.  # noqa: E501
        :rtype: int
        """
        return self._nas_pool_id

    @nas_pool_id.setter
    def nas_pool_id(self, nas_pool_id):
        """Sets the nas_pool_id of this NasShare.


        :param nas_pool_id: The nas_pool_id of this NasShare.  # noqa: E501
        :type: int
        """

        self._nas_pool_id = nas_pool_id

    @property
    def path(self):
        """Gets the path of this NasShare.  # noqa: E501


        :return: The path of this NasShare.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this NasShare.


        :param path: The path of this NasShare.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def options(self):
        """Gets the options of this NasShare.  # noqa: E501


        :return: The options of this NasShare.  # noqa: E501
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this NasShare.


        :param options: The options of this NasShare.  # noqa: E501
        :type: str
        """

        self._options = options

    @property
    def username(self):
        """Gets the username of this NasShare.  # noqa: E501


        :return: The username of this NasShare.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this NasShare.


        :param username: The username of this NasShare.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this NasShare.  # noqa: E501


        :return: The password of this NasShare.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NasShare.


        :param password: The password of this NasShare.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(NasShare, dict):
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
        if not isinstance(other, NasShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
