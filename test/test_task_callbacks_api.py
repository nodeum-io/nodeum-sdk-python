# coding: utf-8

"""
    Nodeum API

    # About  This document describes the Nodeum API version 2:  If you are looking for any information about the product itself, reach the product website https://www.nodeum.io. You can also contact us at this email address : info@nodeum.io  # Filter parameters When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import nodeum_sdk
from nodeum_sdk.api.task_callbacks_api import TaskCallbacksApi  # noqa: E501
from nodeum_sdk.rest import ApiException


class TestTaskCallbacksApi(unittest.TestCase):
    """TaskCallbacksApi unit test stubs"""

    def setUp(self):
        self.api = nodeum_sdk.api.task_callbacks_api.TaskCallbacksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_task_callback(self):
        """Test case for create_task_callback

        Creates a new task callback.  # noqa: E501
        """
        pass

    def test_destroy_task_callback(self):
        """Test case for destroy_task_callback

        Destroys a specific task callback.  # noqa: E501
        """
        pass

    def test_index_task_callbacks(self):
        """Test case for index_task_callbacks

        Lists all task callbacks.  # noqa: E501
        """
        pass

    def test_show_task_callback(self):
        """Test case for show_task_callback

        Displays a specific task callback.  # noqa: E501
        """
        pass

    def test_update_task_callback(self):
        """Test case for update_task_callback

        Updates a specific task callback.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
