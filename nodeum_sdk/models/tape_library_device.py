# coding: utf-8

"""
    Nodeum API

    The Nodeum API makes it easy to tap into the digital data mesh that runs across your organisation. Make requests to our API endpoints and we’ll give you everything you need to interconnect your business workflows with your storage.  All production API requests are made to:  http://nodeumhostname/api/  The current production version of the API is v1.   **REST** The Nodeum API is a RESTful API. This means that the API is designed to allow you to get, create, update, & delete objects with the HTTP verbs GET, POST, PUT, PATCH, & DELETE.  **JSON** The Nodeum API speaks exclusively in JSON. This means that you should always set the Content-Type header to application/json to ensure that your requests are properly accepted and processed by the API.  **Authentication** All API calls require user-password authentication.   **Cross-Origin Resource Sharing** The Nodeum API supports CORS for communicating from Javascript for these endpoints. You will need to specify an Origin URI when creating your application to allow for CORS to be whitelisted for your domain.   **Pagination** Some endpoints such as File Listing return a potentially lengthy array of objects. In order to keep the response sizes manageable the API will take advantage of pagination. Pagination is a mechanism for returning a subset of the results for a request and allowing for subsequent requests to “page” through the rest of the results until the end is reached. Paginated endpoints follow a standard interface that accepts two query parameters, limit and offset, and return a payload that follows a standard form. These parameters names and their behavior are borrowed from SQL LIMIT and OFFSET keywords.  **Versioning** The Nodeum API is constantly being worked on to add features, make improvements, and fix bugs. This means that you should expect changes to be introduced and documented.   However, there are some changes or additions that are considered backwards-compatible and your applications should be flexible enough to handle them. These include:  - Adding new endpoints to the API - Adding new attributes to the response of an existing endpoint - Changing the order of attributes of responses (JSON by definition is an object of unordered key/value pairs)  **Filter parameters** When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: info@nodeum.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from nodeum_sdk.configuration import Configuration


class TapeLibraryDevice(object):
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
        'serial': 'str',
        'protocol': 'str',
        'vendor': 'str',
        'product': 'str',
        'firmware': 'str',
        'device': 'str',
        'acs': 'int',
        'storage_slots': 'int',
        'storage_slots_address': 'int',
        'io_slots': 'int',
        'io_slots_address': 'int'
    }

    attribute_map = {
        'serial': 'serial',
        'protocol': 'protocol',
        'vendor': 'vendor',
        'product': 'product',
        'firmware': 'firmware',
        'device': 'device',
        'acs': 'acs',
        'storage_slots': 'storage_slots',
        'storage_slots_address': 'storage_slots_address',
        'io_slots': 'io_slots',
        'io_slots_address': 'io_slots_address'
    }

    def __init__(self, serial=None, protocol=None, vendor=None, product=None, firmware=None, device=None, acs=None, storage_slots=None, storage_slots_address=None, io_slots=None, io_slots_address=None, local_vars_configuration=None):  # noqa: E501
        """TapeLibraryDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._serial = None
        self._protocol = None
        self._vendor = None
        self._product = None
        self._firmware = None
        self._device = None
        self._acs = None
        self._storage_slots = None
        self._storage_slots_address = None
        self._io_slots = None
        self._io_slots_address = None
        self.discriminator = None

        if serial is not None:
            self.serial = serial
        if protocol is not None:
            self.protocol = protocol
        if vendor is not None:
            self.vendor = vendor
        if product is not None:
            self.product = product
        if firmware is not None:
            self.firmware = firmware
        if device is not None:
            self.device = device
        if acs is not None:
            self.acs = acs
        if storage_slots is not None:
            self.storage_slots = storage_slots
        if storage_slots_address is not None:
            self.storage_slots_address = storage_slots_address
        if io_slots is not None:
            self.io_slots = io_slots
        if io_slots_address is not None:
            self.io_slots_address = io_slots_address

    @property
    def serial(self):
        """Gets the serial of this TapeLibraryDevice.  # noqa: E501


        :return: The serial of this TapeLibraryDevice.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this TapeLibraryDevice.


        :param serial: The serial of this TapeLibraryDevice.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def protocol(self):
        """Gets the protocol of this TapeLibraryDevice.  # noqa: E501


        :return: The protocol of this TapeLibraryDevice.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TapeLibraryDevice.


        :param protocol: The protocol of this TapeLibraryDevice.  # noqa: E501
        :type: str
        """
        allowed_values = ["scsi", "acsls"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and protocol not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def vendor(self):
        """Gets the vendor of this TapeLibraryDevice.  # noqa: E501


        :return: The vendor of this TapeLibraryDevice.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this TapeLibraryDevice.


        :param vendor: The vendor of this TapeLibraryDevice.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def product(self):
        """Gets the product of this TapeLibraryDevice.  # noqa: E501


        :return: The product of this TapeLibraryDevice.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this TapeLibraryDevice.


        :param product: The product of this TapeLibraryDevice.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def firmware(self):
        """Gets the firmware of this TapeLibraryDevice.  # noqa: E501


        :return: The firmware of this TapeLibraryDevice.  # noqa: E501
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this TapeLibraryDevice.


        :param firmware: The firmware of this TapeLibraryDevice.  # noqa: E501
        :type: str
        """

        self._firmware = firmware

    @property
    def device(self):
        """Gets the device of this TapeLibraryDevice.  # noqa: E501


        :return: The device of this TapeLibraryDevice.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this TapeLibraryDevice.


        :param device: The device of this TapeLibraryDevice.  # noqa: E501
        :type: str
        """

        self._device = device

    @property
    def acs(self):
        """Gets the acs of this TapeLibraryDevice.  # noqa: E501


        :return: The acs of this TapeLibraryDevice.  # noqa: E501
        :rtype: int
        """
        return self._acs

    @acs.setter
    def acs(self, acs):
        """Sets the acs of this TapeLibraryDevice.


        :param acs: The acs of this TapeLibraryDevice.  # noqa: E501
        :type: int
        """

        self._acs = acs

    @property
    def storage_slots(self):
        """Gets the storage_slots of this TapeLibraryDevice.  # noqa: E501


        :return: The storage_slots of this TapeLibraryDevice.  # noqa: E501
        :rtype: int
        """
        return self._storage_slots

    @storage_slots.setter
    def storage_slots(self, storage_slots):
        """Sets the storage_slots of this TapeLibraryDevice.


        :param storage_slots: The storage_slots of this TapeLibraryDevice.  # noqa: E501
        :type: int
        """

        self._storage_slots = storage_slots

    @property
    def storage_slots_address(self):
        """Gets the storage_slots_address of this TapeLibraryDevice.  # noqa: E501


        :return: The storage_slots_address of this TapeLibraryDevice.  # noqa: E501
        :rtype: int
        """
        return self._storage_slots_address

    @storage_slots_address.setter
    def storage_slots_address(self, storage_slots_address):
        """Sets the storage_slots_address of this TapeLibraryDevice.


        :param storage_slots_address: The storage_slots_address of this TapeLibraryDevice.  # noqa: E501
        :type: int
        """

        self._storage_slots_address = storage_slots_address

    @property
    def io_slots(self):
        """Gets the io_slots of this TapeLibraryDevice.  # noqa: E501


        :return: The io_slots of this TapeLibraryDevice.  # noqa: E501
        :rtype: int
        """
        return self._io_slots

    @io_slots.setter
    def io_slots(self, io_slots):
        """Sets the io_slots of this TapeLibraryDevice.


        :param io_slots: The io_slots of this TapeLibraryDevice.  # noqa: E501
        :type: int
        """

        self._io_slots = io_slots

    @property
    def io_slots_address(self):
        """Gets the io_slots_address of this TapeLibraryDevice.  # noqa: E501


        :return: The io_slots_address of this TapeLibraryDevice.  # noqa: E501
        :rtype: int
        """
        return self._io_slots_address

    @io_slots_address.setter
    def io_slots_address(self, io_slots_address):
        """Sets the io_slots_address of this TapeLibraryDevice.


        :param io_slots_address: The io_slots_address of this TapeLibraryDevice.  # noqa: E501
        :type: int
        """

        self._io_slots_address = io_slots_address

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
        if not isinstance(other, TapeLibraryDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TapeLibraryDevice):
            return True

        return self.to_dict() != other.to_dict()
