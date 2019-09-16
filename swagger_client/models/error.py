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

from swagger_client.models.attribute_error import AttributeError  # noqa: F401,E501


class Error(object):
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
        'details': 'dict(str, list[AttributeError])',
        'messages': 'list[str]'
    }

    attribute_map = {
        'details': 'details',
        'messages': 'messages'
    }

    def __init__(self, details=None, messages=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501

        self._details = None
        self._messages = None
        self.discriminator = None

        if details is not None:
            self.details = details
        if messages is not None:
            self.messages = messages

    @property
    def details(self):
        """Gets the details of this Error.  # noqa: E501

        Parsable objects describing the errors. The key is the invalid attribute name.  # noqa: E501

        :return: The details of this Error.  # noqa: E501
        :rtype: dict(str, list[AttributeError])
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Error.

        Parsable objects describing the errors. The key is the invalid attribute name.  # noqa: E501

        :param details: The details of this Error.  # noqa: E501
        :type: dict(str, list[AttributeError])
        """

        self._details = details

    @property
    def messages(self):
        """Gets the messages of this Error.  # noqa: E501

        English description of the errors.  # noqa: E501

        :return: The messages of this Error.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this Error.

        English description of the errors.  # noqa: E501

        :param messages: The messages of this Error.  # noqa: E501
        :type: list[str]
        """

        self._messages = messages

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
        if issubclass(Error, dict):
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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
