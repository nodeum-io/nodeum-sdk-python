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
from nodeum_sdk.api.statistics_api import StatisticsApi  # noqa: E501
from nodeum_sdk.rest import ApiException


class TestStatisticsApi(unittest.TestCase):
    """StatisticsApi unit test stubs"""

    def setUp(self):
        self.api = nodeum_sdk.api.statistics_api.StatisticsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_statistics_by_file_extension(self):
        """Test case for statistics_by_file_extension

        TODO  # noqa: E501
        """
        pass

    def test_statistics_by_group_owner(self):
        """Test case for statistics_by_group_owner

        TODO  # noqa: E501
        """
        pass

    def test_statistics_by_primary_name(self):
        """Test case for statistics_by_primary_name

        TODO  # noqa: E501
        """
        pass

    def test_statistics_by_secondary_storage(self):
        """Test case for statistics_by_secondary_storage

        TODO  # noqa: E501
        """
        pass

    def test_statistics_by_size(self):
        """Test case for statistics_by_size

        TODO  # noqa: E501
        """
        pass

    def test_statistics_by_user_owner(self):
        """Test case for statistics_by_user_owner

        TODO  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()