# swagger_client.CloudPoolsApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_pool**](CloudPoolsApi.md#create_cloud_pool) | **POST** /cloud_pools | Creates a new cloud pool.
[**destroy_cloud_pool**](CloudPoolsApi.md#destroy_cloud_pool) | **DELETE** /cloud_pools/{cloud_pool_id} | Destroys a specific cloud pool.
[**index_cloud_pools**](CloudPoolsApi.md#index_cloud_pools) | **GET** /cloud_pools | Lists all cloud pools.
[**show_cloud_pool**](CloudPoolsApi.md#show_cloud_pool) | **GET** /cloud_pools/{cloud_pool_id} | Displays a specific cloud pool.
[**update_cloud_pool**](CloudPoolsApi.md#update_cloud_pool) | **PUT** /cloud_pools/{cloud_pool_id} | Updates a specific cloud pool.


# **create_cloud_pool**
> CloudPool create_cloud_pool(cloud_pool_body)

Creates a new cloud pool.

**API Key Scope**: cloud_pools / create

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
api_instance = swagger_client.CloudPoolsApi(swagger_client.ApiClient(configuration))
cloud_pool_body = swagger_client.CloudPoolUp() # CloudPoolUp | 

try:
    # Creates a new cloud pool.
    api_response = api_instance.create_cloud_pool(cloud_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->create_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_body** | [**CloudPoolUp**](CloudPoolUp.md)|  | 

### Return type

[**CloudPool**](CloudPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_cloud_pool**
> destroy_cloud_pool(cloud_pool_id)

Destroys a specific cloud pool.

**API Key Scope**: cloud_pools / destroy

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
api_instance = swagger_client.CloudPoolsApi(swagger_client.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.

try:
    # Destroys a specific cloud pool.
    api_instance.destroy_cloud_pool(cloud_pool_id)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->destroy_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Numeric ID or name of cloud pool. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_cloud_pools**
> CloudPoolCollection index_cloud_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type)

Lists all cloud pools.

**API Key Scope**: cloud_pools / index

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
api_instance = swagger_client.CloudPoolsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
comment = 'comment_example' # str | Filter on comment (optional)
type = 'type_example' # str | Filter on type (optional)

try:
    # Lists all cloud pools.
    api_response = api_instance.index_cloud_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->index_cloud_pools: %s\n" % e)
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

[**CloudPoolCollection**](CloudPoolCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_cloud_pool**
> CloudPool show_cloud_pool(cloud_pool_id)

Displays a specific cloud pool.

**API Key Scope**: cloud_pools / show

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
api_instance = swagger_client.CloudPoolsApi(swagger_client.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.

try:
    # Displays a specific cloud pool.
    api_response = api_instance.show_cloud_pool(cloud_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->show_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Numeric ID or name of cloud pool. | 

### Return type

[**CloudPool**](CloudPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_pool**
> CloudPool update_cloud_pool(cloud_pool_id, cloud_pool_body)

Updates a specific cloud pool.

**API Key Scope**: cloud_pools / update

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
api_instance = swagger_client.CloudPoolsApi(swagger_client.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.
cloud_pool_body = swagger_client.CloudPoolUp() # CloudPoolUp | 

try:
    # Updates a specific cloud pool.
    api_response = api_instance.update_cloud_pool(cloud_pool_id, cloud_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->update_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Numeric ID or name of cloud pool. | 
 **cloud_pool_body** | [**CloudPoolUp**](CloudPoolUp.md)|  | 

### Return type

[**CloudPool**](CloudPool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

