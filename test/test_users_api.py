# coding: utf-8

"""
    Nodeum API

    Nodeum API  # Filter parameters When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_api_key(self):
        """Test case for create_api_key

        Creates a new API Key for current user.  # noqa: E501
        """
        pass

    def test_destroy_api_key(self):
        """Test case for destroy_api_key

        Destroys a specific API Key.  # noqa: E501
        """
        pass

    def test_index_api_keys(self):
        """Test case for index_api_keys

        Lists all API keys of current user.  # noqa: E501
        """
        pass

    def test_show_api_key(self):
        """Test case for show_api_key

        Displays a specific API Key with its scopes.  # noqa: E501
        """
        pass

    def test_update_api_key(self):
        """Test case for update_api_key

        Updates a specific API Key.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
