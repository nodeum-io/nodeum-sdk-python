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


class Task(object):
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
        'id': 'int',
        'name': 'str',
        'comment': 'str',
        'type': 'str',
        'workflow_type': 'str',
        'workflow_action': 'str',
        'priority': 'int',
        'conflict_resolution': 'str',
        'action': 'str',
        'activate': 'bool',
        'creation_date': 'str',
        'modification_date': 'str',
        'creation_username': 'str',
        'modification_username': 'str',
        'status': 'str',
        'job_started': 'str',
        'job_finished': 'str',
        'processed_size': 'int',
        'to_process_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'comment': 'comment',
        'type': 'type',
        'workflow_type': 'workflow_type',
        'workflow_action': 'workflow_action',
        'priority': 'priority',
        'conflict_resolution': 'conflict_resolution',
        'action': 'action',
        'activate': 'activate',
        'creation_date': 'creation_date',
        'modification_date': 'modification_date',
        'creation_username': 'creation_username',
        'modification_username': 'modification_username',
        'status': 'status',
        'job_started': 'job_started',
        'job_finished': 'job_finished',
        'processed_size': 'processed_size',
        'to_process_size': 'to_process_size'
    }

    def __init__(self, id=None, name=None, comment=None, type=None, workflow_type=None, workflow_action=None, priority=None, conflict_resolution=None, action=None, activate=None, creation_date=None, modification_date=None, creation_username=None, modification_username=None, status=None, job_started=None, job_finished=None, processed_size=None, to_process_size=None):  # noqa: E501
        """Task - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._comment = None
        self._type = None
        self._workflow_type = None
        self._workflow_action = None
        self._priority = None
        self._conflict_resolution = None
        self._action = None
        self._activate = None
        self._creation_date = None
        self._modification_date = None
        self._creation_username = None
        self._modification_username = None
        self._status = None
        self._job_started = None
        self._job_finished = None
        self._processed_size = None
        self._to_process_size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if comment is not None:
            self.comment = comment
        if type is not None:
            self.type = type
        if workflow_type is not None:
            self.workflow_type = workflow_type
        if workflow_action is not None:
            self.workflow_action = workflow_action
        if priority is not None:
            self.priority = priority
        if conflict_resolution is not None:
            self.conflict_resolution = conflict_resolution
        if action is not None:
            self.action = action
        if activate is not None:
            self.activate = activate
        if creation_date is not None:
            self.creation_date = creation_date
        if modification_date is not None:
            self.modification_date = modification_date
        if creation_username is not None:
            self.creation_username = creation_username
        if modification_username is not None:
            self.modification_username = modification_username
        if status is not None:
            self.status = status
        if job_started is not None:
            self.job_started = job_started
        if job_finished is not None:
            self.job_finished = job_finished
        if processed_size is not None:
            self.processed_size = processed_size
        if to_process_size is not None:
            self.to_process_size = to_process_size

    @property
    def id(self):
        """Gets the id of this Task.  # noqa: E501


        :return: The id of this Task.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.


        :param id: The id of this Task.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Task.  # noqa: E501


        :return: The name of this Task.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Task.


        :param name: The name of this Task.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this Task.  # noqa: E501


        :return: The comment of this Task.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this Task.


        :param comment: The comment of this Task.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def type(self):
        """Gets the type of this Task.  # noqa: E501


        :return: The type of this Task.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Task.


        :param type: The type of this Task.  # noqa: E501
        :type: str
        """
        allowed_values = ["export_active_archive_copy", "import_active_archive_copy", "ext_to_cache", "cache_to_primary", "to_cloud_active_archive_copy", "from_cloud_active_archive_copy", "to_nas_active_archive_copy", "from_nas_active_archive_copy", "export_active_archive_move", "from_cloud_active_archive_move", "from_nas_active_archive_move", "to_cloud_active_archive_move", "from_cloud_to_cloud_active_archive_move", "from_cloud_to_nas_active_archive_move", "to_nas_active_archive_move", "from_nas_to_nas_active_archive_move", "from_nas_to_cloud_active_archive_move", "ext_to_cache_move", "export_offline_archiving_copy", "import_offline_archiving_copy", "to_cloud_offline_copy", "from_cloud_offline_copy", "to_nas_offline_copy", "from_nas_offline_copy", "from_cloud_to_cloud_offline_archive_copy", "from_nas_to_nas_offline_archive_copy", "reload_copy", "export_offline_archiving_move", "to_cloud_offline_move", "to_nas_offline_move", "offline_scan_media", "from_nas_to_nas_offline_archive_move", "from_nas_offline_archive_move", "from_cloud_to_cloud_offline_archive_move", "from_cloud_offline_archive_move", "reload_move", "export_data_exchange_copy", "import_data_exchange_copy", "export_data_exchange_move", "import_scan_media", "rehydratation", "format", "check_consistency", "migration_new_ltfs_to_new_ltfs", "full_backup", "incremental_backup", "data_enrichment_google_vision", "data_enrichment_depthen"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def workflow_type(self):
        """Gets the workflow_type of this Task.  # noqa: E501


        :return: The workflow_type of this Task.  # noqa: E501
        :rtype: str
        """
        return self._workflow_type

    @workflow_type.setter
    def workflow_type(self, workflow_type):
        """Sets the workflow_type of this Task.


        :param workflow_type: The workflow_type of this Task.  # noqa: E501
        :type: str
        """
        allowed_values = ["active_archive", "offline_archive", "data_exchange", "maintenance", "data_enrichment"]  # noqa: E501
        if workflow_type not in allowed_values:
            raise ValueError(
                "Invalid value for `workflow_type` ({0}), must be one of {1}"  # noqa: E501
                .format(workflow_type, allowed_values)
            )

        self._workflow_type = workflow_type

    @property
    def workflow_action(self):
        """Gets the workflow_action of this Task.  # noqa: E501


        :return: The workflow_action of this Task.  # noqa: E501
        :rtype: str
        """
        return self._workflow_action

    @workflow_action.setter
    def workflow_action(self, workflow_action):
        """Sets the workflow_action of this Task.


        :param workflow_action: The workflow_action of this Task.  # noqa: E501
        :type: str
        """
        allowed_values = ["copy", "move", "scan", "rehydratation", "format", "check_consistency", "duplication"]  # noqa: E501
        if workflow_action not in allowed_values:
            raise ValueError(
                "Invalid value for `workflow_action` ({0}), must be one of {1}"  # noqa: E501
                .format(workflow_action, allowed_values)
            )

        self._workflow_action = workflow_action

    @property
    def priority(self):
        """Gets the priority of this Task.  # noqa: E501


        :return: The priority of this Task.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Task.


        :param priority: The priority of this Task.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def conflict_resolution(self):
        """Gets the conflict_resolution of this Task.  # noqa: E501


        :return: The conflict_resolution of this Task.  # noqa: E501
        :rtype: str
        """
        return self._conflict_resolution

    @conflict_resolution.setter
    def conflict_resolution(self, conflict_resolution):
        """Sets the conflict_resolution of this Task.


        :param conflict_resolution: The conflict_resolution of this Task.  # noqa: E501
        :type: str
        """
        allowed_values = ["rename", "overwrite", "ignore"]  # noqa: E501
        if conflict_resolution not in allowed_values:
            raise ValueError(
                "Invalid value for `conflict_resolution` ({0}), must be one of {1}"  # noqa: E501
                .format(conflict_resolution, allowed_values)
            )

        self._conflict_resolution = conflict_resolution

    @property
    def action(self):
        """Gets the action of this Task.  # noqa: E501


        :return: The action of this Task.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Task.


        :param action: The action of this Task.  # noqa: E501
        :type: str
        """
        allowed_values = ["noop", "run", "pause", "stop", "resume"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def activate(self):
        """Gets the activate of this Task.  # noqa: E501


        :return: The activate of this Task.  # noqa: E501
        :rtype: bool
        """
        return self._activate

    @activate.setter
    def activate(self, activate):
        """Sets the activate of this Task.


        :param activate: The activate of this Task.  # noqa: E501
        :type: bool
        """

        self._activate = activate

    @property
    def creation_date(self):
        """Gets the creation_date of this Task.  # noqa: E501


        :return: The creation_date of this Task.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Task.


        :param creation_date: The creation_date of this Task.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def modification_date(self):
        """Gets the modification_date of this Task.  # noqa: E501


        :return: The modification_date of this Task.  # noqa: E501
        :rtype: str
        """
        return self._modification_date

    @modification_date.setter
    def modification_date(self, modification_date):
        """Sets the modification_date of this Task.


        :param modification_date: The modification_date of this Task.  # noqa: E501
        :type: str
        """

        self._modification_date = modification_date

    @property
    def creation_username(self):
        """Gets the creation_username of this Task.  # noqa: E501


        :return: The creation_username of this Task.  # noqa: E501
        :rtype: str
        """
        return self._creation_username

    @creation_username.setter
    def creation_username(self, creation_username):
        """Sets the creation_username of this Task.


        :param creation_username: The creation_username of this Task.  # noqa: E501
        :type: str
        """

        self._creation_username = creation_username

    @property
    def modification_username(self):
        """Gets the modification_username of this Task.  # noqa: E501


        :return: The modification_username of this Task.  # noqa: E501
        :rtype: str
        """
        return self._modification_username

    @modification_username.setter
    def modification_username(self, modification_username):
        """Sets the modification_username of this Task.


        :param modification_username: The modification_username of this Task.  # noqa: E501
        :type: str
        """

        self._modification_username = modification_username

    @property
    def status(self):
        """Gets the status of this Task.  # noqa: E501


        :return: The status of this Task.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.


        :param status: The status of this Task.  # noqa: E501
        :type: str
        """
        allowed_values = ["not_activated", "done", "in_progress", "error", "paused", "stopped_by_system", "in_queue", "finished_with_warnings", "calculating", "stopped_by_user"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def job_started(self):
        """Gets the job_started of this Task.  # noqa: E501


        :return: The job_started of this Task.  # noqa: E501
        :rtype: str
        """
        return self._job_started

    @job_started.setter
    def job_started(self, job_started):
        """Sets the job_started of this Task.


        :param job_started: The job_started of this Task.  # noqa: E501
        :type: str
        """

        self._job_started = job_started

    @property
    def job_finished(self):
        """Gets the job_finished of this Task.  # noqa: E501


        :return: The job_finished of this Task.  # noqa: E501
        :rtype: str
        """
        return self._job_finished

    @job_finished.setter
    def job_finished(self, job_finished):
        """Sets the job_finished of this Task.


        :param job_finished: The job_finished of this Task.  # noqa: E501
        :type: str
        """

        self._job_finished = job_finished

    @property
    def processed_size(self):
        """Gets the processed_size of this Task.  # noqa: E501


        :return: The processed_size of this Task.  # noqa: E501
        :rtype: int
        """
        return self._processed_size

    @processed_size.setter
    def processed_size(self, processed_size):
        """Sets the processed_size of this Task.


        :param processed_size: The processed_size of this Task.  # noqa: E501
        :type: int
        """

        self._processed_size = processed_size

    @property
    def to_process_size(self):
        """Gets the to_process_size of this Task.  # noqa: E501


        :return: The to_process_size of this Task.  # noqa: E501
        :rtype: int
        """
        return self._to_process_size

    @to_process_size.setter
    def to_process_size(self, to_process_size):
        """Sets the to_process_size of this Task.


        :param to_process_size: The to_process_size of this Task.  # noqa: E501
        :type: int
        """

        self._to_process_size = to_process_size

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
        if issubclass(Task, dict):
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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
