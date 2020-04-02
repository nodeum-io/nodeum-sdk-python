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


class CloudBucket(object):
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
        'cloud_connector_id': 'int',
        'pool_id': 'int',
        'name': 'str',
        'files_count': 'int',
        'files_size': 'int',
        'location': 'str',
        'price': 'str'
    }

    attribute_map = {
        'id': 'id',
        'cloud_connector_id': 'cloud_connector_id',
        'pool_id': 'pool_id',
        'name': 'name',
        'files_count': 'files_count',
        'files_size': 'files_size',
        'location': 'location',
        'price': 'price'
    }

    def __init__(self, id=None, cloud_connector_id=None, pool_id=None, name=None, files_count=None, files_size=None, location=None, price=None, local_vars_configuration=None):  # noqa: E501
        """CloudBucket - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._cloud_connector_id = None
        self._pool_id = None
        self._name = None
        self._files_count = None
        self._files_size = None
        self._location = None
        self._price = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cloud_connector_id is not None:
            self.cloud_connector_id = cloud_connector_id
        if pool_id is not None:
            self.pool_id = pool_id
        if name is not None:
            self.name = name
        if files_count is not None:
            self.files_count = files_count
        if files_size is not None:
            self.files_size = files_size
        if location is not None:
            self.location = location
        if price is not None:
            self.price = price

    @property
    def id(self):
        """Gets the id of this CloudBucket.  # noqa: E501


        :return: The id of this CloudBucket.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudBucket.


        :param id: The id of this CloudBucket.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def cloud_connector_id(self):
        """Gets the cloud_connector_id of this CloudBucket.  # noqa: E501


        :return: The cloud_connector_id of this CloudBucket.  # noqa: E501
        :rtype: int
        """
        return self._cloud_connector_id

    @cloud_connector_id.setter
    def cloud_connector_id(self, cloud_connector_id):
        """Sets the cloud_connector_id of this CloudBucket.


        :param cloud_connector_id: The cloud_connector_id of this CloudBucket.  # noqa: E501
        :type: int
        """

        self._cloud_connector_id = cloud_connector_id

    @property
    def pool_id(self):
        """Gets the pool_id of this CloudBucket.  # noqa: E501


        :return: The pool_id of this CloudBucket.  # noqa: E501
        :rtype: int
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this CloudBucket.


        :param pool_id: The pool_id of this CloudBucket.  # noqa: E501
        :type: int
        """

        self._pool_id = pool_id

    @property
    def name(self):
        """Gets the name of this CloudBucket.  # noqa: E501


        :return: The name of this CloudBucket.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudBucket.


        :param name: The name of this CloudBucket.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def files_count(self):
        """Gets the files_count of this CloudBucket.  # noqa: E501


        :return: The files_count of this CloudBucket.  # noqa: E501
        :rtype: int
        """
        return self._files_count

    @files_count.setter
    def files_count(self, files_count):
        """Sets the files_count of this CloudBucket.


        :param files_count: The files_count of this CloudBucket.  # noqa: E501
        :type: int
        """

        self._files_count = files_count

    @property
    def files_size(self):
        """Gets the files_size of this CloudBucket.  # noqa: E501


        :return: The files_size of this CloudBucket.  # noqa: E501
        :rtype: int
        """
        return self._files_size

    @files_size.setter
    def files_size(self, files_size):
        """Sets the files_size of this CloudBucket.


        :param files_size: The files_size of this CloudBucket.  # noqa: E501
        :type: int
        """

        self._files_size = files_size

    @property
    def location(self):
        """Gets the location of this CloudBucket.  # noqa: E501


        :return: The location of this CloudBucket.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CloudBucket.


        :param location: The location of this CloudBucket.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def price(self):
        """Gets the price of this CloudBucket.  # noqa: E501


        :return: The price of this CloudBucket.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CloudBucket.


        :param price: The price of this CloudBucket.  # noqa: E501
        :type: str
        """

        self._price = price

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
        if not isinstance(other, CloudBucket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudBucket):
            return True

        return self.to_dict() != other.to_dict()