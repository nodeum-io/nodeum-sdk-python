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
from nodeum_sdk.api.pools_api import PoolsApi  # noqa: E501
from nodeum_sdk.rest import ApiException


class TestPoolsApi(unittest.TestCase):
    """PoolsApi unit test stubs"""

    def setUp(self):
        self.api = nodeum_sdk.api.pools_api.PoolsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_pool(self):
        """Test case for create_pool

        Creates a new pool.  # noqa: E501
        """
        pass

    def test_create_primary_scan(self):
        """Test case for create_primary_scan

        Set a new primary pool scan option.  # noqa: E501
        """
        pass

    def test_destroy_pool(self):
        """Test case for destroy_pool

        Destroys a specific tape pool.  # noqa: E501
        """
        pass

    def test_destroy_primary_scan(self):
        """Test case for destroy_primary_scan

        Disable the primary pool scan.  # noqa: E501
        """
        pass

    def test_index_pools(self):
        """Test case for index_pools

        Lists all pools.  # noqa: E501
        """
        pass

    def test_mount_pool(self):
        """Test case for mount_pool

        Mount Pool.  # noqa: E501
        """
        pass

    def test_mount_status_pool(self):
        """Test case for mount_status_pool

        Get mount status of Pool.  # noqa: E501
        """
        pass

    def test_show_pool(self):
        """Test case for show_pool

        Displays a specific pool.  # noqa: E501
        """
        pass

    def test_show_primary_scan(self):
        """Test case for show_primary_scan

        Displays the primary pool scan status.  # noqa: E501
        """
        pass

    def test_sync_primary_pool(self):
        """Test case for sync_primary_pool

        Synchronize a primary after a scan (for internal use only).  # noqa: E501
        """
        pass

    def test_unmount_pool(self):
        """Test case for unmount_pool

        Unmount Pool.  # noqa: E501
        """
        pass

    def test_update_pool(self):
        """Test case for update_pool

        Updates a specific pool.  # noqa: E501
        """
        pass

    def test_update_primary_scan(self):
        """Test case for update_primary_scan

        Updates the existing primary pool scan option.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
