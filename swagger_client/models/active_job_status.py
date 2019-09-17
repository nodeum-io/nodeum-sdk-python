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


class ActiveJobStatus(object):
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

    def __init__(self, job_id=None, status=None, progress=None, total=None):  # noqa: E501
        """ActiveJobStatus - a model defined in Swagger"""  # noqa: E501

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
        if status not in allowed_values:
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
        if issubclass(ActiveJobStatus, dict):
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
        if not isinstance(other, ActiveJobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other