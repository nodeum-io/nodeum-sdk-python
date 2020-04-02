# coding: utf-8

"""
    Nodeum API

    # About  This document describes the Nodeum API version 2:  If you are looking for any information about the product itself, reach the product website https://www.nodeum.io. You can also contact us at this email address : info@nodeum.io  # Filter parameters When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nodeum_sdk.api_client import ApiClient
from nodeum_sdk.exceptions import (
    ApiTypeError,
    ApiValueError
)


class TaskOptionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_task_option(self, **kwargs):  # noqa: E501
        """Creates a new task option.  # noqa: E501

        **API Key Scope**: task_options / create  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_task_option(task_id=task_id_value, task_option_body=task_option_body_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param TaskOption task_option_body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TaskOption
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_task_option_with_http_info(**kwargs)  # noqa: E501

    def create_task_option_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a new task option.  # noqa: E501

        **API Key Scope**: task_options / create  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_task_option_with_http_info(task_id=task_id_value, task_option_body=task_option_body_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param TaskOption task_option_body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TaskOption, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['task_id', 'task_option_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_task_option" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `create_task_option`")  # noqa: E501
        # verify the required parameter 'task_option_body' is set
        if self.api_client.client_side_validation and ('task_option_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_option_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_option_body` when calling `create_task_option`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'task_option_body' in local_var_params:
            body_params = local_var_params['task_option_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{task_id}/task_options', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskOption',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def destroy_task_option(self, **kwargs):  # noqa: E501
        """Destroys a specific task option.  # noqa: E501

        **API Key Scope**: task_options / destroy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_task_option(task_id=task_id_value, task_option_id=task_option_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_option_id: Numeric ID of task option. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.destroy_task_option_with_http_info(**kwargs)  # noqa: E501

    def destroy_task_option_with_http_info(self, **kwargs):  # noqa: E501
        """Destroys a specific task option.  # noqa: E501

        **API Key Scope**: task_options / destroy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_task_option_with_http_info(task_id=task_id_value, task_option_id=task_option_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_option_id: Numeric ID of task option. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['task_id', 'task_option_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destroy_task_option" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `destroy_task_option`")  # noqa: E501
        # verify the required parameter 'task_option_id' is set
        if self.api_client.client_side_validation and ('task_option_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_option_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_option_id` when calling `destroy_task_option`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501
        if 'task_option_id' in local_var_params:
            path_params['task_option_id'] = local_var_params['task_option_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{task_id}/task_options/{task_option_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def index_task_options(self, **kwargs):  # noqa: E501
        """Lists all task options.  # noqa: E501

        **API Key Scope**: task_options / index  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_task_options(task_id=task_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int limit: The number of items to display for pagination.
        :param int offset: The number of items to skip for pagination.
        :param list[str] sort_by: Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`.
        :param str id: Filter on id
        :param str type: Filter on type
        :param str value: Filter on value
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TaskOptionCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.index_task_options_with_http_info(**kwargs)  # noqa: E501

    def index_task_options_with_http_info(self, **kwargs):  # noqa: E501
        """Lists all task options.  # noqa: E501

        **API Key Scope**: task_options / index  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_task_options_with_http_info(task_id=task_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int limit: The number of items to display for pagination.
        :param int offset: The number of items to skip for pagination.
        :param list[str] sort_by: Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`.
        :param str id: Filter on id
        :param str type: Filter on type
        :param str value: Filter on value
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TaskOptionCollection, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['task_id', 'limit', 'offset', 'sort_by', 'id', 'type', 'value']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method index_task_options" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `index_task_options`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sort_by', local_var_params['sort_by']))  # noqa: E501
            collection_formats['sort_by'] = 'pipe'  # noqa: E501
        if 'id' in local_var_params and local_var_params['id'] is not None:  # noqa: E501
            query_params.append(('id', local_var_params['id']))  # noqa: E501
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'value' in local_var_params and local_var_params['value'] is not None:  # noqa: E501
            query_params.append(('value', local_var_params['value']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{task_id}/task_options', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskOptionCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def show_task_option(self, **kwargs):  # noqa: E501
        """Displays a specific task option.  # noqa: E501

        **API Key Scope**: task_options / show  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_task_option(task_id=task_id_value, task_option_id=task_option_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_option_id: Numeric ID of task option. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TaskOption
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.show_task_option_with_http_info(**kwargs)  # noqa: E501

    def show_task_option_with_http_info(self, **kwargs):  # noqa: E501
        """Displays a specific task option.  # noqa: E501

        **API Key Scope**: task_options / show  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_task_option_with_http_info(task_id=task_id_value, task_option_id=task_option_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_option_id: Numeric ID of task option. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TaskOption, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['task_id', 'task_option_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_task_option" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `show_task_option`")  # noqa: E501
        # verify the required parameter 'task_option_id' is set
        if self.api_client.client_side_validation and ('task_option_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_option_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_option_id` when calling `show_task_option`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501
        if 'task_option_id' in local_var_params:
            path_params['task_option_id'] = local_var_params['task_option_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{task_id}/task_options/{task_option_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskOption',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_task_option(self, **kwargs):  # noqa: E501
        """Updates a specific task option.  # noqa: E501

        **API Key Scope**: task_options / update  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_task_option(task_id=task_id_value, task_option_id=task_option_id_value, task_option_body=task_option_body_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_option_id: Numeric ID of task option. (required)
        :param TaskOption task_option_body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TaskOption
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_task_option_with_http_info(**kwargs)  # noqa: E501

    def update_task_option_with_http_info(self, **kwargs):  # noqa: E501
        """Updates a specific task option.  # noqa: E501

        **API Key Scope**: task_options / update  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_task_option_with_http_info(task_id=task_id_value, task_option_id=task_option_id_value, task_option_body=task_option_body_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_option_id: Numeric ID of task option. (required)
        :param TaskOption task_option_body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TaskOption, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['task_id', 'task_option_id', 'task_option_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_task_option" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `update_task_option`")  # noqa: E501
        # verify the required parameter 'task_option_id' is set
        if self.api_client.client_side_validation and ('task_option_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_option_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_option_id` when calling `update_task_option`")  # noqa: E501
        # verify the required parameter 'task_option_body' is set
        if self.api_client.client_side_validation and ('task_option_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_option_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_option_body` when calling `update_task_option`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501
        if 'task_option_id' in local_var_params:
            path_params['task_option_id'] = local_var_params['task_option_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'task_option_body' in local_var_params:
            body_params = local_var_params['task_option_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{task_id}/task_options/{task_option_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskOption',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)