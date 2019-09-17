# swagger_client.TaskSourcesApi

All URIs are relative to *https://localhost/api/v2*

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
api_instance = swagger_client.TaskSourcesApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_body = swagger_client.TaskSourceUp() # TaskSourceUp | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_task_source**
> destroy_task_source(task_id, task_source_id)

Destroys a specific task source.

**API Key Scope**: task_sources / destroy

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
api_instance = swagger_client.TaskSourcesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_task_sources**
> TaskSourceCollection index_task_sources(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, file_id=file_id, import_file_id=import_file_id, tape_id=tape_id, tape_pool_id=tape_pool_id, cloud_pool_id=cloud_pool_id, nas_pool_id=nas_pool_id)

Lists all task sources.

**API Key Scope**: task_sources / index

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
api_instance = swagger_client.TaskSourcesApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
import_file_id = 'import_file_id_example' # str | Filter on import file id (optional)
tape_id = 'tape_id_example' # str | Filter on tape id (optional)
tape_pool_id = 'tape_pool_id_example' # str | Filter on tape pool id (optional)
cloud_pool_id = 'cloud_pool_id_example' # str | Filter on cloud pool id (optional)
nas_pool_id = 'nas_pool_id_example' # str | Filter on NAS pool id (optional)

try:
    # Lists all task sources.
    api_response = api_instance.index_task_sources(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, file_id=file_id, import_file_id=import_file_id, tape_id=tape_id, tape_pool_id=tape_pool_id, cloud_pool_id=cloud_pool_id, nas_pool_id=nas_pool_id)
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
 **tape_pool_id** | **str**| Filter on tape pool id | [optional] 
 **cloud_pool_id** | **str**| Filter on cloud pool id | [optional] 
 **nas_pool_id** | **str**| Filter on NAS pool id | [optional] 

### Return type

[**TaskSourceCollection**](TaskSourceCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_task_source**
> TaskSourceDown show_task_source(task_id, task_source_id)

Displays a specific task source.

**API Key Scope**: task_sources / show

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
api_instance = swagger_client.TaskSourcesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_source**
> TaskSourceDown update_task_source(task_id, task_source_id, task_source_body)

Updates a specific task source.

**API Key Scope**: task_sources / update

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
api_instance = swagger_client.TaskSourcesApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_source_id = 56 # int | Numeric ID of task source.
task_source_body = swagger_client.TaskSourceUp() # TaskSourceUp | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
