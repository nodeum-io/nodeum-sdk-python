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
from swagger_client.models.tape_drive_device_collection import TapeDriveDeviceCollection  # noqa: E501
from swagger_client.rest import ApiException


class TestTapeDriveDeviceCollection(unittest.TestCase):
    """TapeDriveDeviceCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTapeDriveDeviceCollection(self):
        """Test TapeDriveDeviceCollection"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.tape_drive_device_collection.TapeDriveDeviceCollection()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
