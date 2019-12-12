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


class NodeumFileCollection(object):
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
        'count': 'int',
        'files': 'list[NodeumFile]'
    }

    attribute_map = {
        'count': 'count',
        'files': 'files'
    }

    def __init__(self, count=None, files=None, local_vars_configuration=None):  # noqa: E501
        """NodeumFileCollection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._files = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if files is not None:
            self.files = files

    @property
    def count(self):
        """Gets the count of this NodeumFileCollection.  # noqa: E501


        :return: The count of this NodeumFileCollection.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this NodeumFileCollection.


        :param count: The count of this NodeumFileCollection.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def files(self):
        """Gets the files of this NodeumFileCollection.  # noqa: E501


        :return: The files of this NodeumFileCollection.  # noqa: E501
        :rtype: list[NodeumFile]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this NodeumFileCollection.


        :param files: The files of this NodeumFileCollection.  # noqa: E501
        :type: list[NodeumFile]
        """

        self._files = files

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
        if not isinstance(other, NodeumFileCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NodeumFileCollection):
            return True

        return self.to_dict() != other.to_dict()
