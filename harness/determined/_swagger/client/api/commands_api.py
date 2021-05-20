# coding: utf-8

"""
    Determined API (Beta)

    Determined helps deep learning teams train models more quickly, easily share GPU resources, and effectively collaborate. Determined allows deep learning engineers to focus on building and training models at scale, without needing to worry about DevOps or writing custom code for common tasks like fault tolerance or experiment tracking.  You can think of Determined as a platform that bridges the gap between tools like TensorFlow and PyTorch --- which work great for a single researcher with a single GPU --- to the challenges that arise when doing deep learning at scale, as teams, clusters, and data sets all increase in size.  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: community@determined.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from determined._swagger.client.api_client import ApiClient


class CommandsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def determined_get_command(self, command_id, **kwargs):  # noqa: E501
        """Get the requested command.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_get_command(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: The id of the command. (required)
        :return: V1GetCommandResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.determined_get_command_with_http_info(command_id, **kwargs)  # noqa: E501
        else:
            (data) = self.determined_get_command_with_http_info(command_id, **kwargs)  # noqa: E501
            return data

    def determined_get_command_with_http_info(self, command_id, **kwargs):  # noqa: E501
        """Get the requested command.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_get_command_with_http_info(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: The id of the command. (required)
        :return: V1GetCommandResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method determined_get_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params or
                params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `determined_get_command`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['commandId'] = params['command_id']  # noqa: E501

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
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/commands/{commandId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1GetCommandResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def determined_get_commands(self, **kwargs):  # noqa: E501
        """Get a list of commands.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_get_commands(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort_by: Sort commands by the given field.   - SORT_BY_UNSPECIFIED: Returns commands in an unsorted list.  - SORT_BY_ID: Returns commands sorted by id.  - SORT_BY_DESCRIPTION: Returns commands sorted by description.  - SORT_BY_START_TIME: Return commands sorted by start time.
        :param str order_by: Order commands in either ascending or descending order.   - ORDER_BY_UNSPECIFIED: Returns records in no specific order.  - ORDER_BY_ASC: Returns records in ascending order.  - ORDER_BY_DESC: Returns records in descending order.
        :param int offset: Skip the number of commands before returning results. Negative values denote number of commands to skip from the end before returning results.
        :param int limit: Limit the number of commands. A value of 0 denotes no limit.
        :param list[str] users: Limit commands to those that are owned by the specified users.
        :return: V1GetCommandsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.determined_get_commands_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.determined_get_commands_with_http_info(**kwargs)  # noqa: E501
            return data

    def determined_get_commands_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of commands.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_get_commands_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort_by: Sort commands by the given field.   - SORT_BY_UNSPECIFIED: Returns commands in an unsorted list.  - SORT_BY_ID: Returns commands sorted by id.  - SORT_BY_DESCRIPTION: Returns commands sorted by description.  - SORT_BY_START_TIME: Return commands sorted by start time.
        :param str order_by: Order commands in either ascending or descending order.   - ORDER_BY_UNSPECIFIED: Returns records in no specific order.  - ORDER_BY_ASC: Returns records in ascending order.  - ORDER_BY_DESC: Returns records in descending order.
        :param int offset: Skip the number of commands before returning results. Negative values denote number of commands to skip from the end before returning results.
        :param int limit: Limit the number of commands. A value of 0 denotes no limit.
        :param list[str] users: Limit commands to those that are owned by the specified users.
        :return: V1GetCommandsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort_by', 'order_by', 'offset', 'limit', 'users']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method determined_get_commands" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'users' in params:
            query_params.append(('users', params['users']))  # noqa: E501
            collection_formats['users'] = 'multi'  # noqa: E501

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
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/commands', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1GetCommandsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def determined_kill_command(self, command_id, **kwargs):  # noqa: E501
        """Kill the requested command.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_kill_command(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: The id of the command. (required)
        :return: V1KillCommandResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.determined_kill_command_with_http_info(command_id, **kwargs)  # noqa: E501
        else:
            (data) = self.determined_kill_command_with_http_info(command_id, **kwargs)  # noqa: E501
            return data

    def determined_kill_command_with_http_info(self, command_id, **kwargs):  # noqa: E501
        """Kill the requested command.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_kill_command_with_http_info(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: The id of the command. (required)
        :return: V1KillCommandResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method determined_kill_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params or
                params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `determined_kill_command`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['commandId'] = params['command_id']  # noqa: E501

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
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/commands/{commandId}/kill', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1KillCommandResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def determined_launch_command(self, body, **kwargs):  # noqa: E501
        """Launch a command.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_launch_command(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1LaunchCommandRequest body: (required)
        :return: V1LaunchCommandResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.determined_launch_command_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.determined_launch_command_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def determined_launch_command_with_http_info(self, body, **kwargs):  # noqa: E501
        """Launch a command.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_launch_command_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param V1LaunchCommandRequest body: (required)
        :return: V1LaunchCommandResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method determined_launch_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `determined_launch_command`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/commands', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1LaunchCommandResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
