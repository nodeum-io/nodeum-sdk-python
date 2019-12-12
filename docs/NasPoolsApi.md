# nodeum_sdk.NasPoolsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nas_pool**](NasPoolsApi.md#create_nas_pool) | **POST** /nas_pools | Creates a new NAS pool.
[**destroy_nas_pool**](NasPoolsApi.md#destroy_nas_pool) | **DELETE** /nas_pools/{nas_pool_id} | Destroys a specific NAS pool.
[**index_nas_pools**](NasPoolsApi.md#index_nas_pools) | **GET** /nas_pools | Lists all NAS pools.
[**mount_status_nas_pool**](NasPoolsApi.md#mount_status_nas_pool) | **GET** /nas_pools/{nas_pool_id}/mount | Get mount status of NAS pool.
[**show_nas_pool**](NasPoolsApi.md#show_nas_pool) | **GET** /nas_pools/{nas_pool_id} | Displays a specific NAS pool.
[**update_nas_pool**](NasPoolsApi.md#update_nas_pool) | **PUT** /nas_pools/{nas_pool_id} | Updates a specific NAS pool.


# **create_nas_pool**
> NasPool create_nas_pool(nas_pool_body)

Creates a new NAS pool.

**API Key Scope**: nas_pools / create

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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
nas_pool_body = nodeum_sdk.NasPoolUp() # NasPoolUp | 

try:
    # Creates a new NAS pool.
    api_response = api_instance.create_nas_pool(nas_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasPoolsApi->create_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
nas_pool_body = nodeum_sdk.NasPoolUp() # NasPoolUp | 

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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific NAS pool. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_nas_pool**
> destroy_nas_pool(nas_pool_id)

Destroys a specific NAS pool.

**API Key Scope**: nas_pools / destroy

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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.

try:
    # Destroys a specific NAS pool.
    api_instance.destroy_nas_pool(nas_pool_id)
except ApiException as e:
    print("Exception when calling NasPoolsApi->destroy_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NAS pool destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_nas_pools**
> NasPoolCollection index_nas_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type)

Lists all NAS pools.

**API Key Scope**: nas_pools / index

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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of NAS pools. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mount_status_nas_pool**
> MountStatus mount_status_nas_pool(nas_pool_id)

Get mount status of NAS pool.

**API Key Scope**: nas_pools / mount_status

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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.

try:
    # Get mount status of NAS pool.
    api_response = api_instance.mount_status_nas_pool(nas_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasPoolsApi->mount_status_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.

try:
    # Get mount status of NAS pool.
    api_response = api_instance.mount_status_nas_pool(nas_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasPoolsApi->mount_status_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 

### Return type

[**MountStatus**](MountStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mount status of storage. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_nas_pool**
> NasPool show_nas_pool(nas_pool_id)

Displays a specific NAS pool.

**API Key Scope**: nas_pools / show

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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.

try:
    # Displays a specific NAS pool.
    api_response = api_instance.show_nas_pool(nas_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasPoolsApi->show_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific NAS pool. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nas_pool**
> NasPool update_nas_pool(nas_pool_id, nas_pool_body)

Updates a specific NAS pool.

**API Key Scope**: nas_pools / update

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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_pool_body = nodeum_sdk.NasPoolUp() # NasPoolUp | 

try:
    # Updates a specific NAS pool.
    api_response = api_instance.update_nas_pool(nas_pool_id, nas_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasPoolsApi->update_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasPoolsApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_pool_body = nodeum_sdk.NasPoolUp() # NasPoolUp | 

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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific NAS pool. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

