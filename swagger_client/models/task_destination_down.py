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


class TaskDestinationDown(object):
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
        'folder': 'object',
        'tape_id': 'int',
        'tape_pool_id': 'int',
        'cloud_pool_id': 'int',
        'nas_pool_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'folder': 'folder',
        'tape_id': 'tape_id',
        'tape_pool_id': 'tape_pool_id',
        'cloud_pool_id': 'cloud_pool_id',
        'nas_pool_id': 'nas_pool_id'
    }

    def __init__(self, id=None, folder=None, tape_id=None, tape_pool_id=None, cloud_pool_id=None, nas_pool_id=None):  # noqa: E501
        """TaskDestinationDown - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._folder = None
        self._tape_id = None
        self._tape_pool_id = None
        self._cloud_pool_id = None
        self._nas_pool_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if folder is not None:
            self.folder = folder
        if tape_id is not None:
            self.tape_id = tape_id
        if tape_pool_id is not None:
            self.tape_pool_id = tape_pool_id
        if cloud_pool_id is not None:
            self.cloud_pool_id = cloud_pool_id
        if nas_pool_id is not None:
            self.nas_pool_id = nas_pool_id

    @property
    def id(self):
        """Gets the id of this TaskDestinationDown.  # noqa: E501


        :return: The id of this TaskDestinationDown.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskDestinationDown.


        :param id: The id of this TaskDestinationDown.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def folder(self):
        """Gets the folder of this TaskDestinationDown.  # noqa: E501


        :return: The folder of this TaskDestinationDown.  # noqa: E501
        :rtype: object
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this TaskDestinationDown.


        :param folder: The folder of this TaskDestinationDown.  # noqa: E501
        :type: object
        """

        self._folder = folder

    @property
    def tape_id(self):
        """Gets the tape_id of this TaskDestinationDown.  # noqa: E501


        :return: The tape_id of this TaskDestinationDown.  # noqa: E501
        :rtype: int
        """
        return self._tape_id

    @tape_id.setter
    def tape_id(self, tape_id):
        """Sets the tape_id of this TaskDestinationDown.


        :param tape_id: The tape_id of this TaskDestinationDown.  # noqa: E501
        :type: int
        """

        self._tape_id = tape_id

    @property
    def tape_pool_id(self):
        """Gets the tape_pool_id of this TaskDestinationDown.  # noqa: E501


        :return: The tape_pool_id of this TaskDestinationDown.  # noqa: E501
        :rtype: int
        """
        return self._tape_pool_id

    @tape_pool_id.setter
    def tape_pool_id(self, tape_pool_id):
        """Sets the tape_pool_id of this TaskDestinationDown.


        :param tape_pool_id: The tape_pool_id of this TaskDestinationDown.  # noqa: E501
        :type: int
        """

        self._tape_pool_id = tape_pool_id

    @property
    def cloud_pool_id(self):
        """Gets the cloud_pool_id of this TaskDestinationDown.  # noqa: E501


        :return: The cloud_pool_id of this TaskDestinationDown.  # noqa: E501
        :rtype: int
        """
        return self._cloud_pool_id

    @cloud_pool_id.setter
    def cloud_pool_id(self, cloud_pool_id):
        """Sets the cloud_pool_id of this TaskDestinationDown.


        :param cloud_pool_id: The cloud_pool_id of this TaskDestinationDown.  # noqa: E501
        :type: int
        """

        self._cloud_pool_id = cloud_pool_id

    @property
    def nas_pool_id(self):
        """Gets the nas_pool_id of this TaskDestinationDown.  # noqa: E501


        :return: The nas_pool_id of this TaskDestinationDown.  # noqa: E501
        :rtype: int
        """
        return self._nas_pool_id

    @nas_pool_id.setter
    def nas_pool_id(self, nas_pool_id):
        """Sets the nas_pool_id of this TaskDestinationDown.


        :param nas_pool_id: The nas_pool_id of this TaskDestinationDown.  # noqa: E501
        :type: int
        """

        self._nas_pool_id = nas_pool_id

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
        if issubclass(TaskDestinationDown, dict):
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
        if not isinstance(other, TaskDestinationDown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
