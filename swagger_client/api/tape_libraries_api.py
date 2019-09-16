# coding: utf-8

"""
    Nodeum API

    Nodeum API  # Filter parameters When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TapeLibrariesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_tape_library(self, tape_library_body, **kwargs):  # noqa: E501
        """Creates a new tape library.  # noqa: E501

        **API Key Scope**: tape_libraries / create  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tape_library(tape_library_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TapeLibrary tape_library_body: (required)
        :return: TapeLibrary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_tape_library_with_http_info(tape_library_body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_tape_library_with_http_info(tape_library_body, **kwargs)  # noqa: E501
            return data

    def create_tape_library_with_http_info(self, tape_library_body, **kwargs):  # noqa: E501
        """Creates a new tape library.  # noqa: E501

        **API Key Scope**: tape_libraries / create  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_tape_library_with_http_info(tape_library_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TapeLibrary tape_library_body: (required)
        :return: TapeLibrary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tape_library_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_tape_library" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tape_library_body' is set
        if ('tape_library_body' not in params or
                params['tape_library_body'] is None):
            raise ValueError("Missing the required parameter `tape_library_body` when calling `create_tape_library`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tape_library_body' in params:
            body_params = params['tape_library_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tape_libraries', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TapeLibrary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def destroy_tape_library(self, tape_library_id, **kwargs):  # noqa: E501
        """Destroys a specific tape library.  # noqa: E501

        **API Key Scope**: tape_libraries / destroy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_tape_library(tape_library_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tape_library_id: Numeric ID, serial, or name of tape library. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.destroy_tape_library_with_http_info(tape_library_id, **kwargs)  # noqa: E501
        else:
            (data) = self.destroy_tape_library_with_http_info(tape_library_id, **kwargs)  # noqa: E501
            return data

    def destroy_tape_library_with_http_info(self, tape_library_id, **kwargs):  # noqa: E501
        """Destroys a specific tape library.  # noqa: E501

        **API Key Scope**: tape_libraries / destroy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_tape_library_with_http_info(tape_library_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tape_library_id: Numeric ID, serial, or name of tape library. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tape_library_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destroy_tape_library" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tape_library_id' is set
        if ('tape_library_id' not in params or
                params['tape_library_id'] is None):
            raise ValueError("Missing the required parameter `tape_library_id` when calling `destroy_tape_library`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tape_library_id' in params:
            path_params['tape_library_id'] = params['tape_library_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tape_libraries/{tape_library_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def index_tape_libraries(self, **kwargs):  # noqa: E501
        """Lists all tape libraries.  # noqa: E501

        **API Key Scope**: tape_libraries / index  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_tape_libraries(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The number of items to display for pagination.
        :param int offset: The number of items to skip for pagination.
        :param list[str] sort_by: Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`.
        :param str id: Filter on id
        :param str name: Filter on name
        :param str serial: Filter on serial
        :param str comment: Filter on comment
        :param str protocol: Filter on protocol
        :param str vendor: Filter on vendor
        :param str product: Filter on product
        :param str firmware: Filter on firmware
        :param str device: Filter on device
        :param str libso: Filter on libso
        :param str acs: Filter on acs
        :param str status: Filter on status
        :param str storage_slots: Filter on storage slots
        :param str storage_slots_address: Filter on storage slots address
        :param str io_slots: Filter on io slots
        :param str io_slots_address: Filter on io slots address
        :param str price: Filter on price
        :return: TapeLibraryCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.index_tape_libraries_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.index_tape_libraries_with_http_info(**kwargs)  # noqa: E501
            return data

    def index_tape_libraries_with_http_info(self, **kwargs):  # noqa: E501
        """Lists all tape libraries.  # noqa: E501

        **API Key Scope**: tape_libraries / index  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_tape_libraries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The number of items to display for pagination.
        :param int offset: The number of items to skip for pagination.
        :param list[str] sort_by: Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`.
        :param str id: Filter on id
        :param str name: Filter on name
        :param str serial: Filter on serial
        :param str comment: Filter on comment
        :param str protocol: Filter on protocol
        :param str vendor: Filter on vendor
        :param str product: Filter on product
        :param str firmware: Filter on firmware
        :param str device: Filter on device
        :param str libso: Filter on libso
        :param str acs: Filter on acs
        :param str status: Filter on status
        :param str storage_slots: Filter on storage slots
        :param str storage_slots_address: Filter on storage slots address
        :param str io_slots: Filter on io slots
        :param str io_slots_address: Filter on io slots address
        :param str price: Filter on price
        :return: TapeLibraryCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'sort_by', 'id', 'name', 'serial', 'comment', 'protocol', 'vendor', 'product', 'firmware', 'device', 'libso', 'acs', 'status', 'storage_slots', 'storage_slots_address', 'io_slots', 'io_slots_address', 'price']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method index_tape_libraries" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'sort_by' in params:
            query_params.append(('sort_by', params['sort_by']))  # noqa: E501
            collection_formats['sort_by'] = 'pipes'  # noqa: E501
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'serial' in params:
            query_params.append(('serial', params['serial']))  # noqa: E501
        if 'comment' in params:
            query_params.append(('comment', params['comment']))  # noqa: E501
        if 'protocol' in params:
            query_params.append(('protocol', params['protocol']))  # noqa: E501
        if 'vendor' in params:
            query_params.append(('vendor', params['vendor']))  # noqa: E501
        if 'product' in params:
            query_params.append(('product', params['product']))  # noqa: E501
        if 'firmware' in params:
            query_params.append(('firmware', params['firmware']))  # noqa: E501
        if 'device' in params:
            query_params.append(('device', params['device']))  # noqa: E501
        if 'libso' in params:
            query_params.append(('libso', params['libso']))  # noqa: E501
        if 'acs' in params:
            query_params.append(('acs', params['acs']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'storage_slots' in params:
            query_params.append(('storage_slots', params['storage_slots']))  # noqa: E501
        if 'storage_slots_address' in params:
            query_params.append(('storage_slots_address', params['storage_slots_address']))  # noqa: E501
        if 'io_slots' in params:
            query_params.append(('io_slots', params['io_slots']))  # noqa: E501
        if 'io_slots_address' in params:
            query_params.append(('io_slots_address', params['io_slots_address']))  # noqa: E501
        if 'price' in params:
            query_params.append(('price', params['price']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tape_libraries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TapeLibraryCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def index_tape_library_devices(self, **kwargs):  # noqa: E501
        """Lists tape libraries devices.  # noqa: E501

        **API Key Scope**: tape_libraries / devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_tape_library_devices(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: ID of active job
        :return: TapeLibraryDeviceCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.index_tape_library_devices_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.index_tape_library_devices_with_http_info(**kwargs)  # noqa: E501
            return data

    def index_tape_library_devices_with_http_info(self, **kwargs):  # noqa: E501
        """Lists tape libraries devices.  # noqa: E501

        **API Key Scope**: tape_libraries / devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_tape_library_devices_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: ID of active job
        :return: TapeLibraryDeviceCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method index_tape_library_devices" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in params:
            query_params.append(('job_id', params['job_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tape_libraries/-/devices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TapeLibraryDeviceCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def show_tape_library(self, tape_library_id, **kwargs):  # noqa: E501
        """Displays a specific tape library.  # noqa: E501

        **API Key Scope**: tape_libraries / show  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_tape_library(tape_library_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tape_library_id: Numeric ID, serial, or name of tape library. (required)
        :return: TapeLibrary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.show_tape_library_with_http_info(tape_library_id, **kwargs)  # noqa: E501
        else:
            (data) = self.show_tape_library_with_http_info(tape_library_id, **kwargs)  # noqa: E501
            return data

    def show_tape_library_with_http_info(self, tape_library_id, **kwargs):  # noqa: E501
        """Displays a specific tape library.  # noqa: E501

        **API Key Scope**: tape_libraries / show  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_tape_library_with_http_info(tape_library_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tape_library_id: Numeric ID, serial, or name of tape library. (required)
        :return: TapeLibrary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tape_library_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_tape_library" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tape_library_id' is set
        if ('tape_library_id' not in params or
                params['tape_library_id'] is None):
            raise ValueError("Missing the required parameter `tape_library_id` when calling `show_tape_library`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tape_library_id' in params:
            path_params['tape_library_id'] = params['tape_library_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tape_libraries/{tape_library_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TapeLibrary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_tape_library(self, tape_library_id, tape_library_body, **kwargs):  # noqa: E501
        """Updates a specific tape library.  # noqa: E501

        **API Key Scope**: tape_libraries / update  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tape_library(tape_library_id, tape_library_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tape_library_id: Numeric ID, serial, or name of tape library. (required)
        :param TapeLibrary tape_library_body: (required)
        :return: TapeLibrary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_tape_library_with_http_info(tape_library_id, tape_library_body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_tape_library_with_http_info(tape_library_id, tape_library_body, **kwargs)  # noqa: E501
            return data

    def update_tape_library_with_http_info(self, tape_library_id, tape_library_body, **kwargs):  # noqa: E501
        """Updates a specific tape library.  # noqa: E501

        **API Key Scope**: tape_libraries / update  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_tape_library_with_http_info(tape_library_id, tape_library_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tape_library_id: Numeric ID, serial, or name of tape library. (required)
        :param TapeLibrary tape_library_body: (required)
        :return: TapeLibrary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tape_library_id', 'tape_library_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_tape_library" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tape_library_id' is set
        if ('tape_library_id' not in params or
                params['tape_library_id'] is None):
            raise ValueError("Missing the required parameter `tape_library_id` when calling `update_tape_library`")  # noqa: E501
        # verify the required parameter 'tape_library_body' is set
        if ('tape_library_body' not in params or
                params['tape_library_body'] is None):
            raise ValueError("Missing the required parameter `tape_library_body` when calling `update_tape_library`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tape_library_id' in params:
            path_params['tape_library_id'] = params['tape_library_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tape_library_body' in params:
            body_params = params['tape_library_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tape_libraries/{tape_library_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TapeLibrary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
