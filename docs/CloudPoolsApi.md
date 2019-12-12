# nodeum_sdk.CloudPoolsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_pool**](CloudPoolsApi.md#create_cloud_pool) | **POST** /cloud_pools | Creates a new cloud pool.
[**destroy_cloud_pool**](CloudPoolsApi.md#destroy_cloud_pool) | **DELETE** /cloud_pools/{cloud_pool_id} | Destroys a specific cloud pool.
[**index_cloud_pools**](CloudPoolsApi.md#index_cloud_pools) | **GET** /cloud_pools | Lists all cloud pools.
[**mount_status_cloud_pool**](CloudPoolsApi.md#mount_status_cloud_pool) | **GET** /cloud_pools/{cloud_pool_id}/mount | Get mount status of Cloud pool.
[**show_cloud_pool**](CloudPoolsApi.md#show_cloud_pool) | **GET** /cloud_pools/{cloud_pool_id} | Displays a specific cloud pool.
[**update_cloud_pool**](CloudPoolsApi.md#update_cloud_pool) | **PUT** /cloud_pools/{cloud_pool_id} | Updates a specific cloud pool.


# **create_cloud_pool**
> CloudPool create_cloud_pool(cloud_pool_body)

Creates a new cloud pool.

**API Key Scope**: cloud_pools / create

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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
cloud_pool_body = nodeum_sdk.CloudPoolUp() # CloudPoolUp | 

try:
    # Creates a new cloud pool.
    api_response = api_instance.create_cloud_pool(cloud_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->create_cloud_pool: %s\n" % e)
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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
cloud_pool_body = nodeum_sdk.CloudPoolUp() # CloudPoolUp | 

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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific cloud pool. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_cloud_pool**
> destroy_cloud_pool(cloud_pool_id)

Destroys a specific cloud pool.

**API Key Scope**: cloud_pools / destroy

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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.

try:
    # Destroys a specific cloud pool.
    api_instance.destroy_cloud_pool(cloud_pool_id)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->destroy_cloud_pool: %s\n" % e)
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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Cloud pool destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_cloud_pools**
> CloudPoolCollection index_cloud_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type)

Lists all cloud pools.

**API Key Scope**: cloud_pools / index

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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of cloud pools. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mount_status_cloud_pool**
> MountStatus mount_status_cloud_pool(cloud_pool_id)

Get mount status of Cloud pool.

**API Key Scope**: cloud_pools / mount_status

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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.

try:
    # Get mount status of Cloud pool.
    api_response = api_instance.mount_status_cloud_pool(cloud_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->mount_status_cloud_pool: %s\n" % e)
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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.

try:
    # Get mount status of Cloud pool.
    api_response = api_instance.mount_status_cloud_pool(cloud_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->mount_status_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Numeric ID or name of cloud pool. | 

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

# **show_cloud_pool**
> CloudPool show_cloud_pool(cloud_pool_id)

Displays a specific cloud pool.

**API Key Scope**: cloud_pools / show

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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.

try:
    # Displays a specific cloud pool.
    api_response = api_instance.show_cloud_pool(cloud_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->show_cloud_pool: %s\n" % e)
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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific cloud pool. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_pool**
> CloudPool update_cloud_pool(cloud_pool_id, cloud_pool_body)

Updates a specific cloud pool.

**API Key Scope**: cloud_pools / update

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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.
cloud_pool_body = nodeum_sdk.CloudPoolUp() # CloudPoolUp | 

try:
    # Updates a specific cloud pool.
    api_response = api_instance.update_cloud_pool(cloud_pool_id, cloud_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudPoolsApi->update_cloud_pool: %s\n" % e)
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
api_instance = nodeum_sdk.CloudPoolsApi(nodeum_sdk.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.
cloud_pool_body = nodeum_sdk.CloudPoolUp() # CloudPoolUp | 

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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific cloud pool. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

