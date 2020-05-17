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


class TypeToSecondaryFacets(object):
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
        'on_secondary_nas': 'BySecondaryTypeFacet',
        'on_secondary_public_cloud': 'BySecondaryTypeFacet',
        'on_secondary_object_cloud': 'BySecondaryTypeFacet',
        'on_secondary_tape': 'BySecondaryTypeFacet',
        'on_any_secondary': 'BySecondaryTypeFacet',
        'on_no_secondary': 'BySecondaryTypeFacet'
    }

    attribute_map = {
        'on_secondary_nas': 'on_secondary_nas',
        'on_secondary_public_cloud': 'on_secondary_public_cloud',
        'on_secondary_object_cloud': 'on_secondary_object_cloud',
        'on_secondary_tape': 'on_secondary_tape',
        'on_any_secondary': 'on_any_secondary',
        'on_no_secondary': 'on_no_secondary'
    }

    def __init__(self, on_secondary_nas=None, on_secondary_public_cloud=None, on_secondary_object_cloud=None, on_secondary_tape=None, on_any_secondary=None, on_no_secondary=None, local_vars_configuration=None):  # noqa: E501
        """TypeToSecondaryFacets - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._on_secondary_nas = None
        self._on_secondary_public_cloud = None
        self._on_secondary_object_cloud = None
        self._on_secondary_tape = None
        self._on_any_secondary = None
        self._on_no_secondary = None
        self.discriminator = None

        if on_secondary_nas is not None:
            self.on_secondary_nas = on_secondary_nas
        if on_secondary_public_cloud is not None:
            self.on_secondary_public_cloud = on_secondary_public_cloud
        if on_secondary_object_cloud is not None:
            self.on_secondary_object_cloud = on_secondary_object_cloud
        if on_secondary_tape is not None:
            self.on_secondary_tape = on_secondary_tape
        if on_any_secondary is not None:
            self.on_any_secondary = on_any_secondary
        if on_no_secondary is not None:
            self.on_no_secondary = on_no_secondary

    @property
    def on_secondary_nas(self):
        """Gets the on_secondary_nas of this TypeToSecondaryFacets.  # noqa: E501


        :return: The on_secondary_nas of this TypeToSecondaryFacets.  # noqa: E501
        :rtype: BySecondaryTypeFacet
        """
        return self._on_secondary_nas

    @on_secondary_nas.setter
    def on_secondary_nas(self, on_secondary_nas):
        """Sets the on_secondary_nas of this TypeToSecondaryFacets.


        :param on_secondary_nas: The on_secondary_nas of this TypeToSecondaryFacets.  # noqa: E501
        :type: BySecondaryTypeFacet
        """

        self._on_secondary_nas = on_secondary_nas

    @property
    def on_secondary_public_cloud(self):
        """Gets the on_secondary_public_cloud of this TypeToSecondaryFacets.  # noqa: E501


        :return: The on_secondary_public_cloud of this TypeToSecondaryFacets.  # noqa: E501
        :rtype: BySecondaryTypeFacet
        """
        return self._on_secondary_public_cloud

    @on_secondary_public_cloud.setter
    def on_secondary_public_cloud(self, on_secondary_public_cloud):
        """Sets the on_secondary_public_cloud of this TypeToSecondaryFacets.


        :param on_secondary_public_cloud: The on_secondary_public_cloud of this TypeToSecondaryFacets.  # noqa: E501
        :type: BySecondaryTypeFacet
        """

        self._on_secondary_public_cloud = on_secondary_public_cloud

    @property
    def on_secondary_object_cloud(self):
        """Gets the on_secondary_object_cloud of this TypeToSecondaryFacets.  # noqa: E501


        :return: The on_secondary_object_cloud of this TypeToSecondaryFacets.  # noqa: E501
        :rtype: BySecondaryTypeFacet
        """
        return self._on_secondary_object_cloud

    @on_secondary_object_cloud.setter
    def on_secondary_object_cloud(self, on_secondary_object_cloud):
        """Sets the on_secondary_object_cloud of this TypeToSecondaryFacets.


        :param on_secondary_object_cloud: The on_secondary_object_cloud of this TypeToSecondaryFacets.  # noqa: E501
        :type: BySecondaryTypeFacet
        """

        self._on_secondary_object_cloud = on_secondary_object_cloud

    @property
    def on_secondary_tape(self):
        """Gets the on_secondary_tape of this TypeToSecondaryFacets.  # noqa: E501


        :return: The on_secondary_tape of this TypeToSecondaryFacets.  # noqa: E501
        :rtype: BySecondaryTypeFacet
        """
        return self._on_secondary_tape

    @on_secondary_tape.setter
    def on_secondary_tape(self, on_secondary_tape):
        """Sets the on_secondary_tape of this TypeToSecondaryFacets.


        :param on_secondary_tape: The on_secondary_tape of this TypeToSecondaryFacets.  # noqa: E501
        :type: BySecondaryTypeFacet
        """

        self._on_secondary_tape = on_secondary_tape

    @property
    def on_any_secondary(self):
        """Gets the on_any_secondary of this TypeToSecondaryFacets.  # noqa: E501


        :return: The on_any_secondary of this TypeToSecondaryFacets.  # noqa: E501
        :rtype: BySecondaryTypeFacet
        """
        return self._on_any_secondary

    @on_any_secondary.setter
    def on_any_secondary(self, on_any_secondary):
        """Sets the on_any_secondary of this TypeToSecondaryFacets.


        :param on_any_secondary: The on_any_secondary of this TypeToSecondaryFacets.  # noqa: E501
        :type: BySecondaryTypeFacet
        """

        self._on_any_secondary = on_any_secondary

    @property
    def on_no_secondary(self):
        """Gets the on_no_secondary of this TypeToSecondaryFacets.  # noqa: E501


        :return: The on_no_secondary of this TypeToSecondaryFacets.  # noqa: E501
        :rtype: BySecondaryTypeFacet
        """
        return self._on_no_secondary

    @on_no_secondary.setter
    def on_no_secondary(self, on_no_secondary):
        """Sets the on_no_secondary of this TypeToSecondaryFacets.


        :param on_no_secondary: The on_no_secondary of this TypeToSecondaryFacets.  # noqa: E501
        :type: BySecondaryTypeFacet
        """

        self._on_no_secondary = on_no_secondary

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
        if not isinstance(other, TypeToSecondaryFacets):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TypeToSecondaryFacets):
            return True

        return self.to_dict() != other.to_dict()
