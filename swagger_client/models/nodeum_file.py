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


class NodeumFile(object):
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
        'name': 'str',
        'parent': 'int',
        'type': 'str',
        'permission': 'int',
        'size': 'int',
        'change_date': 'str',
        'modification_date': 'str',
        'access_date': 'str',
        'uid': 'int',
        'gid': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'parent': 'parent',
        'type': 'type',
        'permission': 'permission',
        'size': 'size',
        'change_date': 'change_date',
        'modification_date': 'modification_date',
        'access_date': 'access_date',
        'uid': 'uid',
        'gid': 'gid'
    }

    def __init__(self, id=None, name=None, parent=None, type=None, permission=None, size=None, change_date=None, modification_date=None, access_date=None, uid=None, gid=None):  # noqa: E501
        """NodeumFile - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._parent = None
        self._type = None
        self._permission = None
        self._size = None
        self._change_date = None
        self._modification_date = None
        self._access_date = None
        self._uid = None
        self._gid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if type is not None:
            self.type = type
        if permission is not None:
            self.permission = permission
        if size is not None:
            self.size = size
        if change_date is not None:
            self.change_date = change_date
        if modification_date is not None:
            self.modification_date = modification_date
        if access_date is not None:
            self.access_date = access_date
        if uid is not None:
            self.uid = uid
        if gid is not None:
            self.gid = gid

    @property
    def id(self):
        """Gets the id of this NodeumFile.  # noqa: E501


        :return: The id of this NodeumFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeumFile.


        :param id: The id of this NodeumFile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NodeumFile.  # noqa: E501


        :return: The name of this NodeumFile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeumFile.


        :param name: The name of this NodeumFile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this NodeumFile.  # noqa: E501


        :return: The parent of this NodeumFile.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this NodeumFile.


        :param parent: The parent of this NodeumFile.  # noqa: E501
        :type: int
        """

        self._parent = parent

    @property
    def type(self):
        """Gets the type of this NodeumFile.  # noqa: E501


        :return: The type of this NodeumFile.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeumFile.


        :param type: The type of this NodeumFile.  # noqa: E501
        :type: str
        """
        allowed_values = ["file", "folder"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def permission(self):
        """Gets the permission of this NodeumFile.  # noqa: E501


        :return: The permission of this NodeumFile.  # noqa: E501
        :rtype: int
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this NodeumFile.


        :param permission: The permission of this NodeumFile.  # noqa: E501
        :type: int
        """

        self._permission = permission

    @property
    def size(self):
        """Gets the size of this NodeumFile.  # noqa: E501


        :return: The size of this NodeumFile.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this NodeumFile.


        :param size: The size of this NodeumFile.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def change_date(self):
        """Gets the change_date of this NodeumFile.  # noqa: E501


        :return: The change_date of this NodeumFile.  # noqa: E501
        :rtype: str
        """
        return self._change_date

    @change_date.setter
    def change_date(self, change_date):
        """Sets the change_date of this NodeumFile.


        :param change_date: The change_date of this NodeumFile.  # noqa: E501
        :type: str
        """

        self._change_date = change_date

    @property
    def modification_date(self):
        """Gets the modification_date of this NodeumFile.  # noqa: E501


        :return: The modification_date of this NodeumFile.  # noqa: E501
        :rtype: str
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this NodeumFile.


        :param modification_date: The modification_date of this NodeumFile.  # noqa: E501
        :type: str
        """

        self._modification_date = modification_date

    @property
    def access_date(self):
        """Gets the access_date of this NodeumFile.  # noqa: E501


        :return: The access_date of this NodeumFile.  # noqa: E501
        :rtype: str
        """
        return self._access_date

    @access_date.setter
    def access_date(self, access_date):
        """Sets the access_date of this NodeumFile.


        :param access_date: The access_date of this NodeumFile.  # noqa: E501
        :type: str
        """

        self._access_date = access_date

    @property
    def uid(self):
        """Gets the uid of this NodeumFile.  # noqa: E501


        :return: The uid of this NodeumFile.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this NodeumFile.


        :param uid: The uid of this NodeumFile.  # noqa: E501
        :type: int
        """

        self._uid = uid

    @property
    def gid(self):
        """Gets the gid of this NodeumFile.  # noqa: E501


        :return: The gid of this NodeumFile.  # noqa: E501
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this NodeumFile.


        :param gid: The gid of this NodeumFile.  # noqa: E501
        :type: int
        """

        self._gid = gid

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
        if issubclass(NodeumFile, dict):
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
        if not isinstance(other, NodeumFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
