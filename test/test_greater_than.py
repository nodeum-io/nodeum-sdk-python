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
from nodeum_sdk.models.greater_than import GreaterThan  # noqa: E501
from nodeum_sdk.rest import ApiException


class TestGreaterThan(unittest.TestCase):
    """GreaterThan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGreaterThan(self):
        """Test GreaterThan"""
        # FIXME: construct object with mandatory attributes with example values
        # model = nodeum_sdk.models.greater_than.GreaterThan()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
