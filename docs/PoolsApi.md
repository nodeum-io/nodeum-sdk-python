# nodeum_sdk.PoolsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pool**](PoolsApi.md#create_pool) | **POST** /pools | Creates a new pool.
[**create_primary_scan**](PoolsApi.md#create_primary_scan) | **POST** /pools/{pool_id}/primary_scan | Set a new primary pool scan option.
[**destroy_pool**](PoolsApi.md#destroy_pool) | **DELETE** /pools/{pool_id} | Destroys a specific tape pool.
[**destroy_primary_scan**](PoolsApi.md#destroy_primary_scan) | **DELETE** /pools/{pool_id}/primary_scan | Disable the primary pool scan.
[**index_pools**](PoolsApi.md#index_pools) | **GET** /pools | Lists all pools.
[**mount_pool**](PoolsApi.md#mount_pool) | **PUT** /pools/{pool_id}/mount | Mount Pool.
[**mount_status_pool**](PoolsApi.md#mount_status_pool) | **GET** /pools/{pool_id}/mount | Get mount status of Pool.
[**show_pool**](PoolsApi.md#show_pool) | **GET** /pools/{pool_id} | Displays a specific pool.
[**show_primary_scan**](PoolsApi.md#show_primary_scan) | **GET** /pools/{pool_id}/primary_scan | Displays the primary pool scan status.
[**sync_primary_pool**](PoolsApi.md#sync_primary_pool) | **POST** /pools/{pool_id}/sync | Synchronize a primary after a scan (for internal use only).
[**unmount_pool**](PoolsApi.md#unmount_pool) | **DELETE** /pools/{pool_id}/mount | Unmount Pool.
[**update_pool**](PoolsApi.md#update_pool) | **PUT** /pools/{pool_id} | Updates a specific pool.
[**update_primary_scan**](PoolsApi.md#update_primary_scan) | **PUT** /pools/{pool_id}/primary_scan | Updates the existing primary pool scan option.


# **create_pool**
> Pool create_pool(pool_body)

Creates a new pool.

**API Key Scope**: pools / create

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_body = nodeum_sdk.PoolUp() # PoolUp | 

try:
    # Creates a new pool.
    api_response = api_instance.create_pool(pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->create_pool: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_body = nodeum_sdk.PoolUp() # PoolUp | 

try:
    # Creates a new pool.
    api_response = api_instance.create_pool(pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->create_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_body** | [**PoolUp**](PoolUp.md)|  | 

### Return type

[**Pool**](Pool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific pool. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_primary_scan**
> PrimaryScan create_primary_scan(pool_id, primary_scan_body)

Set a new primary pool scan option.

**API Key Scope**: primary_scans / create

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
primary_scan_body = nodeum_sdk.PrimaryScan() # PrimaryScan | 

try:
    # Set a new primary pool scan option.
    api_response = api_instance.create_primary_scan(pool_id, primary_scan_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->create_primary_scan: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
primary_scan_body = nodeum_sdk.PrimaryScan() # PrimaryScan | 

try:
    # Set a new primary pool scan option.
    api_response = api_instance.create_primary_scan(pool_id, primary_scan_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->create_primary_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **primary_scan_body** | [**PrimaryScan**](PrimaryScan.md)|  | 

### Return type

[**PrimaryScan**](PrimaryScan.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The primary pool scan status. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_pool**
> destroy_pool(pool_id)

Destroys a specific tape pool.

**API Key Scope**: pools / destroy

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Destroys a specific tape pool.
    api_instance.destroy_pool(pool_id)
except ApiException as e:
    print("Exception when calling PoolsApi->destroy_pool: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Destroys a specific tape pool.
    api_instance.destroy_pool(pool_id)
except ApiException as e:
    print("Exception when calling PoolsApi->destroy_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 

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
**204** | Pool destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_primary_scan**
> destroy_primary_scan(pool_id)

Disable the primary pool scan.

**API Key Scope**: primary_scans / destroy

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Disable the primary pool scan.
    api_instance.destroy_primary_scan(pool_id)
except ApiException as e:
    print("Exception when calling PoolsApi->destroy_primary_scan: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Disable the primary pool scan.
    api_instance.destroy_primary_scan(pool_id)
except ApiException as e:
    print("Exception when calling PoolsApi->destroy_primary_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 

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
**204** | Primary pool scan disabled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_pools**
> PoolCollection index_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type, content=content, primary_id=primary_id)

Lists all pools.

**API Key Scope**: pools / index

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
comment = 'comment_example' # str | Filter on comment (optional)
type = 'type_example' # str | Filter on type (optional)
content = 'content_example' # str | Filter on content (optional)
primary_id = 'primary_id_example' # str | Filter on primary id (optional)

try:
    # Lists all pools.
    api_response = api_instance.index_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type, content=content, primary_id=primary_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->index_pools: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
comment = 'comment_example' # str | Filter on comment (optional)
type = 'type_example' # str | Filter on type (optional)
content = 'content_example' # str | Filter on content (optional)
primary_id = 'primary_id_example' # str | Filter on primary id (optional)

try:
    # Lists all pools.
    api_response = api_instance.index_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type, content=content, primary_id=primary_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->index_pools: %s\n" % e)
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
 **content** | **str**| Filter on content | [optional] 
 **primary_id** | **str**| Filter on primary id | [optional] 

### Return type

[**PoolCollection**](PoolCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of pools. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mount_pool**
> MountStatus mount_pool(pool_id)

Mount Pool.

**API Key Scope**: pools / mount

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Mount Pool.
    api_response = api_instance.mount_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->mount_pool: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Mount Pool.
    api_response = api_instance.mount_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->mount_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 

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

# **mount_status_pool**
> MountStatus mount_status_pool(pool_id)

Get mount status of Pool.

**API Key Scope**: pools / mount_status

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Get mount status of Pool.
    api_response = api_instance.mount_status_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->mount_status_pool: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Get mount status of Pool.
    api_response = api_instance.mount_status_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->mount_status_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 

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

# **show_pool**
> Pool show_pool(pool_id)

Displays a specific pool.

**API Key Scope**: pools / show

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Displays a specific pool.
    api_response = api_instance.show_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->show_pool: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Displays a specific pool.
    api_response = api_instance.show_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->show_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 

### Return type

[**Pool**](Pool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific pool. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_primary_scan**
> PrimaryScan show_primary_scan(pool_id)

Displays the primary pool scan status.

**API Key Scope**: primary_scans / show

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Displays the primary pool scan status.
    api_response = api_instance.show_primary_scan(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->show_primary_scan: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Displays the primary pool scan status.
    api_response = api_instance.show_primary_scan(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->show_primary_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 

### Return type

[**PrimaryScan**](PrimaryScan.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The primary pool scan status. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_primary_pool**
> sync_primary_pool(pool_id, tx)

Synchronize a primary after a scan (for internal use only).

**API Key Scope**: pools / sync_primary

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
tx = 56 # int | New transaction number.

try:
    # Synchronize a primary after a scan (for internal use only).
    api_instance.sync_primary_pool(pool_id, tx)
except ApiException as e:
    print("Exception when calling PoolsApi->sync_primary_pool: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
tx = 56 # int | New transaction number.

try:
    # Synchronize a primary after a scan (for internal use only).
    api_instance.sync_primary_pool(pool_id, tx)
except ApiException as e:
    print("Exception when calling PoolsApi->sync_primary_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **tx** | **int**| New transaction number. | 

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
**204** | Synchronization triggered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmount_pool**
> MountStatus unmount_pool(pool_id)

Unmount Pool.

**API Key Scope**: pools / unmount

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Unmount Pool.
    api_response = api_instance.unmount_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->unmount_pool: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.

try:
    # Unmount Pool.
    api_response = api_instance.unmount_pool(pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->unmount_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 

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

# **update_pool**
> Pool update_pool(pool_id, pool_body)

Updates a specific pool.

**API Key Scope**: pools / update

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
pool_body = nodeum_sdk.PoolUp() # PoolUp | 

try:
    # Updates a specific pool.
    api_response = api_instance.update_pool(pool_id, pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->update_pool: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
pool_body = nodeum_sdk.PoolUp() # PoolUp | 

try:
    # Updates a specific pool.
    api_response = api_instance.update_pool(pool_id, pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->update_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **pool_body** | [**PoolUp**](PoolUp.md)|  | 

### Return type

[**Pool**](Pool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific pool. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_primary_scan**
> PrimaryScan update_primary_scan(pool_id, primary_scan_body)

Updates the existing primary pool scan option.

**API Key Scope**: primary_scans / update

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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
primary_scan_body = nodeum_sdk.PrimaryScan() # PrimaryScan | 

try:
    # Updates the existing primary pool scan option.
    api_response = api_instance.update_primary_scan(pool_id, primary_scan_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->update_primary_scan: %s\n" % e)
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
api_instance = nodeum_sdk.PoolsApi(nodeum_sdk.ApiClient(configuration))
pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
primary_scan_body = nodeum_sdk.PrimaryScan() # PrimaryScan | 

try:
    # Updates the existing primary pool scan option.
    api_response = api_instance.update_primary_scan(pool_id, primary_scan_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoolsApi->update_primary_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **primary_scan_body** | [**PrimaryScan**](PrimaryScan.md)|  | 

### Return type

[**PrimaryScan**](PrimaryScan.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The primary pool scan status. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

