# coding: utf-8

"""
    Nodeum API

    # About  This document describes the Nodeum API version 2:  If you are looking for any information about the product itself, reach the product website https://www.nodeum.io. You can also contact us at this email address : info@nodeum.io  # Filter parameters When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from nodeum_sdk.configuration import Configuration


class TapeLibrary(object):
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
        'io_slots_address': 'int',
        'id': 'int',
        'name': 'str',
        'comment': 'str',
        'libso': 'str',
        'status': 'str',
        'price': 'str'
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
        'io_slots_address': 'io_slots_address',
        'id': 'id',
        'name': 'name',
        'comment': 'comment',
        'libso': 'libso',
        'status': 'status',
        'price': 'price'
    }

    def __init__(self, serial=None, protocol=None, vendor=None, product=None, firmware=None, device=None, acs=None, storage_slots=None, storage_slots_address=None, io_slots=None, io_slots_address=None, id=None, name=None, comment=None, libso=None, status=None, price=None, local_vars_configuration=None):  # noqa: E501
        """TapeLibrary - a model defined in OpenAPI"""  # noqa: E501
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
        self._id = None
        self._name = None
        self._comment = None
        self._libso = None
        self._status = None
        self._price = None
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
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if comment is not None:
            self.comment = comment
        if libso is not None:
            self.libso = libso
        if status is not None:
            self.status = status
        if price is not None:
            self.price = price

    @property
    def serial(self):
        """Gets the serial of this TapeLibrary.  # noqa: E501


        :return: The serial of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this TapeLibrary.


        :param serial: The serial of this TapeLibrary.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def protocol(self):
        """Gets the protocol of this TapeLibrary.  # noqa: E501


        :return: The protocol of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TapeLibrary.


        :param protocol: The protocol of this TapeLibrary.  # noqa: E501
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
        """Gets the vendor of this TapeLibrary.  # noqa: E501


        :return: The vendor of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this TapeLibrary.


        :param vendor: The vendor of this TapeLibrary.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def product(self):
        """Gets the product of this TapeLibrary.  # noqa: E501


        :return: The product of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this TapeLibrary.


        :param product: The product of this TapeLibrary.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def firmware(self):
        """Gets the firmware of this TapeLibrary.  # noqa: E501


        :return: The firmware of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """Sets the firmware of this TapeLibrary.


        :param firmware: The firmware of this TapeLibrary.  # noqa: E501
        :type: str
        """

        self._firmware = firmware

    @property
    def device(self):
        """Gets the device of this TapeLibrary.  # noqa: E501


        :return: The device of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this TapeLibrary.


        :param device: The device of this TapeLibrary.  # noqa: E501
        :type: str
        """

        self._device = device

    @property
    def acs(self):
        """Gets the acs of this TapeLibrary.  # noqa: E501


        :return: The acs of this TapeLibrary.  # noqa: E501
        :rtype: int
        """
        return self._acs

    @acs.setter
    def acs(self, acs):
        """Sets the acs of this TapeLibrary.


        :param acs: The acs of this TapeLibrary.  # noqa: E501
        :type: int
        """

        self._acs = acs

    @property
    def storage_slots(self):
        """Gets the storage_slots of this TapeLibrary.  # noqa: E501


        :return: The storage_slots of this TapeLibrary.  # noqa: E501
        :rtype: int
        """
        return self._storage_slots

    @storage_slots.setter
    def storage_slots(self, storage_slots):
        """Sets the storage_slots of this TapeLibrary.


        :param storage_slots: The storage_slots of this TapeLibrary.  # noqa: E501
        :type: int
        """

        self._storage_slots = storage_slots

    @property
    def storage_slots_address(self):
        """Gets the storage_slots_address of this TapeLibrary.  # noqa: E501


        :return: The storage_slots_address of this TapeLibrary.  # noqa: E501
        :rtype: int
        """
        return self._storage_slots_address

    @storage_slots_address.setter
    def storage_slots_address(self, storage_slots_address):
        """Sets the storage_slots_address of this TapeLibrary.


        :param storage_slots_address: The storage_slots_address of this TapeLibrary.  # noqa: E501
        :type: int
        """

        self._storage_slots_address = storage_slots_address

    @property
    def io_slots(self):
        """Gets the io_slots of this TapeLibrary.  # noqa: E501


        :return: The io_slots of this TapeLibrary.  # noqa: E501
        :rtype: int
        """
        return self._io_slots

    @io_slots.setter
    def io_slots(self, io_slots):
        """Sets the io_slots of this TapeLibrary.


        :param io_slots: The io_slots of this TapeLibrary.  # noqa: E501
        :type: int
        """

        self._io_slots = io_slots

    @property
    def io_slots_address(self):
        """Gets the io_slots_address of this TapeLibrary.  # noqa: E501


        :return: The io_slots_address of this TapeLibrary.  # noqa: E501
        :rtype: int
        """
        return self._io_slots_address

    @io_slots_address.setter
    def io_slots_address(self, io_slots_address):
        """Sets the io_slots_address of this TapeLibrary.


        :param io_slots_address: The io_slots_address of this TapeLibrary.  # noqa: E501
        :type: int
        """

        self._io_slots_address = io_slots_address

    @property
    def id(self):
        """Gets the id of this TapeLibrary.  # noqa: E501


        :return: The id of this TapeLibrary.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TapeLibrary.


        :param id: The id of this TapeLibrary.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TapeLibrary.  # noqa: E501


        :return: The name of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapeLibrary.


        :param name: The name of this TapeLibrary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def comment(self):
        """Gets the comment of this TapeLibrary.  # noqa: E501


        :return: The comment of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this TapeLibrary.


        :param comment: The comment of this TapeLibrary.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def libso(self):
        """Gets the libso of this TapeLibrary.  # noqa: E501


        :return: The libso of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._libso

    @libso.setter
    def libso(self, libso):
        """Sets the libso of this TapeLibrary.


        :param libso: The libso of this TapeLibrary.  # noqa: E501
        :type: str
        """

        self._libso = libso

    @property
    def status(self):
        """Gets the status of this TapeLibrary.  # noqa: E501


        :return: The status of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TapeLibrary.


        :param status: The status of this TapeLibrary.  # noqa: E501
        :type: str
        """
        allowed_values = ["offline", "online"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def price(self):
        """Gets the price of this TapeLibrary.  # noqa: E501


        :return: The price of this TapeLibrary.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this TapeLibrary.


        :param price: The price of this TapeLibrary.  # noqa: E501
        :type: str
        """

        self._price = price

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
        if not isinstance(other, TapeLibrary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TapeLibrary):
            return True

        return self.to_dict() != other.to_dict()