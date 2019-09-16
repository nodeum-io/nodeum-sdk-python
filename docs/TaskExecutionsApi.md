# swagger_client.TaskExecutionsApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_task_executions**](TaskExecutionsApi.md#index_task_executions) | **GET** /task_executions | Lists all task executions.
[**index_task_executions_by_task**](TaskExecutionsApi.md#index_task_executions_by_task) | **GET** /tasks/{task_id}/task_executions | Lists all task executions.
[**show_task_execution**](TaskExecutionsApi.md#show_task_execution) | **GET** /task_executions/{task_execution_id} | Displays a specific task execution.
[**show_task_execution_by_task**](TaskExecutionsApi.md#show_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id} | Displays a specific task execution.


# **index_task_executions**
> TaskExecutionCollection index_task_executions(limit=limit, offset=offset, sort_by=sort_by, id=id, task_id=task_id, name=name, type=type, status=status, log_time=log_time, job_started=job_started, job_finished=job_finished, to_process_size=to_process_size, processed_size=processed_size, to_process_files=to_process_files, processed_files=processed_files, finalized_files=finalized_files, estimation_time=estimation_time, bandwidth=bandwidth)

Lists all task executions.

**API Key Scope**: task_executions / index

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: BearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TaskExecutionsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
task_id = 'task_id_example' # str | Filter on task id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
status = 'status_example' # str | Filter on status (optional)
log_time = 'log_time_example' # str | Filter on log time (optional)
job_started = 'job_started_example' # str | Filter on job started (optional)
job_finished = 'job_finished_example' # str | Filter on job finished (optional)
to_process_size = 'to_process_size_example' # str | Filter on to process size (optional)
processed_size = 'processed_size_example' # str | Filter on processed size (optional)
to_process_files = 'to_process_files_example' # str | Filter on to process files (optional)
processed_files = 'processed_files_example' # str | Filter on processed files (optional)
finalized_files = 'finalized_files_example' # str | Filter on finalized files (optional)
estimation_time = 'estimation_time_example' # str | Filter on estimation time (optional)
bandwidth = 'bandwidth_example' # str | Filter on bandwidth (optional)

try:
    # Lists all task executions.
    api_response = api_instance.index_task_executions(limit=limit, offset=offset, sort_by=sort_by, id=id, task_id=task_id, name=name, type=type, status=status, log_time=log_time, job_started=job_started, job_finished=job_finished, to_process_size=to_process_size, processed_size=processed_size, to_process_files=to_process_files, processed_files=processed_files, finalized_files=finalized_files, estimation_time=estimation_time, bandwidth=bandwidth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskExecutionsApi->index_task_executions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **task_id** | **str**| Filter on task id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **status** | **str**| Filter on status | [optional] 
 **log_time** | **str**| Filter on log time | [optional] 
 **job_started** | **str**| Filter on job started | [optional] 
 **job_finished** | **str**| Filter on job finished | [optional] 
 **to_process_size** | **str**| Filter on to process size | [optional] 
 **processed_size** | **str**| Filter on processed size | [optional] 
 **to_process_files** | **str**| Filter on to process files | [optional] 
 **processed_files** | **str**| Filter on processed files | [optional] 
 **finalized_files** | **str**| Filter on finalized files | [optional] 
 **estimation_time** | **str**| Filter on estimation time | [optional] 
 **bandwidth** | **str**| Filter on bandwidth | [optional] 

### Return type

[**TaskExecutionCollection**](TaskExecutionCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_task_executions_by_task**
> TaskExecutionCollection index_task_executions_by_task(task_id)

Lists all task executions.

**API Key Scope**: task_executions / index

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: BearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TaskExecutionsApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.

try:
    # Lists all task executions.
    api_response = api_instance.index_task_executions_by_task(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskExecutionsApi->index_task_executions_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 

### Return type

[**TaskExecutionCollection**](TaskExecutionCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_task_execution**
> TaskExecution show_task_execution(task_execution_id)

Displays a specific task execution.

**API Key Scope**: task_executions / show

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: BearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TaskExecutionsApi(swagger_client.ApiClient(configuration))
task_execution_id = 789 # int | Numeric ID of task execution.

try:
    # Displays a specific task execution.
    api_response = api_instance.show_task_execution(task_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskExecutionsApi->show_task_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_execution_id** | **int**| Numeric ID of task execution. | 

### Return type

[**TaskExecution**](TaskExecution.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_task_execution_by_task**
> TaskExecution show_task_execution_by_task(task_id, task_execution_id)

Displays a specific task execution.

**API Key Scope**: task_executions / show

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: BearerAuth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TaskExecutionsApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 789 # int | Numeric ID of task execution.

try:
    # Displays a specific task execution.
    api_response = api_instance.show_task_execution_by_task(task_id, task_execution_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskExecutionsApi->show_task_execution_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_execution_id** | **int**| Numeric ID of task execution. | 

### Return type

[**TaskExecution**](TaskExecution.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

