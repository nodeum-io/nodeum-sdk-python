# nodeum_sdk.TaskSourcesApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_source**](TaskSourcesApi.md#create_task_source) | **POST** /tasks/{task_id}/task_sources | Creates a new task source.
[**destroy_task_source**](TaskSourcesApi.md#destroy_task_source) | **DELETE** /tasks/{task_id}/task_sources/{task_source_id} | Destroys a specific task source.
[**index_task_sources**](TaskSourcesApi.md#index_task_sources) | **GET** /tasks/{task_id}/task_sources | Lists all task sources.
[**show_task_source**](TaskSourcesApi.md#show_task_source) | **GET** /tasks/{task_id}/task_sources/{task_source_id} | Displays a specific task source.
[**update_task_source**](TaskSourcesApi.md#update_task_source) | **PUT** /tasks/{task_id}/task_sources/{task_source_id} | Updates a specific task source.


# **create_task_source**
> TaskSourceDown create_task_source(task_id, task_source_body)

Creates a new task source.

**API Key Scope**: task_sources / create

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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_body = nodeum_sdk.TaskSourceUp() # TaskSourceUp | 

try:
    # Creates a new task source.
    api_response = api_instance.create_task_source(task_id, task_source_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->create_task_source: %s\n" % e)
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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_body = nodeum_sdk.TaskSourceUp() # TaskSourceUp | 

try:
    # Creates a new task source.
    api_response = api_instance.create_task_source(task_id, task_source_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->create_task_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_source_body** | [**TaskSourceUp**](TaskSourceUp.md)|  | 

### Return type

[**TaskSourceDown**](TaskSourceDown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific task source. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_task_source**
> destroy_task_source(task_id, task_source_id)

Destroys a specific task source.

**API Key Scope**: task_sources / destroy

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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_id = 56 # int | Numeric ID of task source.

try:
    # Destroys a specific task source.
    api_instance.destroy_task_source(task_id, task_source_id)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->destroy_task_source: %s\n" % e)
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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_id = 56 # int | Numeric ID of task source.

try:
    # Destroys a specific task source.
    api_instance.destroy_task_source(task_id, task_source_id)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->destroy_task_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_source_id** | **int**| Numeric ID of task source. | 

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
**204** | Task source destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_task_sources**
> TaskSourceCollection index_task_sources(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, file_id=file_id, import_file_id=import_file_id, tape_id=tape_id, pool_id=pool_id)

Lists all task sources.

**API Key Scope**: task_sources / index

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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
import_file_id = 'import_file_id_example' # str | Filter on import file id (optional)
tape_id = 'tape_id_example' # str | Filter on tape id (optional)
pool_id = 'pool_id_example' # str | Filter on a pool id (optional)

try:
    # Lists all task sources.
    api_response = api_instance.index_task_sources(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, file_id=file_id, import_file_id=import_file_id, tape_id=tape_id, pool_id=pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->index_task_sources: %s\n" % e)
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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
import_file_id = 'import_file_id_example' # str | Filter on import file id (optional)
tape_id = 'tape_id_example' # str | Filter on tape id (optional)
pool_id = 'pool_id_example' # str | Filter on a pool id (optional)

try:
    # Lists all task sources.
    api_response = api_instance.index_task_sources(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, file_id=file_id, import_file_id=import_file_id, tape_id=tape_id, pool_id=pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->index_task_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **import_file_id** | **str**| Filter on import file id | [optional] 
 **tape_id** | **str**| Filter on tape id | [optional] 
 **pool_id** | **str**| Filter on a pool id | [optional] 

### Return type

[**TaskSourceCollection**](TaskSourceCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of task sources. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_task_source**
> TaskSourceDown show_task_source(task_id, task_source_id)

Displays a specific task source.

**API Key Scope**: task_sources / show

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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_id = 56 # int | Numeric ID of task source.

try:
    # Displays a specific task source.
    api_response = api_instance.show_task_source(task_id, task_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->show_task_source: %s\n" % e)
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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_id = 56 # int | Numeric ID of task source.

try:
    # Displays a specific task source.
    api_response = api_instance.show_task_source(task_id, task_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->show_task_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_source_id** | **int**| Numeric ID of task source. | 

### Return type

[**TaskSourceDown**](TaskSourceDown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific task source. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_source**
> TaskSourceDown update_task_source(task_id, task_source_id, task_source_body)

Updates a specific task source.

**API Key Scope**: task_sources / update

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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_id = 56 # int | Numeric ID of task source.
task_source_body = nodeum_sdk.TaskSourceUp() # TaskSourceUp | 

try:
    # Updates a specific task source.
    api_response = api_instance.update_task_source(task_id, task_source_id, task_source_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->update_task_source: %s\n" % e)
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
api_instance = nodeum_sdk.TaskSourcesApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_id = 56 # int | Numeric ID of task source.
task_source_body = nodeum_sdk.TaskSourceUp() # TaskSourceUp | 

try:
    # Updates a specific task source.
    api_response = api_instance.update_task_source(task_id, task_source_id, task_source_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskSourcesApi->update_task_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_source_id** | **int**| Numeric ID of task source. | 
 **task_source_body** | [**TaskSourceUp**](TaskSourceUp.md)|  | 

### Return type

[**TaskSourceDown**](TaskSourceDown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific task source. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

