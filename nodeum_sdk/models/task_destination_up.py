# coding: utf-8

"""
    Nodeum API

    # About  This document describes the Nodeum API version 2:  If you are looking for any information about the product itself, reach the product website https://www.nodeum.io. You can also contact us at this email address : info@nodeum.io  # Filter parameters When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from nodeum_sdk.configuration import Configuration


class TaskDestinationUp(object):
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
        'folder_id': 'int',
        'folder_path': 'str',
        'tape_id': 'int',
        'tape_barcode': 'str',
        'pool_id': 'int',
        'pool_name': 'str'
    }

    attribute_map = {
        'folder_id': 'folder_id',
        'folder_path': 'folder_path',
        'tape_id': 'tape_id',
        'tape_barcode': 'tape_barcode',
        'pool_id': 'pool_id',
        'pool_name': 'pool_name'
    }

    def __init__(self, folder_id=None, folder_path=None, tape_id=None, tape_barcode=None, pool_id=None, pool_name=None, local_vars_configuration=None):  # noqa: E501
        """TaskDestinationUp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._folder_id = None
        self._folder_path = None
        self._tape_id = None
        self._tape_barcode = None
        self._pool_id = None
        self._pool_name = None
        self.discriminator = None

        if folder_id is not None:
            self.folder_id = folder_id
        if folder_path is not None:
            self.folder_path = folder_path
        if tape_id is not None:
            self.tape_id = tape_id
        if tape_barcode is not None:
            self.tape_barcode = tape_barcode
        if pool_id is not None:
            self.pool_id = pool_id
        if pool_name is not None:
            self.pool_name = pool_name

    @property
    def folder_id(self):
        """Gets the folder_id of this TaskDestinationUp.  # noqa: E501


        :return: The folder_id of this TaskDestinationUp.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this TaskDestinationUp.


        :param folder_id: The folder_id of this TaskDestinationUp.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def folder_path(self):
        """Gets the folder_path of this TaskDestinationUp.  # noqa: E501


        :return: The folder_path of this TaskDestinationUp.  # noqa: E501
        :rtype: str
        """
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path):
        """Sets the folder_path of this TaskDestinationUp.


        :param folder_path: The folder_path of this TaskDestinationUp.  # noqa: E501
        :type: str
        """

        self._folder_path = folder_path

    @property
    def tape_id(self):
        """Gets the tape_id of this TaskDestinationUp.  # noqa: E501


        :return: The tape_id of this TaskDestinationUp.  # noqa: E501
        :rtype: int
        """
        return self._tape_id

    @tape_id.setter
    def tape_id(self, tape_id):
        """Sets the tape_id of this TaskDestinationUp.


        :param tape_id: The tape_id of this TaskDestinationUp.  # noqa: E501
        :type: int
        """

        self._tape_id = tape_id

    @property
    def tape_barcode(self):
        """Gets the tape_barcode of this TaskDestinationUp.  # noqa: E501


        :return: The tape_barcode of this TaskDestinationUp.  # noqa: E501
        :rtype: str
        """
        return self._tape_barcode

    @tape_barcode.setter
    def tape_barcode(self, tape_barcode):
        """Sets the tape_barcode of this TaskDestinationUp.


        :param tape_barcode: The tape_barcode of this TaskDestinationUp.  # noqa: E501
        :type: str
        """

        self._tape_barcode = tape_barcode

    @property
    def pool_id(self):
        """Gets the pool_id of this TaskDestinationUp.  # noqa: E501


        :return: The pool_id of this TaskDestinationUp.  # noqa: E501
        :rtype: int
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this TaskDestinationUp.


        :param pool_id: The pool_id of this TaskDestinationUp.  # noqa: E501
        :type: int
        """

        self._pool_id = pool_id

    @property
    def pool_name(self):
        """Gets the pool_name of this TaskDestinationUp.  # noqa: E501


        :return: The pool_name of this TaskDestinationUp.  # noqa: E501
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        """Sets the pool_name of this TaskDestinationUp.


        :param pool_name: The pool_name of this TaskDestinationUp.  # noqa: E501
        :type: str
        """

        self._pool_name = pool_name

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
        if not isinstance(other, TaskDestinationUp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskDestinationUp):
            return True

        return self.to_dict() != other.to_dict()