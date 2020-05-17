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


class TaskFacetAllOf(object):
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
        'to_process_size_sum': 'int',
        'processed_size_sum': 'int',
        'to_process_files_sum': 'int',
        'processed_files_sum': 'int',
        'finalized_files_sum': 'int',
        'bandwidth_avg': 'int'
    }

    attribute_map = {
        'to_process_size_sum': 'to_process_size_sum',
        'processed_size_sum': 'processed_size_sum',
        'to_process_files_sum': 'to_process_files_sum',
        'processed_files_sum': 'processed_files_sum',
        'finalized_files_sum': 'finalized_files_sum',
        'bandwidth_avg': 'bandwidth_avg'
    }

    def __init__(self, to_process_size_sum=None, processed_size_sum=None, to_process_files_sum=None, processed_files_sum=None, finalized_files_sum=None, bandwidth_avg=None, local_vars_configuration=None):  # noqa: E501
        """TaskFacetAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._to_process_size_sum = None
        self._processed_size_sum = None
        self._to_process_files_sum = None
        self._processed_files_sum = None
        self._finalized_files_sum = None
        self._bandwidth_avg = None
        self.discriminator = None

        if to_process_size_sum is not None:
            self.to_process_size_sum = to_process_size_sum
        if processed_size_sum is not None:
            self.processed_size_sum = processed_size_sum
        if to_process_files_sum is not None:
            self.to_process_files_sum = to_process_files_sum
        if processed_files_sum is not None:
            self.processed_files_sum = processed_files_sum
        if finalized_files_sum is not None:
            self.finalized_files_sum = finalized_files_sum
        if bandwidth_avg is not None:
            self.bandwidth_avg = bandwidth_avg

    @property
    def to_process_size_sum(self):
        """Gets the to_process_size_sum of this TaskFacetAllOf.  # noqa: E501


        :return: The to_process_size_sum of this TaskFacetAllOf.  # noqa: E501
        :rtype: int
        """
        return self._to_process_size_sum

    @to_process_size_sum.setter
    def to_process_size_sum(self, to_process_size_sum):
        """Sets the to_process_size_sum of this TaskFacetAllOf.


        :param to_process_size_sum: The to_process_size_sum of this TaskFacetAllOf.  # noqa: E501
        :type: int
        """

        self._to_process_size_sum = to_process_size_sum

    @property
    def processed_size_sum(self):
        """Gets the processed_size_sum of this TaskFacetAllOf.  # noqa: E501


        :return: The processed_size_sum of this TaskFacetAllOf.  # noqa: E501
        :rtype: int
        """
        return self._processed_size_sum

    @processed_size_sum.setter
    def processed_size_sum(self, processed_size_sum):
        """Sets the processed_size_sum of this TaskFacetAllOf.


        :param processed_size_sum: The processed_size_sum of this TaskFacetAllOf.  # noqa: E501
        :type: int
        """

        self._processed_size_sum = processed_size_sum

    @property
    def to_process_files_sum(self):
        """Gets the to_process_files_sum of this TaskFacetAllOf.  # noqa: E501


        :return: The to_process_files_sum of this TaskFacetAllOf.  # noqa: E501
        :rtype: int
        """
        return self._to_process_files_sum

    @to_process_files_sum.setter
    def to_process_files_sum(self, to_process_files_sum):
        """Sets the to_process_files_sum of this TaskFacetAllOf.


        :param to_process_files_sum: The to_process_files_sum of this TaskFacetAllOf.  # noqa: E501
        :type: int
        """

        self._to_process_files_sum = to_process_files_sum

    @property
    def processed_files_sum(self):
        """Gets the processed_files_sum of this TaskFacetAllOf.  # noqa: E501


        :return: The processed_files_sum of this TaskFacetAllOf.  # noqa: E501
        :rtype: int
        """
        return self._processed_files_sum

    @processed_files_sum.setter
    def processed_files_sum(self, processed_files_sum):
        """Sets the processed_files_sum of this TaskFacetAllOf.


        :param processed_files_sum: The processed_files_sum of this TaskFacetAllOf.  # noqa: E501
        :type: int
        """

        self._processed_files_sum = processed_files_sum

    @property
    def finalized_files_sum(self):
        """Gets the finalized_files_sum of this TaskFacetAllOf.  # noqa: E501


        :return: The finalized_files_sum of this TaskFacetAllOf.  # noqa: E501
        :rtype: int
        """
        return self._finalized_files_sum

    @finalized_files_sum.setter
    def finalized_files_sum(self, finalized_files_sum):
        """Sets the finalized_files_sum of this TaskFacetAllOf.


        :param finalized_files_sum: The finalized_files_sum of this TaskFacetAllOf.  # noqa: E501
        :type: int
        """

        self._finalized_files_sum = finalized_files_sum

    @property
    def bandwidth_avg(self):
        """Gets the bandwidth_avg of this TaskFacetAllOf.  # noqa: E501


        :return: The bandwidth_avg of this TaskFacetAllOf.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth_avg

    @bandwidth_avg.setter
    def bandwidth_avg(self, bandwidth_avg):
        """Sets the bandwidth_avg of this TaskFacetAllOf.


        :param bandwidth_avg: The bandwidth_avg of this TaskFacetAllOf.  # noqa: E501
        :type: int
        """

        self._bandwidth_avg = bandwidth_avg

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
        if not isinstance(other, TaskFacetAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskFacetAllOf):
            return True

        return self.to_dict() != other.to_dict()