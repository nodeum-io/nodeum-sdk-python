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


class ActiveJobStatus(object):
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
        'job_id': 'str',
        'status': 'str',
        'progress': 'int',
        'total': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'progress': 'progress',
        'total': 'total'
    }

    def __init__(self, job_id=None, status=None, progress=None, total=None, local_vars_configuration=None):  # noqa: E501
        """ActiveJobStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._job_id = None
        self._status = None
        self._progress = None
        self._total = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if total is not None:
            self.total = total

    @property
    def job_id(self):
        """Gets the job_id of this ActiveJobStatus.  # noqa: E501


        :return: The job_id of this ActiveJobStatus.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ActiveJobStatus.


        :param job_id: The job_id of this ActiveJobStatus.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this ActiveJobStatus.  # noqa: E501


        :return: The status of this ActiveJobStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ActiveJobStatus.


        :param status: The status of this ActiveJobStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["queued", "working", "completed", "failed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def progress(self):
        """Gets the progress of this ActiveJobStatus.  # noqa: E501


        :return: The progress of this ActiveJobStatus.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ActiveJobStatus.


        :param progress: The progress of this ActiveJobStatus.  # noqa: E501
        :type: int
        """

        self._progress = progress

    @property
    def total(self):
        """Gets the total of this ActiveJobStatus.  # noqa: E501


        :return: The total of this ActiveJobStatus.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ActiveJobStatus.


        :param total: The total of this ActiveJobStatus.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, ActiveJobStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActiveJobStatus):
            return True

        return self.to_dict() != other.to_dict()
