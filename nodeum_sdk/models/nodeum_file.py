# coding: utf-8

"""
    Nodeum API

    The Nodeum API makes it easy to tap into the digital data mesh that runs across your organisation. Make requests to our API endpoints and we’ll give you everything you need to interconnect your business workflows with your storage.  All production API requests are made to:  http://nodeumhostname/api/  The current production version of the API is v1.   **REST** The Nodeum API is a RESTful API. This means that the API is designed to allow you to get, create, update, & delete objects with the HTTP verbs GET, POST, PUT, PATCH, & DELETE.  **JSON** The Nodeum API speaks exclusively in JSON. This means that you should always set the Content-Type header to application/json to ensure that your requests are properly accepted and processed by the API.  **Authentication** All API calls require user-password authentication.   **Cross-Origin Resource Sharing** The Nodeum API supports CORS for communicating from Javascript for these endpoints. You will need to specify an Origin URI when creating your application to allow for CORS to be whitelisted for your domain.   **Pagination** Some endpoints such as File Listing return a potentially lengthy array of objects. In order to keep the response sizes manageable the API will take advantage of pagination. Pagination is a mechanism for returning a subset of the results for a request and allowing for subsequent requests to “page” through the rest of the results until the end is reached. Paginated endpoints follow a standard interface that accepts two query parameters, limit and offset, and return a payload that follows a standard form. These parameters names and their behavior are borrowed from SQL LIMIT and OFFSET keywords.  **Versioning** The Nodeum API is constantly being worked on to add features, make improvements, and fix bugs. This means that you should expect changes to be introduced and documented.   However, there are some changes or additions that are considered backwards-compatible and your applications should be flexible enough to handle them. These include:  - Adding new endpoints to the API - Adding new attributes to the response of an existing endpoint - Changing the order of attributes of responses (JSON by definition is an object of unordered key/value pairs)  **Filter parameters** When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: info@nodeum.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from nodeum_sdk.configuration import Configuration


class NodeumFile(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'name': 'str',
        'parent': 'int',
        'primary_id': 'int',
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
        'primary_id': 'primary_id',
        'type': 'type',
        'permission': 'permission',
        'size': 'size',
        'change_date': 'change_date',
        'modification_date': 'modification_date',
        'access_date': 'access_date',
        'uid': 'uid',
        'gid': 'gid'
    }

    def __init__(self, id=None, name=None, parent=None, primary_id=None, type=None, permission=None, size=None, change_date=None, modification_date=None, access_date=None, uid=None, gid=None, local_vars_configuration=None):  # noqa: E501
        """NodeumFile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._parent = None
        self._primary_id = None
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
        if primary_id is not None:
            self.primary_id = primary_id
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
    def primary_id(self):
        """Gets the primary_id of this NodeumFile.  # noqa: E501


        :return: The primary_id of this NodeumFile.  # noqa: E501
        :rtype: int
        """
        return self._primary_id

    @primary_id.setter
    def primary_id(self, primary_id):
        """Sets the primary_id of this NodeumFile.


        :param primary_id: The primary_id of this NodeumFile.  # noqa: E501
        :type: int
        """

        self._primary_id = primary_id

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
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
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

        for attr, _ in six.iteritems(self.openapi_types):
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

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeumFile):
            return True

        return self.to_dict() != other.to_dict()
