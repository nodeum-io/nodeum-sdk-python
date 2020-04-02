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


class TaskExecution(object):
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
        'id': 'str',
        'task_id': 'int',
        'name': 'str',
        'workflow_type': 'str',
        'workflow_action': 'str',
        'source_type': 'str',
        'destination_type': 'str',
        'status': 'str',
        'log_time': 'str',
        'job_started': 'str',
        'job_finished': 'str',
        'to_process_size': 'int',
        'processed_size': 'int',
        'to_process_files': 'int',
        'processed_files': 'int',
        'finalized_files': 'int',
        'estimation_time': 'int',
        'bandwidth': 'int'
    }

    attribute_map = {
        'id': 'id',
        'task_id': 'task_id',
        'name': 'name',
        'workflow_type': 'workflow_type',
        'workflow_action': 'workflow_action',
        'source_type': 'source_type',
        'destination_type': 'destination_type',
        'status': 'status',
        'log_time': 'log_time',
        'job_started': 'job_started',
        'job_finished': 'job_finished',
        'to_process_size': 'to_process_size',
        'processed_size': 'processed_size',
        'to_process_files': 'to_process_files',
        'processed_files': 'processed_files',
        'finalized_files': 'finalized_files',
        'estimation_time': 'estimation_time',
        'bandwidth': 'bandwidth'
    }

    def __init__(self, id=None, task_id=None, name=None, workflow_type=None, workflow_action=None, source_type=None, destination_type=None, status=None, log_time=None, job_started=None, job_finished=None, to_process_size=None, processed_size=None, to_process_files=None, processed_files=None, finalized_files=None, estimation_time=None, bandwidth=None, local_vars_configuration=None):  # noqa: E501
        """TaskExecution - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._task_id = None
        self._name = None
        self._workflow_type = None
        self._workflow_action = None
        self._source_type = None
        self._destination_type = None
        self._status = None
        self._log_time = None
        self._job_started = None
        self._job_finished = None
        self._to_process_size = None
        self._processed_size = None
        self._to_process_files = None
        self._processed_files = None
        self._finalized_files = None
        self._estimation_time = None
        self._bandwidth = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_id is not None:
            self.task_id = task_id
        if name is not None:
            self.name = name
        if workflow_type is not None:
            self.workflow_type = workflow_type
        if workflow_action is not None:
            self.workflow_action = workflow_action
        if source_type is not None:
            self.source_type = source_type
        if destination_type is not None:
            self.destination_type = destination_type
        if status is not None:
            self.status = status
        if log_time is not None:
            self.log_time = log_time
        if job_started is not None:
            self.job_started = job_started
        if job_finished is not None:
            self.job_finished = job_finished
        if to_process_size is not None:
            self.to_process_size = to_process_size
        if processed_size is not None:
            self.processed_size = processed_size
        if to_process_files is not None:
            self.to_process_files = to_process_files
        if processed_files is not None:
            self.processed_files = processed_files
        if finalized_files is not None:
            self.finalized_files = finalized_files
        if estimation_time is not None:
            self.estimation_time = estimation_time
        if bandwidth is not None:
            self.bandwidth = bandwidth

    @property
    def id(self):
        """Gets the id of this TaskExecution.  # noqa: E501


        :return: The id of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskExecution.


        :param id: The id of this TaskExecution.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def task_id(self):
        """Gets the task_id of this TaskExecution.  # noqa: E501


        :return: The task_id of this TaskExecution.  # noqa: E501
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskExecution.


        :param task_id: The task_id of this TaskExecution.  # noqa: E501
        :type: int
        """

        self._task_id = task_id

    @property
    def name(self):
        """Gets the name of this TaskExecution.  # noqa: E501


        :return: The name of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskExecution.


        :param name: The name of this TaskExecution.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def workflow_type(self):
        """Gets the workflow_type of this TaskExecution.  # noqa: E501


        :return: The workflow_type of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._workflow_type

    @workflow_type.setter
    def workflow_type(self, workflow_type):
        """Sets the workflow_type of this TaskExecution.


        :param workflow_type: The workflow_type of this TaskExecution.  # noqa: E501
        :type: str
        """
        allowed_values = ["active_archive", "offline_archive", "data_exchange", "maintenance", "data_enrichment"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and workflow_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `workflow_type` ({0}), must be one of {1}"  # noqa: E501
                .format(workflow_type, allowed_values)
            )

        self._workflow_type = workflow_type

    @property
    def workflow_action(self):
        """Gets the workflow_action of this TaskExecution.  # noqa: E501


        :return: The workflow_action of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._workflow_action

    @workflow_action.setter
    def workflow_action(self, workflow_action):
        """Sets the workflow_action of this TaskExecution.


        :param workflow_action: The workflow_action of this TaskExecution.  # noqa: E501
        :type: str
        """
        allowed_values = ["copy", "move", "scan", "rehydratation", "format", "check_consistency", "duplication", "cache_cleaning", "ejection", "get_index", "full_backup", "incremental_backup"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and workflow_action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `workflow_action` ({0}), must be one of {1}"  # noqa: E501
                .format(workflow_action, allowed_values)
            )

        self._workflow_action = workflow_action

    @property
    def source_type(self):
        """Gets the source_type of this TaskExecution.  # noqa: E501


        :return: The source_type of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this TaskExecution.


        :param source_type: The source_type of this TaskExecution.  # noqa: E501
        :type: str
        """
        allowed_values = ["container", "primary_nas", "secondary_nas", "primary_cloud", "secondary_cloud", "secondary_tape"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and source_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def destination_type(self):
        """Gets the destination_type of this TaskExecution.  # noqa: E501


        :return: The destination_type of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this TaskExecution.


        :param destination_type: The destination_type of this TaskExecution.  # noqa: E501
        :type: str
        """
        allowed_values = ["container", "primary_nas", "secondary_nas", "primary_cloud", "secondary_cloud", "secondary_tape"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and destination_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `destination_type` ({0}), must be one of {1}"  # noqa: E501
                .format(destination_type, allowed_values)
            )

        self._destination_type = destination_type

    @property
    def status(self):
        """Gets the status of this TaskExecution.  # noqa: E501


        :return: The status of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskExecution.


        :param status: The status of this TaskExecution.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_activated", "done", "in_progress", "error", "paused", "stopped_by_system", "in_queue", "finished_with_warnings", "calculating", "stopped_by_user"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def log_time(self):
        """Gets the log_time of this TaskExecution.  # noqa: E501


        :return: The log_time of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._log_time

    @log_time.setter
    def log_time(self, log_time):
        """Sets the log_time of this TaskExecution.


        :param log_time: The log_time of this TaskExecution.  # noqa: E501
        :type: str
        """

        self._log_time = log_time

    @property
    def job_started(self):
        """Gets the job_started of this TaskExecution.  # noqa: E501


        :return: The job_started of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._job_started

    @job_started.setter
    def job_started(self, job_started):
        """Sets the job_started of this TaskExecution.


        :param job_started: The job_started of this TaskExecution.  # noqa: E501
        :type: str
        """

        self._job_started = job_started

    @property
    def job_finished(self):
        """Gets the job_finished of this TaskExecution.  # noqa: E501


        :return: The job_finished of this TaskExecution.  # noqa: E501
        :rtype: str
        """
        return self._job_finished

    @job_finished.setter
    def job_finished(self, job_finished):
        """Sets the job_finished of this TaskExecution.


        :param job_finished: The job_finished of this TaskExecution.  # noqa: E501
        :type: str
        """

        self._job_finished = job_finished

    @property
    def to_process_size(self):
        """Gets the to_process_size of this TaskExecution.  # noqa: E501


        :return: The to_process_size of this TaskExecution.  # noqa: E501
        :rtype: int
        """
        return self._to_process_size

    @to_process_size.setter
    def to_process_size(self, to_process_size):
        """Sets the to_process_size of this TaskExecution.


        :param to_process_size: The to_process_size of this TaskExecution.  # noqa: E501
        :type: int
        """

        self._to_process_size = to_process_size

    @property
    def processed_size(self):
        """Gets the processed_size of this TaskExecution.  # noqa: E501


        :return: The processed_size of this TaskExecution.  # noqa: E501
        :rtype: int
        """
        return self._processed_size

    @processed_size.setter
    def processed_size(self, processed_size):
        """Sets the processed_size of this TaskExecution.


        :param processed_size: The processed_size of this TaskExecution.  # noqa: E501
        :type: int
        """

        self._processed_size = processed_size

    @property
    def to_process_files(self):
        """Gets the to_process_files of this TaskExecution.  # noqa: E501


        :return: The to_process_files of this TaskExecution.  # noqa: E501
        :rtype: int
        """
        return self._to_process_files

    @to_process_files.setter
    def to_process_files(self, to_process_files):
        """Sets the to_process_files of this TaskExecution.


        :param to_process_files: The to_process_files of this TaskExecution.  # noqa: E501
        :type: int
        """

        self._to_process_files = to_process_files

    @property
    def processed_files(self):
        """Gets the processed_files of this TaskExecution.  # noqa: E501


        :return: The processed_files of this TaskExecution.  # noqa: E501
        :rtype: int
        """
        return self._processed_files

    @processed_files.setter
    def processed_files(self, processed_files):
        """Sets the processed_files of this TaskExecution.


        :param processed_files: The processed_files of this TaskExecution.  # noqa: E501
        :type: int
        """

        self._processed_files = processed_files

    @property
    def finalized_files(self):
        """Gets the finalized_files of this TaskExecution.  # noqa: E501


        :return: The finalized_files of this TaskExecution.  # noqa: E501
        :rtype: int
        """
        return self._finalized_files

    @finalized_files.setter
    def finalized_files(self, finalized_files):
        """Sets the finalized_files of this TaskExecution.


        :param finalized_files: The finalized_files of this TaskExecution.  # noqa: E501
        :type: int
        """

        self._finalized_files = finalized_files

    @property
    def estimation_time(self):
        """Gets the estimation_time of this TaskExecution.  # noqa: E501


        :return: The estimation_time of this TaskExecution.  # noqa: E501
        :rtype: int
        """
        return self._estimation_time

    @estimation_time.setter
    def estimation_time(self, estimation_time):
        """Sets the estimation_time of this TaskExecution.


        :param estimation_time: The estimation_time of this TaskExecution.  # noqa: E501
        :type: int
        """

        self._estimation_time = estimation_time

    @property
    def bandwidth(self):
        """Gets the bandwidth of this TaskExecution.  # noqa: E501


        :return: The bandwidth of this TaskExecution.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this TaskExecution.


        :param bandwidth: The bandwidth of this TaskExecution.  # noqa: E501
        :type: int
        """

        self._bandwidth = bandwidth

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
        if not isinstance(other, TaskExecution):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskExecution):
            return True

        return self.to_dict() != other.to_dict()