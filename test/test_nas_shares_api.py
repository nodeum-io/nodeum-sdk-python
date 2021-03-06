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
from nodeum_sdk.api.nas_shares_api import NasSharesApi  # noqa: E501
from nodeum_sdk.rest import ApiException


class TestNasSharesApi(unittest.TestCase):
    """NasSharesApi unit test stubs"""

    def setUp(self):
        self.api = nodeum_sdk.api.nas_shares_api.NasSharesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_nas_share_by_nas(self):
        """Test case for create_nas_share_by_nas

        Creates a new NAS share.  # noqa: E501
        """
        pass

    def test_destroy_nas_share(self):
        """Test case for destroy_nas_share

        Destroys a specific NAS share.  # noqa: E501
        """
        pass

    def test_destroy_nas_share_by_nas(self):
        """Test case for destroy_nas_share_by_nas

        Destroys a specific NAS share.  # noqa: E501
        """
        pass

    def test_destroy_nas_share_by_pool(self):
        """Test case for destroy_nas_share_by_pool

        Destroys a specific NAS share.  # noqa: E501
        """
        pass

    def test_index_nas_shares(self):
        """Test case for index_nas_shares

        Lists all NAS shares.  # noqa: E501
        """
        pass

    def test_index_nas_shares_by_nas(self):
        """Test case for index_nas_shares_by_nas

        Lists all NAS shares.  # noqa: E501
        """
        pass

    def test_index_nas_shares_by_pool(self):
        """Test case for index_nas_shares_by_pool

        Lists all NAS shares from pool.  # noqa: E501
        """
        pass

    def test_mount_status_nas_share(self):
        """Test case for mount_status_nas_share

        Get mount status of NAS Share.  # noqa: E501
        """
        pass

    def test_mount_status_nas_share_by_nas(self):
        """Test case for mount_status_nas_share_by_nas

        Get mount status of NAS Share.  # noqa: E501
        """
        pass

    def test_mount_status_nas_share_by_pool(self):
        """Test case for mount_status_nas_share_by_pool

        Get mount status of NAS Share.  # noqa: E501
        """
        pass

    def test_show_nas_share(self):
        """Test case for show_nas_share

        Displays a specific NAS share.  # noqa: E501
        """
        pass

    def test_show_nas_share_by_nas(self):
        """Test case for show_nas_share_by_nas

        Displays a specific NAS share.  # noqa: E501
        """
        pass

    def test_show_nas_share_by_pool(self):
        """Test case for show_nas_share_by_pool

        Displays a specific NAS share.  # noqa: E501
        """
        pass

    def test_test_nas_share(self):
        """Test case for test_nas_share

        Test an unsaved NAS Share.  # noqa: E501
        """
        pass

    def test_test_result_nas_share(self):
        """Test case for test_result_nas_share

        Check result of a NAS Share test job.  # noqa: E501
        """
        pass

    def test_update_nas_share(self):
        """Test case for update_nas_share

        Updates a specific NAS share.  # noqa: E501
        """
        pass

    def test_update_nas_share_by_nas(self):
        """Test case for update_nas_share_by_nas

        Updates a specific NAS share.  # noqa: E501
        """
        pass

    def test_update_nas_share_by_pool(self):
        """Test case for update_nas_share_by_pool

        Updates a specific NAS share.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
