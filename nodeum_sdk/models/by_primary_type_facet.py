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


class ByPrimaryTypeFacet(object):
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
        'files_count': 'int',
        'file_size_sum': 'int',
        'cost': 'float',
        'in_cache': 'FileFacet',
        'less_1_week': 'FileFacet',
        'less_1_month': 'FileFacet',
        'less_3_months': 'FileFacet',
        'less_6_months': 'FileFacet',
        'less_1_year': 'FileFacet',
        'less_2_years': 'FileFacet',
        'more_2_years': 'FileFacet',
        'prim_name_s': 'ByDateFacetBuckets'
    }

    attribute_map = {
        'count': 'count',
        'files_count': 'files_count',
        'file_size_sum': 'file_size_sum',
        'cost': 'cost',
        'in_cache': 'in_cache',
        'less_1_week': 'less_1_week',
        'less_1_month': 'less_1_month',
        'less_3_months': 'less_3_months',
        'less_6_months': 'less_6_months',
        'less_1_year': 'less_1_year',
        'less_2_years': 'less_2_years',
        'more_2_years': 'more_2_years',
        'prim_name_s': 'prim_name_s'
    }

    def __init__(self, count=None, files_count=None, file_size_sum=None, cost=None, in_cache=None, less_1_week=None, less_1_month=None, less_3_months=None, less_6_months=None, less_1_year=None, less_2_years=None, more_2_years=None, prim_name_s=None, local_vars_configuration=None):  # noqa: E501
        """ByPrimaryTypeFacet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._count = None
        self._files_count = None
        self._file_size_sum = None
        self._cost = None
        self._in_cache = None
        self._less_1_week = None
        self._less_1_month = None
        self._less_3_months = None
        self._less_6_months = None
        self._less_1_year = None
        self._less_2_years = None
        self._more_2_years = None
        self._prim_name_s = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if files_count is not None:
            self.files_count = files_count
        if file_size_sum is not None:
            self.file_size_sum = file_size_sum
        if cost is not None:
            self.cost = cost
        if in_cache is not None:
            self.in_cache = in_cache
        if less_1_week is not None:
            self.less_1_week = less_1_week
        if less_1_month is not None:
            self.less_1_month = less_1_month
        if less_3_months is not None:
            self.less_3_months = less_3_months
        if less_6_months is not None:
            self.less_6_months = less_6_months
        if less_1_year is not None:
            self.less_1_year = less_1_year
        if less_2_years is not None:
            self.less_2_years = less_2_years
        if more_2_years is not None:
            self.more_2_years = more_2_years
        if prim_name_s is not None:
            self.prim_name_s = prim_name_s

    @property
    def count(self):
        """Gets the count of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The count of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ByPrimaryTypeFacet.


        :param count: The count of this ByPrimaryTypeFacet.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def files_count(self):
        """Gets the files_count of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The files_count of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: int
        """
        return self._files_count

    @files_count.setter
    def files_count(self, files_count):
        """Sets the files_count of this ByPrimaryTypeFacet.


        :param files_count: The files_count of this ByPrimaryTypeFacet.  # noqa: E501
        :type: int
        """

        self._files_count = files_count

    @property
    def file_size_sum(self):
        """Gets the file_size_sum of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The file_size_sum of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: int
        """
        return self._file_size_sum

    @file_size_sum.setter
    def file_size_sum(self, file_size_sum):
        """Sets the file_size_sum of this ByPrimaryTypeFacet.


        :param file_size_sum: The file_size_sum of this ByPrimaryTypeFacet.  # noqa: E501
        :type: int
        """

        self._file_size_sum = file_size_sum

    @property
    def cost(self):
        """Gets the cost of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The cost of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: float
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this ByPrimaryTypeFacet.


        :param cost: The cost of this ByPrimaryTypeFacet.  # noqa: E501
        :type: float
        """

        self._cost = cost

    @property
    def in_cache(self):
        """Gets the in_cache of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The in_cache of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: FileFacet
        """
        return self._in_cache

    @in_cache.setter
    def in_cache(self, in_cache):
        """Sets the in_cache of this ByPrimaryTypeFacet.


        :param in_cache: The in_cache of this ByPrimaryTypeFacet.  # noqa: E501
        :type: FileFacet
        """

        self._in_cache = in_cache

    @property
    def less_1_week(self):
        """Gets the less_1_week of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The less_1_week of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: FileFacet
        """
        return self._less_1_week

    @less_1_week.setter
    def less_1_week(self, less_1_week):
        """Sets the less_1_week of this ByPrimaryTypeFacet.


        :param less_1_week: The less_1_week of this ByPrimaryTypeFacet.  # noqa: E501
        :type: FileFacet
        """

        self._less_1_week = less_1_week

    @property
    def less_1_month(self):
        """Gets the less_1_month of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The less_1_month of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: FileFacet
        """
        return self._less_1_month

    @less_1_month.setter
    def less_1_month(self, less_1_month):
        """Sets the less_1_month of this ByPrimaryTypeFacet.


        :param less_1_month: The less_1_month of this ByPrimaryTypeFacet.  # noqa: E501
        :type: FileFacet
        """

        self._less_1_month = less_1_month

    @property
    def less_3_months(self):
        """Gets the less_3_months of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The less_3_months of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: FileFacet
        """
        return self._less_3_months

    @less_3_months.setter
    def less_3_months(self, less_3_months):
        """Sets the less_3_months of this ByPrimaryTypeFacet.


        :param less_3_months: The less_3_months of this ByPrimaryTypeFacet.  # noqa: E501
        :type: FileFacet
        """

        self._less_3_months = less_3_months

    @property
    def less_6_months(self):
        """Gets the less_6_months of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The less_6_months of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: FileFacet
        """
        return self._less_6_months

    @less_6_months.setter
    def less_6_months(self, less_6_months):
        """Sets the less_6_months of this ByPrimaryTypeFacet.


        :param less_6_months: The less_6_months of this ByPrimaryTypeFacet.  # noqa: E501
        :type: FileFacet
        """

        self._less_6_months = less_6_months

    @property
    def less_1_year(self):
        """Gets the less_1_year of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The less_1_year of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: FileFacet
        """
        return self._less_1_year

    @less_1_year.setter
    def less_1_year(self, less_1_year):
        """Sets the less_1_year of this ByPrimaryTypeFacet.


        :param less_1_year: The less_1_year of this ByPrimaryTypeFacet.  # noqa: E501
        :type: FileFacet
        """

        self._less_1_year = less_1_year

    @property
    def less_2_years(self):
        """Gets the less_2_years of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The less_2_years of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: FileFacet
        """
        return self._less_2_years

    @less_2_years.setter
    def less_2_years(self, less_2_years):
        """Sets the less_2_years of this ByPrimaryTypeFacet.


        :param less_2_years: The less_2_years of this ByPrimaryTypeFacet.  # noqa: E501
        :type: FileFacet
        """

        self._less_2_years = less_2_years

    @property
    def more_2_years(self):
        """Gets the more_2_years of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The more_2_years of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: FileFacet
        """
        return self._more_2_years

    @more_2_years.setter
    def more_2_years(self, more_2_years):
        """Sets the more_2_years of this ByPrimaryTypeFacet.


        :param more_2_years: The more_2_years of this ByPrimaryTypeFacet.  # noqa: E501
        :type: FileFacet
        """

        self._more_2_years = more_2_years

    @property
    def prim_name_s(self):
        """Gets the prim_name_s of this ByPrimaryTypeFacet.  # noqa: E501


        :return: The prim_name_s of this ByPrimaryTypeFacet.  # noqa: E501
        :rtype: ByDateFacetBuckets
        """
        return self._prim_name_s

    @prim_name_s.setter
    def prim_name_s(self, prim_name_s):
        """Sets the prim_name_s of this ByPrimaryTypeFacet.


        :param prim_name_s: The prim_name_s of this ByPrimaryTypeFacet.  # noqa: E501
        :type: ByDateFacetBuckets
        """

        self._prim_name_s = prim_name_s

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
        if not isinstance(other, ByPrimaryTypeFacet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ByPrimaryTypeFacet):
            return True

        return self.to_dict() != other.to_dict()