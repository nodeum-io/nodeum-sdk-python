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
from swagger_client.api.cloud_pools_api import CloudPoolsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCloudPoolsApi(unittest.TestCase):
    """CloudPoolsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.cloud_pools_api.CloudPoolsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cloud_pool(self):
        """Test case for create_cloud_pool

        Creates a new cloud pool.  # noqa: E501
        """
        pass

    def test_destroy_cloud_pool(self):
        """Test case for destroy_cloud_pool

        Destroys a specific cloud pool.  # noqa: E501
        """
        pass

    def test_index_cloud_pools(self):
        """Test case for index_cloud_pools

        Lists all cloud pools.  # noqa: E501
        """
        pass

    def test_show_cloud_pool(self):
        """Test case for show_cloud_pool

        Displays a specific cloud pool.  # noqa: E501
        """
        pass

    def test_update_cloud_pool(self):
        """Test case for update_cloud_pool

        Updates a specific cloud pool.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
