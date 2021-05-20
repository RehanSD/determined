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


class TrialsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def determined_get_experiment_trials(self, experiment_id, **kwargs):  # noqa: E501
        """Get the list of trials for an experiment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_get_experiment_trials(experiment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int experiment_id: Limit trials to those that are owned by the specified experiments. (required)
        :param str sort_by: Sort trials by the given field.   - SORT_BY_UNSPECIFIED: Returns trials in an unsorted list.  - SORT_BY_ID: Returns trials sorted by id.  - SORT_BY_START_TIME: Return trials sorted by start time.  - SORT_BY_END_TIME: Return trials sorted by end time. Trials without end times are returned after trials that are.  - SORT_BY_STATE: Return trials sorted by state.  - SORT_BY_BEST_VALIDATION_METRIC: Return the trials sorted by the best metric so far, where the metric is specified by `searcher.metric` in the experiment configuration.  - SORT_BY_LATEST_VALIDATION_METRIC: Return the trials sorted by the latest metric so far, where the metric is specified by `searcher.metric` in the experiment configuration.  - SORT_BY_BATCHES_PROCESSED: Return the trials sorted by the number of batches completed.  - SORT_BY_DURATION: Return the trials sorted by the total duration.
        :param str order_by: Order trials in either ascending or descending order.   - ORDER_BY_UNSPECIFIED: Returns records in no specific order.  - ORDER_BY_ASC: Returns records in ascending order.  - ORDER_BY_DESC: Returns records in descending order.
        :param int offset: Skip the number of trials before returning results. Negative values denote number of trials to skip from the end before returning results.
        :param int limit: Limit the number of trials. A value of 0 denotes no limit.
        :param list[str] states: Limit trials to those that match the provided state.   - STATE_UNSPECIFIED: The state of the experiment is unknown.  - STATE_ACTIVE: The experiment is in an active state.  - STATE_PAUSED: The experiment is in a paused state  - STATE_STOPPING_COMPLETED: The experiment is completed and is shutting down.  - STATE_STOPPING_CANCELED: The experiment is canceled and is shutting down.  - STATE_STOPPING_ERROR: The experiment is errored and is shutting down.  - STATE_COMPLETED: The experiment is completed and is shut down.  - STATE_CANCELED: The experiment is canceled and is shut down.  - STATE_ERROR: The experiment is errored and is shut down.  - STATE_DELETED: The experiment has been deleted.
        :return: V1GetExperimentTrialsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.determined_get_experiment_trials_with_http_info(experiment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.determined_get_experiment_trials_with_http_info(experiment_id, **kwargs)  # noqa: E501
            return data

    def determined_get_experiment_trials_with_http_info(self, experiment_id, **kwargs):  # noqa: E501
        """Get the list of trials for an experiment.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_get_experiment_trials_with_http_info(experiment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int experiment_id: Limit trials to those that are owned by the specified experiments. (required)
        :param str sort_by: Sort trials by the given field.   - SORT_BY_UNSPECIFIED: Returns trials in an unsorted list.  - SORT_BY_ID: Returns trials sorted by id.  - SORT_BY_START_TIME: Return trials sorted by start time.  - SORT_BY_END_TIME: Return trials sorted by end time. Trials without end times are returned after trials that are.  - SORT_BY_STATE: Return trials sorted by state.  - SORT_BY_BEST_VALIDATION_METRIC: Return the trials sorted by the best metric so far, where the metric is specified by `searcher.metric` in the experiment configuration.  - SORT_BY_LATEST_VALIDATION_METRIC: Return the trials sorted by the latest metric so far, where the metric is specified by `searcher.metric` in the experiment configuration.  - SORT_BY_BATCHES_PROCESSED: Return the trials sorted by the number of batches completed.  - SORT_BY_DURATION: Return the trials sorted by the total duration.
        :param str order_by: Order trials in either ascending or descending order.   - ORDER_BY_UNSPECIFIED: Returns records in no specific order.  - ORDER_BY_ASC: Returns records in ascending order.  - ORDER_BY_DESC: Returns records in descending order.
        :param int offset: Skip the number of trials before returning results. Negative values denote number of trials to skip from the end before returning results.
        :param int limit: Limit the number of trials. A value of 0 denotes no limit.
        :param list[str] states: Limit trials to those that match the provided state.   - STATE_UNSPECIFIED: The state of the experiment is unknown.  - STATE_ACTIVE: The experiment is in an active state.  - STATE_PAUSED: The experiment is in a paused state  - STATE_STOPPING_COMPLETED: The experiment is completed and is shutting down.  - STATE_STOPPING_CANCELED: The experiment is canceled and is shutting down.  - STATE_STOPPING_ERROR: The experiment is errored and is shutting down.  - STATE_COMPLETED: The experiment is completed and is shut down.  - STATE_CANCELED: The experiment is canceled and is shut down.  - STATE_ERROR: The experiment is errored and is shut down.  - STATE_DELETED: The experiment has been deleted.
        :return: V1GetExperimentTrialsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['experiment_id', 'sort_by', 'order_by', 'offset', 'limit', 'states']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method determined_get_experiment_trials" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'experiment_id' is set
        if ('experiment_id' not in params or
                params['experiment_id'] is None):
            raise ValueError("Missing the required parameter `experiment_id` when calling `determined_get_experiment_trials`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'experiment_id' in params:
            path_params['experimentId'] = params['experiment_id']  # noqa: E501

        query_params = []
        if 'sort_by' in params:
            query_params.append(('sortBy', params['sort_by']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'states' in params:
            query_params.append(('states', params['states']))  # noqa: E501
            collection_formats['states'] = 'multi'  # noqa: E501

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
            '/api/v1/experiments/{experimentId}/trials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1GetExperimentTrialsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def determined_get_trial(self, trial_id, **kwargs):  # noqa: E501
        """Get a single trial.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_get_trial(trial_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trial_id: The requested trial's id. (required)
        :return: V1GetTrialResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.determined_get_trial_with_http_info(trial_id, **kwargs)  # noqa: E501
        else:
            (data) = self.determined_get_trial_with_http_info(trial_id, **kwargs)  # noqa: E501
            return data

    def determined_get_trial_with_http_info(self, trial_id, **kwargs):  # noqa: E501
        """Get a single trial.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_get_trial_with_http_info(trial_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trial_id: The requested trial's id. (required)
        :return: V1GetTrialResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trial_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method determined_get_trial" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trial_id' is set
        if ('trial_id' not in params or
                params['trial_id'] is None):
            raise ValueError("Missing the required parameter `trial_id` when calling `determined_get_trial`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trial_id' in params:
            path_params['trialId'] = params['trial_id']  # noqa: E501

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
            '/api/v1/trials/{trialId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1GetTrialResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def determined_kill_trial(self, id, **kwargs):  # noqa: E501
        """Kill a trial.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_kill_trial(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The trial id (required)
        :return: V1KillTrialResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.determined_kill_trial_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.determined_kill_trial_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def determined_kill_trial_with_http_info(self, id, **kwargs):  # noqa: E501
        """Kill a trial.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_kill_trial_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The trial id (required)
        :return: V1KillTrialResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method determined_kill_trial" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `determined_kill_trial`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

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
            '/api/v1/trials/{id}/kill', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='V1KillTrialResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def determined_trial_logs(self, trial_id, **kwargs):  # noqa: E501
        """Stream trial logs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_trial_logs(trial_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trial_id: The id of the trial. (required)
        :param int limit: Limit the number of trial logs. A value of 0 denotes no limit.
        :param bool follow: Continue following logs until the trial stops.
        :param list[str] agent_ids: Limit the trial logs to a subset of agents.
        :param list[str] container_ids: Limit the trial logs to a subset of containers.
        :param list[int] rank_ids: Limit the trial logs to a subset of ranks.
        :param list[str] levels: Limit the trial logs to a subset of agents.   - LOG_LEVEL_UNSPECIFIED: Unspecified log level.  - LOG_LEVEL_TRACE: A log level of TRACE.  - LOG_LEVEL_DEBUG: A log level of DEBUG.  - LOG_LEVEL_INFO: A log level of INFO.  - LOG_LEVEL_WARNING: A log level of WARNING.  - LOG_LEVEL_ERROR: A log level of ERROR.  - LOG_LEVEL_CRITICAL: A log level of CRITICAL.
        :param list[str] stdtypes: Limit the trial logs to a subset of output streams.
        :param list[str] sources: Limit the trial logs to a subset of sources.
        :param datetime timestamp_before: Limit the trial logs to ones with a timestamp before a given time.
        :param datetime timestamp_after: Limit the trial logs to ones with a timestamp after a given time.
        :param str order_by: Order logs in either ascending or descending order by timestamp.   - ORDER_BY_UNSPECIFIED: Returns records in no specific order.  - ORDER_BY_ASC: Returns records in ascending order.  - ORDER_BY_DESC: Returns records in descending order.
        :return: StreamResultOfV1TrialLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.determined_trial_logs_with_http_info(trial_id, **kwargs)  # noqa: E501
        else:
            (data) = self.determined_trial_logs_with_http_info(trial_id, **kwargs)  # noqa: E501
            return data

    def determined_trial_logs_with_http_info(self, trial_id, **kwargs):  # noqa: E501
        """Stream trial logs.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_trial_logs_with_http_info(trial_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trial_id: The id of the trial. (required)
        :param int limit: Limit the number of trial logs. A value of 0 denotes no limit.
        :param bool follow: Continue following logs until the trial stops.
        :param list[str] agent_ids: Limit the trial logs to a subset of agents.
        :param list[str] container_ids: Limit the trial logs to a subset of containers.
        :param list[int] rank_ids: Limit the trial logs to a subset of ranks.
        :param list[str] levels: Limit the trial logs to a subset of agents.   - LOG_LEVEL_UNSPECIFIED: Unspecified log level.  - LOG_LEVEL_TRACE: A log level of TRACE.  - LOG_LEVEL_DEBUG: A log level of DEBUG.  - LOG_LEVEL_INFO: A log level of INFO.  - LOG_LEVEL_WARNING: A log level of WARNING.  - LOG_LEVEL_ERROR: A log level of ERROR.  - LOG_LEVEL_CRITICAL: A log level of CRITICAL.
        :param list[str] stdtypes: Limit the trial logs to a subset of output streams.
        :param list[str] sources: Limit the trial logs to a subset of sources.
        :param datetime timestamp_before: Limit the trial logs to ones with a timestamp before a given time.
        :param datetime timestamp_after: Limit the trial logs to ones with a timestamp after a given time.
        :param str order_by: Order logs in either ascending or descending order by timestamp.   - ORDER_BY_UNSPECIFIED: Returns records in no specific order.  - ORDER_BY_ASC: Returns records in ascending order.  - ORDER_BY_DESC: Returns records in descending order.
        :return: StreamResultOfV1TrialLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trial_id', 'limit', 'follow', 'agent_ids', 'container_ids', 'rank_ids', 'levels', 'stdtypes', 'sources', 'timestamp_before', 'timestamp_after', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method determined_trial_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trial_id' is set
        if ('trial_id' not in params or
                params['trial_id'] is None):
            raise ValueError("Missing the required parameter `trial_id` when calling `determined_trial_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trial_id' in params:
            path_params['trialId'] = params['trial_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'follow' in params:
            query_params.append(('follow', params['follow']))  # noqa: E501
        if 'agent_ids' in params:
            query_params.append(('agentIds', params['agent_ids']))  # noqa: E501
            collection_formats['agentIds'] = 'multi'  # noqa: E501
        if 'container_ids' in params:
            query_params.append(('containerIds', params['container_ids']))  # noqa: E501
            collection_formats['containerIds'] = 'multi'  # noqa: E501
        if 'rank_ids' in params:
            query_params.append(('rankIds', params['rank_ids']))  # noqa: E501
            collection_formats['rankIds'] = 'multi'  # noqa: E501
        if 'levels' in params:
            query_params.append(('levels', params['levels']))  # noqa: E501
            collection_formats['levels'] = 'multi'  # noqa: E501
        if 'stdtypes' in params:
            query_params.append(('stdtypes', params['stdtypes']))  # noqa: E501
            collection_formats['stdtypes'] = 'multi'  # noqa: E501
        if 'sources' in params:
            query_params.append(('sources', params['sources']))  # noqa: E501
            collection_formats['sources'] = 'multi'  # noqa: E501
        if 'timestamp_before' in params:
            query_params.append(('timestampBefore', params['timestamp_before']))  # noqa: E501
        if 'timestamp_after' in params:
            query_params.append(('timestampAfter', params['timestamp_after']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501

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
            '/api/v1/trials/{trialId}/logs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamResultOfV1TrialLogsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def determined_trial_logs_fields(self, trial_id, **kwargs):  # noqa: E501
        """Stream trial log fields.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_trial_logs_fields(trial_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trial_id: The ID of the trial. (required)
        :param bool follow: Continue following fields until the trial stops.
        :return: StreamResultOfV1TrialLogsFieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.determined_trial_logs_fields_with_http_info(trial_id, **kwargs)  # noqa: E501
        else:
            (data) = self.determined_trial_logs_fields_with_http_info(trial_id, **kwargs)  # noqa: E501
            return data

    def determined_trial_logs_fields_with_http_info(self, trial_id, **kwargs):  # noqa: E501
        """Stream trial log fields.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.determined_trial_logs_fields_with_http_info(trial_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int trial_id: The ID of the trial. (required)
        :param bool follow: Continue following fields until the trial stops.
        :return: StreamResultOfV1TrialLogsFieldsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['trial_id', 'follow']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method determined_trial_logs_fields" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'trial_id' is set
        if ('trial_id' not in params or
                params['trial_id'] is None):
            raise ValueError("Missing the required parameter `trial_id` when calling `determined_trial_logs_fields`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'trial_id' in params:
            path_params['trialId'] = params['trial_id']  # noqa: E501

        query_params = []
        if 'follow' in params:
            query_params.append(('follow', params['follow']))  # noqa: E501

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
            '/api/v1/trials/{trialId}/logs/fields', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamResultOfV1TrialLogsFieldsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
