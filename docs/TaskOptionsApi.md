# swagger_client.TaskOptionsApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task_option**](TaskOptionsApi.md#create_task_option) | **POST** /tasks/{task_id}/task_options | Creates a new task option.
[**destroy_task_option**](TaskOptionsApi.md#destroy_task_option) | **DELETE** /tasks/{task_id}/task_options/{task_option_id} | Destroys a specific task option.
[**index_task_options**](TaskOptionsApi.md#index_task_options) | **GET** /tasks/{task_id}/task_options | Lists all task options.
[**show_task_option**](TaskOptionsApi.md#show_task_option) | **GET** /tasks/{task_id}/task_options/{task_option_id} | Displays a specific task option.
[**update_task_option**](TaskOptionsApi.md#update_task_option) | **PUT** /tasks/{task_id}/task_options/{task_option_id} | Updates a specific task option.


# **create_task_option**
> TaskOption create_task_option(task_id, task_option_body)

Creates a new task option.

**API Key Scope**: task_options / create

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
api_instance = swagger_client.TaskOptionsApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_option_body = swagger_client.TaskOption() # TaskOption | 

try:
    # Creates a new task option.
    api_response = api_instance.create_task_option(task_id, task_option_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskOptionsApi->create_task_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_option_body** | [**TaskOption**](TaskOption.md)|  | 

### Return type

[**TaskOption**](TaskOption.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_task_option**
> destroy_task_option(task_id, task_option_id)

Destroys a specific task option.

**API Key Scope**: task_options / destroy

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
api_instance = swagger_client.TaskOptionsApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_option_id = 56 # int | Numeric ID of task option.

try:
    # Destroys a specific task option.
    api_instance.destroy_task_option(task_id, task_option_id)
except ApiException as e:
    print("Exception when calling TaskOptionsApi->destroy_task_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_option_id** | **int**| Numeric ID of task option. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_task_options**
> TaskOptionCollection index_task_options(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, type=type, value=value)

Lists all task options.

**API Key Scope**: task_options / index

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
api_instance = swagger_client.TaskOptionsApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
type = 'type_example' # str | Filter on type (optional)
value = 'value_example' # str | Filter on value (optional)

try:
    # Lists all task options.
    api_response = api_instance.index_task_options(task_id, limit=limit, offset=offset, sort_by=sort_by, id=id, type=type, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskOptionsApi->index_task_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **value** | **str**| Filter on value | [optional] 

### Return type

[**TaskOptionCollection**](TaskOptionCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_task_option**
> TaskOption show_task_option(task_id, task_option_id)

Displays a specific task option.

**API Key Scope**: task_options / show

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
api_instance = swagger_client.TaskOptionsApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_option_id = 56 # int | Numeric ID of task option.

try:
    # Displays a specific task option.
    api_response = api_instance.show_task_option(task_id, task_option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskOptionsApi->show_task_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_option_id** | **int**| Numeric ID of task option. | 

### Return type

[**TaskOption**](TaskOption.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_option**
> TaskOption update_task_option(task_id, task_option_id, task_option_body)

Updates a specific task option.

**API Key Scope**: task_options / update

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
api_instance = swagger_client.TaskOptionsApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_option_id = 56 # int | Numeric ID of task option.
task_option_body = swagger_client.TaskOption() # TaskOption | 

try:
    # Updates a specific task option.
    api_response = api_instance.update_task_option(task_id, task_option_id, task_option_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskOptionsApi->update_task_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_option_id** | **int**| Numeric ID of task option. | 
 **task_option_body** | [**TaskOption**](TaskOption.md)|  | 

### Return type

[**TaskOption**](TaskOption.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

