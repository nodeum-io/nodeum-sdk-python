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

from swagger_client.models.tape_drive import TapeDrive  # noqa: F401,E501


class TapeDriveCollection(object):
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
        'count': 'int',
        'tape_drives': 'list[TapeDrive]'
    }

    attribute_map = {
        'count': 'count',
        'tape_drives': 'tape_drives'
    }

    def __init__(self, count=None, tape_drives=None):  # noqa: E501
        """TapeDriveCollection - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._tape_drives = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if tape_drives is not None:
            self.tape_drives = tape_drives

    @property
    def count(self):
        """Gets the count of this TapeDriveCollection.  # noqa: E501


        :return: The count of this TapeDriveCollection.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TapeDriveCollection.


        :param count: The count of this TapeDriveCollection.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def tape_drives(self):
        """Gets the tape_drives of this TapeDriveCollection.  # noqa: E501


        :return: The tape_drives of this TapeDriveCollection.  # noqa: E501
        :rtype: list[TapeDrive]
        """
        return self._tape_drives

    @tape_drives.setter
    def tape_drives(self, tape_drives):
        """Sets the tape_drives of this TapeDriveCollection.


        :param tape_drives: The tape_drives of this TapeDriveCollection.  # noqa: E501
        :type: list[TapeDrive]
        """

        self._tape_drives = tape_drives

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
        if issubclass(TapeDriveCollection, dict):
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
        if not isinstance(other, TapeDriveCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
