# nodeum_sdk.TaskDestinationsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_destination**](TaskDestinationsApi.md#create_task_destination) | **POST** /tasks/{task_id}/task_destinations | Creates a new task destination.
[**destroy_task_destination**](TaskDestinationsApi.md#destroy_task_destination) | **DELETE** /tasks/{task_id}/task_destinations/{task_destination_id} | Destroys a specific task destination.
[**index_task_destinations**](TaskDestinationsApi.md#index_task_destinations) | **GET** /tasks/{task_id}/task_destinations | Lists all task destinations.
[**show_task_destination**](TaskDestinationsApi.md#show_task_destination) | **GET** /tasks/{task_id}/task_destinations/{task_destination_id} | Displays a specific task destination.
[**update_task_destination**](TaskDestinationsApi.md#update_task_destination) | **PUT** /tasks/{task_id}/task_destinations/{task_destination_id} | Updates a specific task destination.


# **create_task_destination**
> TaskDestinationDown create_task_destination(task_id, task_destination_body)

Creates a new task destination.

**API Key Scope**: task_destinations / create

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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_destination_body = nodeum_sdk.TaskDestinationUp() # TaskDestinationUp | 

try:
    # Creates a new task destination.
    api_response = api_instance.create_task_destination(task_id, task_destination_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->create_task_destination: %s\n" % e)
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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_destination_body = nodeum_sdk.TaskDestinationUp() # TaskDestinationUp | 

try:
    # Creates a new task destination.
    api_response = api_instance.create_task_destination(task_id, task_destination_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->create_task_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_destination_body** | [**TaskDestinationUp**](TaskDestinationUp.md)|  | 

### Return type

[**TaskDestinationDown**](TaskDestinationDown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific task destination. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_task_destination**
> destroy_task_destination(task_id, task_destination_id)

Destroys a specific task destination.

**API Key Scope**: task_destinations / destroy

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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_destination_id = 56 # int | Numeric ID of task destination.

try:
    # Destroys a specific task destination.
    api_instance.destroy_task_destination(task_id, task_destination_id)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->destroy_task_destination: %s\n" % e)
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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_destination_id = 56 # int | Numeric ID of task destination.

try:
    # Destroys a specific task destination.
    api_instance.destroy_task_destination(task_id, task_destination_id)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->destroy_task_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_destination_id** | **int**| Numeric ID of task destination. | 

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
**204** | Task destination destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_task_destinations**
> TaskDestinationCollection index_task_destinations(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, folder_id=folder_id, tape_id=tape_id, pool_id=pool_id)

Lists all task destinations.

**API Key Scope**: task_destinations / index

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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
folder_id = 'folder_id_example' # str | Filter on folder id (optional)
tape_id = 'tape_id_example' # str | Filter on tape id (optional)
pool_id = 'pool_id_example' # str | Filter on a pool id (optional)

try:
    # Lists all task destinations.
    api_response = api_instance.index_task_destinations(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, folder_id=folder_id, tape_id=tape_id, pool_id=pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->index_task_destinations: %s\n" % e)
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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
folder_id = 'folder_id_example' # str | Filter on folder id (optional)
tape_id = 'tape_id_example' # str | Filter on tape id (optional)
pool_id = 'pool_id_example' # str | Filter on a pool id (optional)

try:
    # Lists all task destinations.
    api_response = api_instance.index_task_destinations(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, folder_id=folder_id, tape_id=tape_id, pool_id=pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->index_task_destinations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **folder_id** | **str**| Filter on folder id | [optional] 
 **tape_id** | **str**| Filter on tape id | [optional] 
 **pool_id** | **str**| Filter on a pool id | [optional] 

### Return type

[**TaskDestinationCollection**](TaskDestinationCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of task destinations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_task_destination**
> TaskDestinationDown show_task_destination(task_id, task_destination_id)

Displays a specific task destination.

**API Key Scope**: task_destinations / show

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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_destination_id = 56 # int | Numeric ID of task destination.

try:
    # Displays a specific task destination.
    api_response = api_instance.show_task_destination(task_id, task_destination_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->show_task_destination: %s\n" % e)
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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_destination_id = 56 # int | Numeric ID of task destination.

try:
    # Displays a specific task destination.
    api_response = api_instance.show_task_destination(task_id, task_destination_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->show_task_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_destination_id** | **int**| Numeric ID of task destination. | 

### Return type

[**TaskDestinationDown**](TaskDestinationDown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific task destination. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_destination**
> TaskDestinationDown update_task_destination(task_id, task_destination_id, task_destination_body)

Updates a specific task destination.

**API Key Scope**: task_destinations / update

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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_destination_id = 56 # int | Numeric ID of task destination.
task_destination_body = nodeum_sdk.TaskDestinationUp() # TaskDestinationUp | 

try:
    # Updates a specific task destination.
    api_response = api_instance.update_task_destination(task_id, task_destination_id, task_destination_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->update_task_destination: %s\n" % e)
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
api_instance = nodeum_sdk.TaskDestinationsApi(nodeum_sdk.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_destination_id = 56 # int | Numeric ID of task destination.
task_destination_body = nodeum_sdk.TaskDestinationUp() # TaskDestinationUp | 

try:
    # Updates a specific task destination.
    api_response = api_instance.update_task_destination(task_id, task_destination_id, task_destination_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskDestinationsApi->update_task_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_destination_id** | **int**| Numeric ID of task destination. | 
 **task_destination_body** | [**TaskDestinationUp**](TaskDestinationUp.md)|  | 

### Return type

[**TaskDestinationDown**](TaskDestinationDown.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific task destination. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

