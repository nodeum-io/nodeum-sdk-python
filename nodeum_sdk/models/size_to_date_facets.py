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


class SizeToDateFacets(object):
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
        'less_100_kb': 'ByDateFacet',
        'less_1_mb': 'ByDateFacet',
        'less_10_mb': 'ByDateFacet',
        'less_100_mb': 'ByDateFacet',
        'less_1_gb': 'ByDateFacet',
        'less_10_gb': 'ByDateFacet',
        'less_100_gb': 'ByDateFacet',
        'more_100_gb': 'ByDateFacet'
    }

    attribute_map = {
        'less_100_kb': 'less_100_kb',
        'less_1_mb': 'less_1_mb',
        'less_10_mb': 'less_10_mb',
        'less_100_mb': 'less_100_mb',
        'less_1_gb': 'less_1_gb',
        'less_10_gb': 'less_10_gb',
        'less_100_gb': 'less_100_gb',
        'more_100_gb': 'more_100_gb'
    }

    def __init__(self, less_100_kb=None, less_1_mb=None, less_10_mb=None, less_100_mb=None, less_1_gb=None, less_10_gb=None, less_100_gb=None, more_100_gb=None, local_vars_configuration=None):  # noqa: E501
        """SizeToDateFacets - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._less_100_kb = None
        self._less_1_mb = None
        self._less_10_mb = None
        self._less_100_mb = None
        self._less_1_gb = None
        self._less_10_gb = None
        self._less_100_gb = None
        self._more_100_gb = None
        self.discriminator = None

        if less_100_kb is not None:
            self.less_100_kb = less_100_kb
        if less_1_mb is not None:
            self.less_1_mb = less_1_mb
        if less_10_mb is not None:
            self.less_10_mb = less_10_mb
        if less_100_mb is not None:
            self.less_100_mb = less_100_mb
        if less_1_gb is not None:
            self.less_1_gb = less_1_gb
        if less_10_gb is not None:
            self.less_10_gb = less_10_gb
        if less_100_gb is not None:
            self.less_100_gb = less_100_gb
        if more_100_gb is not None:
            self.more_100_gb = more_100_gb

    @property
    def less_100_kb(self):
        """Gets the less_100_kb of this SizeToDateFacets.  # noqa: E501


        :return: The less_100_kb of this SizeToDateFacets.  # noqa: E501
        :rtype: ByDateFacet
        """
        return self._less_100_kb

    @less_100_kb.setter
    def less_100_kb(self, less_100_kb):
        """Sets the less_100_kb of this SizeToDateFacets.


        :param less_100_kb: The less_100_kb of this SizeToDateFacets.  # noqa: E501
        :type: ByDateFacet
        """

        self._less_100_kb = less_100_kb

    @property
    def less_1_mb(self):
        """Gets the less_1_mb of this SizeToDateFacets.  # noqa: E501


        :return: The less_1_mb of this SizeToDateFacets.  # noqa: E501
        :rtype: ByDateFacet
        """
        return self._less_1_mb

    @less_1_mb.setter
    def less_1_mb(self, less_1_mb):
        """Sets the less_1_mb of this SizeToDateFacets.


        :param less_1_mb: The less_1_mb of this SizeToDateFacets.  # noqa: E501
        :type: ByDateFacet
        """

        self._less_1_mb = less_1_mb

    @property
    def less_10_mb(self):
        """Gets the less_10_mb of this SizeToDateFacets.  # noqa: E501


        :return: The less_10_mb of this SizeToDateFacets.  # noqa: E501
        :rtype: ByDateFacet
        """
        return self._less_10_mb

    @less_10_mb.setter
    def less_10_mb(self, less_10_mb):
        """Sets the less_10_mb of this SizeToDateFacets.


        :param less_10_mb: The less_10_mb of this SizeToDateFacets.  # noqa: E501
        :type: ByDateFacet
        """

        self._less_10_mb = less_10_mb

    @property
    def less_100_mb(self):
        """Gets the less_100_mb of this SizeToDateFacets.  # noqa: E501


        :return: The less_100_mb of this SizeToDateFacets.  # noqa: E501
        :rtype: ByDateFacet
        """
        return self._less_100_mb

    @less_100_mb.setter
    def less_100_mb(self, less_100_mb):
        """Sets the less_100_mb of this SizeToDateFacets.


        :param less_100_mb: The less_100_mb of this SizeToDateFacets.  # noqa: E501
        :type: ByDateFacet
        """

        self._less_100_mb = less_100_mb

    @property
    def less_1_gb(self):
        """Gets the less_1_gb of this SizeToDateFacets.  # noqa: E501


        :return: The less_1_gb of this SizeToDateFacets.  # noqa: E501
        :rtype: ByDateFacet
        """
        return self._less_1_gb

    @less_1_gb.setter
    def less_1_gb(self, less_1_gb):
        """Sets the less_1_gb of this SizeToDateFacets.


        :param less_1_gb: The less_1_gb of this SizeToDateFacets.  # noqa: E501
        :type: ByDateFacet
        """

        self._less_1_gb = less_1_gb

    @property
    def less_10_gb(self):
        """Gets the less_10_gb of this SizeToDateFacets.  # noqa: E501


        :return: The less_10_gb of this SizeToDateFacets.  # noqa: E501
        :rtype: ByDateFacet
        """
        return self._less_10_gb

    @less_10_gb.setter
    def less_10_gb(self, less_10_gb):
        """Sets the less_10_gb of this SizeToDateFacets.


        :param less_10_gb: The less_10_gb of this SizeToDateFacets.  # noqa: E501
        :type: ByDateFacet
        """

        self._less_10_gb = less_10_gb

    @property
    def less_100_gb(self):
        """Gets the less_100_gb of this SizeToDateFacets.  # noqa: E501


        :return: The less_100_gb of this SizeToDateFacets.  # noqa: E501
        :rtype: ByDateFacet
        """
        return self._less_100_gb

    @less_100_gb.setter
    def less_100_gb(self, less_100_gb):
        """Sets the less_100_gb of this SizeToDateFacets.


        :param less_100_gb: The less_100_gb of this SizeToDateFacets.  # noqa: E501
        :type: ByDateFacet
        """

        self._less_100_gb = less_100_gb

    @property
    def more_100_gb(self):
        """Gets the more_100_gb of this SizeToDateFacets.  # noqa: E501


        :return: The more_100_gb of this SizeToDateFacets.  # noqa: E501
        :rtype: ByDateFacet
        """
        return self._more_100_gb

    @more_100_gb.setter
    def more_100_gb(self, more_100_gb):
        """Sets the more_100_gb of this SizeToDateFacets.


        :param more_100_gb: The more_100_gb of this SizeToDateFacets.  # noqa: E501
        :type: ByDateFacet
        """

        self._more_100_gb = more_100_gb

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
        if not isinstance(other, SizeToDateFacets):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SizeToDateFacets):
            return True

        return self.to_dict() != other.to_dict()
