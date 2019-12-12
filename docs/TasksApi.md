# nodeum_sdk.TasksApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /tasks | Creates a new task.
[**destroy_task**](TasksApi.md#destroy_task) | **DELETE** /tasks/{task_id} | Destroys a specific task.
[**index_tasks**](TasksApi.md#index_tasks) | **GET** /tasks | Lists all tasks.
[**show_task**](TasksApi.md#show_task) | **GET** /tasks/{task_id} | Displays a specific task.
[**update_task**](TasksApi.md#update_task) | **PUT** /tasks/{task_id} | Updates a specific task.


# **create_task**
> Task create_task(task_body)

Creates a new task.

**API Key Scope**: tasks / create

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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
task_body = nodeum_sdk.Task() # Task | 

try:
    # Creates a new task.
    api_response = api_instance.create_task(task_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
task_body = nodeum_sdk.Task() # Task | 

try:
    # Creates a new task.
    api_response = api_instance.create_task(task_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_body** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific task. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_task**
> destroy_task(task_id)

Destroys a specific task.

**API Key Scope**: tasks / destroy

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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.

try:
    # Destroys a specific task.
    api_instance.destroy_task(task_id)
except ApiException as e:
    print("Exception when calling TasksApi->destroy_task: %s\n" % e)
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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.

try:
    # Destroys a specific task.
    api_instance.destroy_task(task_id)
except ApiException as e:
    print("Exception when calling TasksApi->destroy_task: %s\n" % e)
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
**204** | Task destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tasks**
> TaskCollection index_tasks(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type, priority=priority, conflict_resolution=conflict_resolution, action=action, activate=activate, creation_date=creation_date, creation_username=creation_username, modification_date=modification_date, modification_username=modification_username, job_started=job_started, job_finished=job_finished, status=status, processed_size=processed_size, to_process_size=to_process_size)

Lists all tasks.

**API Key Scope**: tasks / index

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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
comment = 'comment_example' # str | Filter on comment (optional)
type = 'type_example' # str | Filter on type (optional)
priority = 'priority_example' # str | Filter on priority (optional)
conflict_resolution = 'conflict_resolution_example' # str | Filter on conflict resolution (optional)
action = 'action_example' # str | Filter on action (optional)
activate = 'activate_example' # str | Filter on activate (optional)
creation_date = 'creation_date_example' # str | Filter on creation date (optional)
creation_username = 'creation_username_example' # str | Filter on creation username (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
modification_username = 'modification_username_example' # str | Filter on modification username (optional)
job_started = 'job_started_example' # str | Filter on job started (optional)
job_finished = 'job_finished_example' # str | Filter on job finished (optional)
status = 'status_example' # str | Filter on status (optional)
processed_size = 'processed_size_example' # str | Filter on processed size (optional)
to_process_size = 'to_process_size_example' # str | Filter on to process size (optional)

try:
    # Lists all tasks.
    api_response = api_instance.index_tasks(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type, priority=priority, conflict_resolution=conflict_resolution, action=action, activate=activate, creation_date=creation_date, creation_username=creation_username, modification_date=modification_date, modification_username=modification_username, job_started=job_started, job_finished=job_finished, status=status, processed_size=processed_size, to_process_size=to_process_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->index_tasks: %s\n" % e)
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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
comment = 'comment_example' # str | Filter on comment (optional)
type = 'type_example' # str | Filter on type (optional)
priority = 'priority_example' # str | Filter on priority (optional)
conflict_resolution = 'conflict_resolution_example' # str | Filter on conflict resolution (optional)
action = 'action_example' # str | Filter on action (optional)
activate = 'activate_example' # str | Filter on activate (optional)
creation_date = 'creation_date_example' # str | Filter on creation date (optional)
creation_username = 'creation_username_example' # str | Filter on creation username (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
modification_username = 'modification_username_example' # str | Filter on modification username (optional)
job_started = 'job_started_example' # str | Filter on job started (optional)
job_finished = 'job_finished_example' # str | Filter on job finished (optional)
status = 'status_example' # str | Filter on status (optional)
processed_size = 'processed_size_example' # str | Filter on processed size (optional)
to_process_size = 'to_process_size_example' # str | Filter on to process size (optional)

try:
    # Lists all tasks.
    api_response = api_instance.index_tasks(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type, priority=priority, conflict_resolution=conflict_resolution, action=action, activate=activate, creation_date=creation_date, creation_username=creation_username, modification_date=modification_date, modification_username=modification_username, job_started=job_started, job_finished=job_finished, status=status, processed_size=processed_size, to_process_size=to_process_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->index_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **comment** | **str**| Filter on comment | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **priority** | **str**| Filter on priority | [optional] 
 **conflict_resolution** | **str**| Filter on conflict resolution | [optional] 
 **action** | **str**| Filter on action | [optional] 
 **activate** | **str**| Filter on activate | [optional] 
 **creation_date** | **str**| Filter on creation date | [optional] 
 **creation_username** | **str**| Filter on creation username | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **modification_username** | **str**| Filter on modification username | [optional] 
 **job_started** | **str**| Filter on job started | [optional] 
 **job_finished** | **str**| Filter on job finished | [optional] 
 **status** | **str**| Filter on status | [optional] 
 **processed_size** | **str**| Filter on processed size | [optional] 
 **to_process_size** | **str**| Filter on to process size | [optional] 

### Return type

[**TaskCollection**](TaskCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tasks. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_task**
> Task show_task(task_id)

Displays a specific task.

**API Key Scope**: tasks / show

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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.

try:
    # Displays a specific task.
    api_response = api_instance.show_task(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->show_task: %s\n" % e)
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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.

try:
    # Displays a specific task.
    api_response = api_instance.show_task(task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->show_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 

### Return type

[**Task**](Task.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific task. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> Task update_task(task_id, task_body)

Updates a specific task.

**API Key Scope**: tasks / update

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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_body = nodeum_sdk.Task() # Task | 

try:
    # Updates a specific task.
    api_response = api_instance.update_task(task_id, task_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)
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
# Create an instance of the API class
api_instance = nodeum_sdk.TasksApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_body = nodeum_sdk.Task() # Task | 

try:
    # Updates a specific task.
    api_response = api_instance.update_task(task_id, task_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_body** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific task. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

