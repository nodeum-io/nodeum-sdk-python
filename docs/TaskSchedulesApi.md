# nodeum_sdk.TaskSchedulesApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_schedule**](TaskSchedulesApi.md#create_task_schedule) | **POST** /tasks/{task_id}/task_schedule | Creates a new task schedule. Only one should be created.
[**destroy_task_schedule**](TaskSchedulesApi.md#destroy_task_schedule) | **DELETE** /tasks/{task_id}/task_schedule | Destroys the task schedule.
[**index_task_schedules**](TaskSchedulesApi.md#index_task_schedules) | **GET** /task_schedules | Lists all task schedules.
[**show_task_schedule**](TaskSchedulesApi.md#show_task_schedule) | **GET** /tasks/{task_id}/task_schedule | Displays the task schedule.
[**update_task_schedule**](TaskSchedulesApi.md#update_task_schedule) | **PUT** /tasks/{task_id}/task_schedule | Updates the existing task schedule.


# **create_task_schedule**
> TaskSchedule create_task_schedule(task_id, task_schedule_body)

Creates a new task schedule. Only one should be created.

**API Key Scope**: task_schedules / create

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_schedule_body = nodeum_sdk.TaskSchedule() # TaskSchedule | 

    try:
        # Creates a new task schedule. Only one should be created.
        api_response = api_instance.create_task_schedule(task_id, task_schedule_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->create_task_schedule: %s\n" % e)
```

* Api Key Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_schedule_body = nodeum_sdk.TaskSchedule() # TaskSchedule | 

    try:
        # Creates a new task schedule. Only one should be created.
        api_response = api_instance.create_task_schedule(task_id, task_schedule_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->create_task_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_schedule_body** | [**TaskSchedule**](TaskSchedule.md)|  | 

### Return type

[**TaskSchedule**](TaskSchedule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific task schedule. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_task_schedule**
> destroy_task_schedule(task_id)

Destroys the task schedule.

**API Key Scope**: task_schedules / destroy

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.

    try:
        # Destroys the task schedule.
        api_instance.destroy_task_schedule(task_id)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->destroy_task_schedule: %s\n" % e)
```

* Api Key Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.

    try:
        # Destroys the task schedule.
        api_instance.destroy_task_schedule(task_id)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->destroy_task_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Task schedule destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_task_schedules**
> TaskScheduleCollection index_task_schedules(with_next=with_next, limit=limit, offset=offset, sort_by=sort_by, id=id, rrule=rrule, done=done, task_id=task_id)

Lists all task schedules.

**API Key Scope**: task_schedules / index

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    with_next = True # bool | Display the next scheduled date, and information about missing executions. (optional) (default to True)
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
rrule = 'rrule_example' # str | Filter on RRule of schedule (optional)
done = 'done_example' # str | Filter on done schedule (optional)
task_id = 'task_id_example' # str | Filter on task id (optional)

    try:
        # Lists all task schedules.
        api_response = api_instance.index_task_schedules(with_next=with_next, limit=limit, offset=offset, sort_by=sort_by, id=id, rrule=rrule, done=done, task_id=task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->index_task_schedules: %s\n" % e)
```

* Api Key Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    with_next = True # bool | Display the next scheduled date, and information about missing executions. (optional) (default to True)
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
rrule = 'rrule_example' # str | Filter on RRule of schedule (optional)
done = 'done_example' # str | Filter on done schedule (optional)
task_id = 'task_id_example' # str | Filter on task id (optional)

    try:
        # Lists all task schedules.
        api_response = api_instance.index_task_schedules(with_next=with_next, limit=limit, offset=offset, sort_by=sort_by, id=id, rrule=rrule, done=done, task_id=task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->index_task_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_next** | **bool**| Display the next scheduled date, and information about missing executions. | [optional] [default to True]
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **rrule** | **str**| Filter on RRule of schedule | [optional] 
 **done** | **str**| Filter on done schedule | [optional] 
 **task_id** | **str**| Filter on task id | [optional] 

### Return type

[**TaskScheduleCollection**](TaskScheduleCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of task schedules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_task_schedule**
> TaskSchedule show_task_schedule(task_id)

Displays the task schedule.

**API Key Scope**: task_schedules / show

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.

    try:
        # Displays the task schedule.
        api_response = api_instance.show_task_schedule(task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->show_task_schedule: %s\n" % e)
```

* Api Key Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.

    try:
        # Displays the task schedule.
        api_response = api_instance.show_task_schedule(task_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->show_task_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 

### Return type

[**TaskSchedule**](TaskSchedule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific task schedule. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_schedule**
> TaskSchedule update_task_schedule(task_id, task_schedule_body)

Updates the existing task schedule.

**API Key Scope**: task_schedules / update

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_schedule_body = nodeum_sdk.TaskSchedule() # TaskSchedule | 

    try:
        # Updates the existing task schedule.
        api_response = api_instance.update_task_schedule(task_id, task_schedule_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->update_task_schedule: %s\n" % e)
```

* Api Key Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import nodeum_sdk
from nodeum_sdk.rest import ApiException
from pprint import pprint
configuration = nodeum_sdk.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
configuration = nodeum_sdk.Configuration()
# Configure API key authorization: BearerAuth
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost/api/v2
configuration.host = "http://localhost/api/v2"

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.TaskSchedulesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_schedule_body = nodeum_sdk.TaskSchedule() # TaskSchedule | 

    try:
        # Updates the existing task schedule.
        api_response = api_instance.update_task_schedule(task_id, task_schedule_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaskSchedulesApi->update_task_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_schedule_body** | [**TaskSchedule**](TaskSchedule.md)|  | 

### Return type

[**TaskSchedule**](TaskSchedule.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific task schedule. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

