# coding: utf-8

"""
    Nodeum API

    The Nodeum API makes it easy to tap into the digital data mesh that runs across your organisation. Make requests to our API endpoints and we’ll give you everything you need to interconnect your business workflows with your storage.  All production API requests are made to:  http://nodeumhostname/api/  The current production version of the API is v1.   **REST** The Nodeum API is a RESTful API. This means that the API is designed to allow you to get, create, update, & delete objects with the HTTP verbs GET, POST, PUT, PATCH, & DELETE.  **JSON** The Nodeum API speaks exclusively in JSON. This means that you should always set the Content-Type header to application/json to ensure that your requests are properly accepted and processed by the API.  **Authentication** All API calls require user-password authentication.   **Cross-Origin Resource Sharing** The Nodeum API supports CORS for communicating from Javascript for these endpoints. You will need to specify an Origin URI when creating your application to allow for CORS to be whitelisted for your domain.   **Pagination** Some endpoints such as File Listing return a potentially lengthy array of objects. In order to keep the response sizes manageable the API will take advantage of pagination. Pagination is a mechanism for returning a subset of the results for a request and allowing for subsequent requests to “page” through the rest of the results until the end is reached. Paginated endpoints follow a standard interface that accepts two query parameters, limit and offset, and return a payload that follows a standard form. These parameters names and their behavior are borrowed from SQL LIMIT and OFFSET keywords.  **Versioning** The Nodeum API is constantly being worked on to add features, make improvements, and fix bugs. This means that you should expect changes to be introduced and documented.   However, there are some changes or additions that are considered backwards-compatible and your applications should be flexible enough to handle them. These include:  - Adding new endpoints to the API - Adding new attributes to the response of an existing endpoint - Changing the order of attributes of responses (JSON by definition is an object of unordered key/value pairs)  **Filter parameters** When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)    # noqa: E501

    The version of the OpenAPI document: 2.1.0
    Contact: info@nodeum.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from nodeum_sdk.api_client import ApiClient
from nodeum_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class TaskDestinationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_task_destination(self, **kwargs):  # noqa: E501
        """Creates a new task destination.  # noqa: E501

        **API Key Scope**: task_destinations / create  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_task_destination(task_id=task_id_value, task_destination_body=task_destination_body_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param TaskDestinationUp task_destination_body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TaskDestinationDown
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_task_destination_with_http_info(**kwargs)  # noqa: E501

    def create_task_destination_with_http_info(self, **kwargs):  # noqa: E501
        """Creates a new task destination.  # noqa: E501

        **API Key Scope**: task_destinations / create  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_task_destination_with_http_info(task_id=task_id_value, task_destination_body=task_destination_body_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param TaskDestinationUp task_destination_body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TaskDestinationDown, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'task_id',
            'task_destination_body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_task_destination" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `create_task_destination`")  # noqa: E501
        # verify the required parameter 'task_destination_body' is set
        if self.api_client.client_side_validation and ('task_destination_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_destination_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_destination_body` when calling `create_task_destination`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'task_destination_body' in local_var_params:
            body_params = local_var_params['task_destination_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{task_id}/task_destinations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskDestinationDown',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def destroy_task_destination(self, **kwargs):  # noqa: E501
        """Destroys a specific task destination.  # noqa: E501

        **API Key Scope**: task_destinations / destroy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_task_destination(task_id=task_id_value, task_destination_id=task_destination_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_destination_id: Numeric ID of task destination. (required)
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
        return self.destroy_task_destination_with_http_info(**kwargs)  # noqa: E501

    def destroy_task_destination_with_http_info(self, **kwargs):  # noqa: E501
        """Destroys a specific task destination.  # noqa: E501

        **API Key Scope**: task_destinations / destroy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.destroy_task_destination_with_http_info(task_id=task_id_value, task_destination_id=task_destination_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_destination_id: Numeric ID of task destination. (required)
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

        all_params = [
            'task_id',
            'task_destination_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method destroy_task_destination" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `destroy_task_destination`")  # noqa: E501
        # verify the required parameter 'task_destination_id' is set
        if self.api_client.client_side_validation and ('task_destination_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_destination_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_destination_id` when calling `destroy_task_destination`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501
        if 'task_destination_id' in local_var_params:
            path_params['task_destination_id'] = local_var_params['task_destination_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{task_id}/task_destinations/{task_destination_id}', 'DELETE',
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

    def index_task_destinations(self, **kwargs):  # noqa: E501
        """Lists all task destinations.  # noqa: E501

        **API Key Scope**: task_destinations / index  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_task_destinations(task_id=task_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int limit: The number of items to display for pagination.
        :param int offset: The number of items to skip for pagination.
        :param list[str] sort_by: Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`.
        :param str id: Filter on id
        :param str folder_id: Filter on folder id
        :param str tape_id: Filter on tape id
        :param str pool_id: Filter on a pool id
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TaskDestinationCollection
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.index_task_destinations_with_http_info(**kwargs)  # noqa: E501

    def index_task_destinations_with_http_info(self, **kwargs):  # noqa: E501
        """Lists all task destinations.  # noqa: E501

        **API Key Scope**: task_destinations / index  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.index_task_destinations_with_http_info(task_id=task_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int limit: The number of items to display for pagination.
        :param int offset: The number of items to skip for pagination.
        :param list[str] sort_by: Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`.
        :param str id: Filter on id
        :param str folder_id: Filter on folder id
        :param str tape_id: Filter on tape id
        :param str pool_id: Filter on a pool id
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TaskDestinationCollection, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'task_id',
            'limit',
            'offset',
            'sort_by',
            'id',
            'folder_id',
            'tape_id',
            'pool_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method index_task_destinations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `index_task_destinations`")  # noqa: E501

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
        if 'folder_id' in local_var_params and local_var_params['folder_id'] is not None:  # noqa: E501
            query_params.append(('folder_id', local_var_params['folder_id']))  # noqa: E501
        if 'tape_id' in local_var_params and local_var_params['tape_id'] is not None:  # noqa: E501
            query_params.append(('tape_id', local_var_params['tape_id']))  # noqa: E501
        if 'pool_id' in local_var_params and local_var_params['pool_id'] is not None:  # noqa: E501
            query_params.append(('pool_id', local_var_params['pool_id']))  # noqa: E501

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
            '/tasks/{task_id}/task_destinations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskDestinationCollection',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def show_task_destination(self, **kwargs):  # noqa: E501
        """Displays a specific task destination.  # noqa: E501

        **API Key Scope**: task_destinations / show  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_task_destination(task_id=task_id_value, task_destination_id=task_destination_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_destination_id: Numeric ID of task destination. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TaskDestinationDown
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.show_task_destination_with_http_info(**kwargs)  # noqa: E501

    def show_task_destination_with_http_info(self, **kwargs):  # noqa: E501
        """Displays a specific task destination.  # noqa: E501

        **API Key Scope**: task_destinations / show  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_task_destination_with_http_info(task_id=task_id_value, task_destination_id=task_destination_id_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_destination_id: Numeric ID of task destination. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TaskDestinationDown, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'task_id',
            'task_destination_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_task_destination" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `show_task_destination`")  # noqa: E501
        # verify the required parameter 'task_destination_id' is set
        if self.api_client.client_side_validation and ('task_destination_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_destination_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_destination_id` when calling `show_task_destination`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501
        if 'task_destination_id' in local_var_params:
            path_params['task_destination_id'] = local_var_params['task_destination_id']  # noqa: E501

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
            '/tasks/{task_id}/task_destinations/{task_destination_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskDestinationDown',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_task_destination(self, **kwargs):  # noqa: E501
        """Updates a specific task destination.  # noqa: E501

        **API Key Scope**: task_destinations / update  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_task_destination(task_id=task_id_value, task_destination_id=task_destination_id_value, task_destination_body=task_destination_body_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_destination_id: Numeric ID of task destination. (required)
        :param TaskDestinationUp task_destination_body: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TaskDestinationDown
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_task_destination_with_http_info(**kwargs)  # noqa: E501

    def update_task_destination_with_http_info(self, **kwargs):  # noqa: E501
        """Updates a specific task destination.  # noqa: E501

        **API Key Scope**: task_destinations / update  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_task_destination_with_http_info(task_id=task_id_value, task_destination_id=task_destination_id_value, task_destination_body=task_destination_body_value, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str task_id: Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID. (required)
        :param int task_destination_id: Numeric ID of task destination. (required)
        :param TaskDestinationUp task_destination_body: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TaskDestinationDown, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'task_id',
            'task_destination_id',
            'task_destination_body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_task_destination" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_id' is set
        if self.api_client.client_side_validation and ('task_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_id` when calling `update_task_destination`")  # noqa: E501
        # verify the required parameter 'task_destination_id' is set
        if self.api_client.client_side_validation and ('task_destination_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_destination_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_destination_id` when calling `update_task_destination`")  # noqa: E501
        # verify the required parameter 'task_destination_body' is set
        if self.api_client.client_side_validation and ('task_destination_body' not in local_var_params or  # noqa: E501
                                                        local_var_params['task_destination_body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `task_destination_body` when calling `update_task_destination`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']  # noqa: E501
        if 'task_destination_id' in local_var_params:
            path_params['task_destination_id'] = local_var_params['task_destination_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'task_destination_body' in local_var_params:
            body_params = local_var_params['task_destination_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth', 'BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{task_id}/task_destinations/{task_destination_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskDestinationDown',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
