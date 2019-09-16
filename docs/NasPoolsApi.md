# swagger_client.NasPoolsApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nas_pool**](NasPoolsApi.md#create_nas_pool) | **POST** /nas_pools | Creates a new NAS pool.
[**destroy_nas_pool**](NasPoolsApi.md#destroy_nas_pool) | **DELETE** /nas_pools/{nas_pool_id} | Destroys a specific NAS pool.
[**index_nas_pools**](NasPoolsApi.md#index_nas_pools) | **GET** /nas_pools | Lists all NAS pools.
[**show_nas_pool**](NasPoolsApi.md#show_nas_pool) | **GET** /nas_pools/{nas_pool_id} | Displays a specific NAS pool.
[**update_nas_pool**](NasPoolsApi.md#update_nas_pool) | **PUT** /nas_pools/{nas_pool_id} | Updates a specific NAS pool.


# **create_nas_pool**
> NasPool create_nas_pool(nas_pool_body)

Creates a new NAS pool.

**API Key Scope**: nas_pools / create

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
api_instance = swagger_client.NasPoolsApi(swagger_client.ApiClient(configuration))
nas_pool_body = swagger_client.NasPoolUp() # NasPoolUp | 

try:
    # Creates a new NAS pool.
    api_response = api_instance.create_nas_pool(nas_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasPoolsApi->create_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_body** | [**NasPoolUp**](NasPoolUp.md)|  | 

### Return type

[**NasPool**](NasPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_nas_pool**
> destroy_nas_pool(nas_pool_id)

Destroys a specific NAS pool.

**API Key Scope**: nas_pools / destroy

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
api_instance = swagger_client.NasPoolsApi(swagger_client.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.

try:
    # Destroys a specific NAS pool.
    api_instance.destroy_nas_pool(nas_pool_id)
except ApiException as e:
    print("Exception when calling NasPoolsApi->destroy_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_nas_pools**
> NasPoolCollection index_nas_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type)

Lists all NAS pools.

**API Key Scope**: nas_pools / index

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
api_instance = swagger_client.NasPoolsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
comment = 'comment_example' # str | Filter on comment (optional)
type = 'type_example' # str | Filter on type (optional)

try:
    # Lists all NAS pools.
    api_response = api_instance.index_nas_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasPoolsApi->index_nas_pools: %s\n" % e)
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

### Return type

[**NasPoolCollection**](NasPoolCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_nas_pool**
> NasPool show_nas_pool(nas_pool_id)

Displays a specific NAS pool.

**API Key Scope**: nas_pools / show

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
api_instance = swagger_client.NasPoolsApi(swagger_client.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.

try:
    # Displays a specific NAS pool.
    api_response = api_instance.show_nas_pool(nas_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasPoolsApi->show_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 

### Return type

[**NasPool**](NasPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nas_pool**
> NasPool update_nas_pool(nas_pool_id, nas_pool_body)

Updates a specific NAS pool.

**API Key Scope**: nas_pools / update

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
api_instance = swagger_client.NasPoolsApi(swagger_client.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_pool_body = swagger_client.NasPoolUp() # NasPoolUp | 

try:
    # Updates a specific NAS pool.
    api_response = api_instance.update_nas_pool(nas_pool_id, nas_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasPoolsApi->update_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 
 **nas_pool_body** | [**NasPoolUp**](NasPoolUp.md)|  | 

### Return type

[**NasPool**](NasPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

