# nodeum_sdk.NasSharesApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nas_share_by_nas**](NasSharesApi.md#create_nas_share_by_nas) | **POST** /nas/{nas_id}/nas_shares | Creates a new NAS share.
[**destroy_nas_share**](NasSharesApi.md#destroy_nas_share) | **DELETE** /nas_shares/{nas_share_id} | Destroys a specific NAS share.
[**destroy_nas_share_by_nas**](NasSharesApi.md#destroy_nas_share_by_nas) | **DELETE** /nas/{nas_id}/nas_shares/{nas_share_id} | Destroys a specific NAS share.
[**destroy_nas_share_by_nas_pool**](NasSharesApi.md#destroy_nas_share_by_nas_pool) | **DELETE** /nas_pools/{nas_pool_id}/nas_shares/{nas_share_id} | Destroys a specific NAS share.
[**index_nas_shares**](NasSharesApi.md#index_nas_shares) | **GET** /nas_shares | Lists all NAS shares.
[**index_nas_shares_by_nas**](NasSharesApi.md#index_nas_shares_by_nas) | **GET** /nas/{nas_id}/nas_shares | Lists all NAS shares.
[**index_nas_shares_by_nas_pool**](NasSharesApi.md#index_nas_shares_by_nas_pool) | **GET** /nas_pools/{nas_pool_id}/nas_shares | Lists all NAS shares.
[**mount_status_nas_share**](NasSharesApi.md#mount_status_nas_share) | **GET** /nas_shares/{nas_share_id}/mount | Get mount status of NAS Share.
[**mount_status_nas_share_by_nas**](NasSharesApi.md#mount_status_nas_share_by_nas) | **GET** /nas/{nas_id}/nas_shares/{nas_share_id}/mount | Get mount status of NAS Share.
[**mount_status_nas_share_by_nas_pool**](NasSharesApi.md#mount_status_nas_share_by_nas_pool) | **GET** /nas_pools/{nas_pool_id}/nas_shares/{nas_share_id}/mount | Get mount status of NAS Share.
[**show_nas_share_by_nas**](NasSharesApi.md#show_nas_share_by_nas) | **GET** /nas/{nas_id}/nas_shares/{nas_share_id} | Displays a specific NAS share.
[**show_nas_shares**](NasSharesApi.md#show_nas_shares) | **GET** /nas_shares/{nas_share_id} | Displays a specific NAS share.
[**show_nas_shares_by_nas_pool**](NasSharesApi.md#show_nas_shares_by_nas_pool) | **GET** /nas_pools/{nas_pool_id}/nas_shares/{nas_share_id} | Displays a specific NAS share.
[**test_nas_share**](NasSharesApi.md#test_nas_share) | **PUT** /nas/{nas_id}/nas_shares/-/test | Test an unsaved NAS Share.
[**test_result_nas_share**](NasSharesApi.md#test_result_nas_share) | **GET** /nas/{nas_id}/nas_shares/-/test | Check result of a NAS Share test job.
[**update_nas_share**](NasSharesApi.md#update_nas_share) | **PUT** /nas_shares/{nas_share_id} | Updates a specific NAS share.
[**update_nas_share_by_nas**](NasSharesApi.md#update_nas_share_by_nas) | **PUT** /nas/{nas_id}/nas_shares/{nas_share_id} | Updates a specific NAS share.
[**update_nas_share_by_nas_pool**](NasSharesApi.md#update_nas_share_by_nas_pool) | **PUT** /nas_pools/{nas_pool_id}/nas_shares/{nas_share_id} | Updates a specific NAS share.


# **create_nas_share_by_nas**
> NasShare create_nas_share_by_nas(nas_id, nas_share_body)

Creates a new NAS share.

**API Key Scope**: nas_shares / create

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Creates a new NAS share.
    api_response = api_instance.create_nas_share_by_nas(nas_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->create_nas_share_by_nas: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Creates a new NAS share.
    api_response = api_instance.create_nas_share_by_nas(nas_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->create_nas_share_by_nas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_id** | **str**| Numeric ID or name of NAS. | 
 **nas_share_body** | [**NasShare**](NasShare.md)|  | 

### Return type

[**NasShare**](NasShare.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific NAS share. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_nas_share**
> destroy_nas_share(nas_share_id)

Destroys a specific NAS share.

**API Key Scope**: nas_shares / destroy

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Destroys a specific NAS share.
    api_instance.destroy_nas_share(nas_share_id)
except ApiException as e:
    print("Exception when calling NasSharesApi->destroy_nas_share: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Destroys a specific NAS share.
    api_instance.destroy_nas_share(nas_share_id)
except ApiException as e:
    print("Exception when calling NasSharesApi->destroy_nas_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_share_id** | **int**| Numeric ID of NAS share. | 

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
**204** | NAS share destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_nas_share_by_nas**
> destroy_nas_share_by_nas(nas_id, nas_share_id)

Destroys a specific NAS share.

**API Key Scope**: nas_shares / destroy

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Destroys a specific NAS share.
    api_instance.destroy_nas_share_by_nas(nas_id, nas_share_id)
except ApiException as e:
    print("Exception when calling NasSharesApi->destroy_nas_share_by_nas: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Destroys a specific NAS share.
    api_instance.destroy_nas_share_by_nas(nas_id, nas_share_id)
except ApiException as e:
    print("Exception when calling NasSharesApi->destroy_nas_share_by_nas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_id** | **str**| Numeric ID or name of NAS. | 
 **nas_share_id** | **int**| Numeric ID of NAS share. | 

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
**204** | NAS share destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_nas_share_by_nas_pool**
> destroy_nas_share_by_nas_pool(nas_pool_id, nas_share_id)

Destroys a specific NAS share.

**API Key Scope**: nas_shares / destroy

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Destroys a specific NAS share.
    api_instance.destroy_nas_share_by_nas_pool(nas_pool_id, nas_share_id)
except ApiException as e:
    print("Exception when calling NasSharesApi->destroy_nas_share_by_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Destroys a specific NAS share.
    api_instance.destroy_nas_share_by_nas_pool(nas_pool_id, nas_share_id)
except ApiException as e:
    print("Exception when calling NasSharesApi->destroy_nas_share_by_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 
 **nas_share_id** | **int**| Numeric ID of NAS share. | 

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
**204** | NAS share destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_nas_shares**
> NasShareCollection index_nas_shares(limit=limit, offset=offset, sort_by=sort_by, id=id, path=path, options=options, username=username, nas_id=nas_id, nas_pool_id=nas_pool_id)

Lists all NAS shares.

**API Key Scope**: nas_shares / index   Optional API Key Explicit Scope: nas_shares / get_password

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
path = 'path_example' # str | Filter on path (optional)
options = 'options_example' # str | Filter on options (optional)
username = 'username_example' # str | Filter on username (optional)
nas_id = 'nas_id_example' # str | Filter on NAS id (optional)
nas_pool_id = 'nas_pool_id_example' # str | Filter on NAS pool id (optional)

try:
    # Lists all NAS shares.
    api_response = api_instance.index_nas_shares(limit=limit, offset=offset, sort_by=sort_by, id=id, path=path, options=options, username=username, nas_id=nas_id, nas_pool_id=nas_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->index_nas_shares: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
path = 'path_example' # str | Filter on path (optional)
options = 'options_example' # str | Filter on options (optional)
username = 'username_example' # str | Filter on username (optional)
nas_id = 'nas_id_example' # str | Filter on NAS id (optional)
nas_pool_id = 'nas_pool_id_example' # str | Filter on NAS pool id (optional)

try:
    # Lists all NAS shares.
    api_response = api_instance.index_nas_shares(limit=limit, offset=offset, sort_by=sort_by, id=id, path=path, options=options, username=username, nas_id=nas_id, nas_pool_id=nas_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->index_nas_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **path** | **str**| Filter on path | [optional] 
 **options** | **str**| Filter on options | [optional] 
 **username** | **str**| Filter on username | [optional] 
 **nas_id** | **str**| Filter on NAS id | [optional] 
 **nas_pool_id** | **str**| Filter on NAS pool id | [optional] 

### Return type

[**NasShareCollection**](NasShareCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of NAS shares. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_nas_shares_by_nas**
> NasShareCollection index_nas_shares_by_nas(nas_id, limit=limit, offset=offset, sort_by=sort_by, id=id, path=path, options=options, username=username, nas_pool_id=nas_pool_id)

Lists all NAS shares.

**API Key Scope**: nas_shares / index   Optional API Key Explicit Scope: nas_shares / get_password

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
path = 'path_example' # str | Filter on path (optional)
options = 'options_example' # str | Filter on options (optional)
username = 'username_example' # str | Filter on username (optional)
nas_pool_id = 'nas_pool_id_example' # str | Filter on NAS pool id (optional)

try:
    # Lists all NAS shares.
    api_response = api_instance.index_nas_shares_by_nas(nas_id, limit=limit, offset=offset, sort_by=sort_by, id=id, path=path, options=options, username=username, nas_pool_id=nas_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->index_nas_shares_by_nas: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
path = 'path_example' # str | Filter on path (optional)
options = 'options_example' # str | Filter on options (optional)
username = 'username_example' # str | Filter on username (optional)
nas_pool_id = 'nas_pool_id_example' # str | Filter on NAS pool id (optional)

try:
    # Lists all NAS shares.
    api_response = api_instance.index_nas_shares_by_nas(nas_id, limit=limit, offset=offset, sort_by=sort_by, id=id, path=path, options=options, username=username, nas_pool_id=nas_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->index_nas_shares_by_nas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_id** | **str**| Numeric ID or name of NAS. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **path** | **str**| Filter on path | [optional] 
 **options** | **str**| Filter on options | [optional] 
 **username** | **str**| Filter on username | [optional] 
 **nas_pool_id** | **str**| Filter on NAS pool id | [optional] 

### Return type

[**NasShareCollection**](NasShareCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of NAS shares. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_nas_shares_by_nas_pool**
> NasShareCollection index_nas_shares_by_nas_pool(nas_pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, path=path, options=options, username=username, nas_id=nas_id)

Lists all NAS shares.

**API Key Scope**: nas_shares / index   Optional API Key Explicit Scope: nas_shares / get_password

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
path = 'path_example' # str | Filter on path (optional)
options = 'options_example' # str | Filter on options (optional)
username = 'username_example' # str | Filter on username (optional)
nas_id = 'nas_id_example' # str | Filter on NAS id (optional)

try:
    # Lists all NAS shares.
    api_response = api_instance.index_nas_shares_by_nas_pool(nas_pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, path=path, options=options, username=username, nas_id=nas_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->index_nas_shares_by_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
path = 'path_example' # str | Filter on path (optional)
options = 'options_example' # str | Filter on options (optional)
username = 'username_example' # str | Filter on username (optional)
nas_id = 'nas_id_example' # str | Filter on NAS id (optional)

try:
    # Lists all NAS shares.
    api_response = api_instance.index_nas_shares_by_nas_pool(nas_pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, path=path, options=options, username=username, nas_id=nas_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->index_nas_shares_by_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **path** | **str**| Filter on path | [optional] 
 **options** | **str**| Filter on options | [optional] 
 **username** | **str**| Filter on username | [optional] 
 **nas_id** | **str**| Filter on NAS id | [optional] 

### Return type

[**NasShareCollection**](NasShareCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of NAS shares. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mount_status_nas_share**
> MountStatus mount_status_nas_share(nas_share_id)

Get mount status of NAS Share.

**API Key Scope**: nas_shares / mount_status

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Get mount status of NAS Share.
    api_response = api_instance.mount_status_nas_share(nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->mount_status_nas_share: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Get mount status of NAS Share.
    api_response = api_instance.mount_status_nas_share(nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->mount_status_nas_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_share_id** | **int**| Numeric ID of NAS share. | 

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

# **mount_status_nas_share_by_nas**
> MountStatus mount_status_nas_share_by_nas(nas_id, nas_share_id)

Get mount status of NAS Share.

**API Key Scope**: nas_shares / mount_status

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Get mount status of NAS Share.
    api_response = api_instance.mount_status_nas_share_by_nas(nas_id, nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->mount_status_nas_share_by_nas: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Get mount status of NAS Share.
    api_response = api_instance.mount_status_nas_share_by_nas(nas_id, nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->mount_status_nas_share_by_nas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_id** | **str**| Numeric ID or name of NAS. | 
 **nas_share_id** | **int**| Numeric ID of NAS share. | 

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

# **mount_status_nas_share_by_nas_pool**
> MountStatus mount_status_nas_share_by_nas_pool(nas_pool_id, nas_share_id)

Get mount status of NAS Share.

**API Key Scope**: nas_shares / mount_status

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Get mount status of NAS Share.
    api_response = api_instance.mount_status_nas_share_by_nas_pool(nas_pool_id, nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->mount_status_nas_share_by_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Get mount status of NAS Share.
    api_response = api_instance.mount_status_nas_share_by_nas_pool(nas_pool_id, nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->mount_status_nas_share_by_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 
 **nas_share_id** | **int**| Numeric ID of NAS share. | 

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

# **show_nas_share_by_nas**
> NasShare show_nas_share_by_nas(nas_id, nas_share_id)

Displays a specific NAS share.

**API Key Scope**: nas_shares / show   Optional API Key Explicit Scope: nas_shares / get_password

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Displays a specific NAS share.
    api_response = api_instance.show_nas_share_by_nas(nas_id, nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->show_nas_share_by_nas: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Displays a specific NAS share.
    api_response = api_instance.show_nas_share_by_nas(nas_id, nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->show_nas_share_by_nas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_id** | **str**| Numeric ID or name of NAS. | 
 **nas_share_id** | **int**| Numeric ID of NAS share. | 

### Return type

[**NasShare**](NasShare.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific NAS share. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_nas_shares**
> NasShare show_nas_shares(nas_share_id)

Displays a specific NAS share.

**API Key Scope**: nas_shares / show   Optional API Key Explicit Scope: nas_shares / get_password

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Displays a specific NAS share.
    api_response = api_instance.show_nas_shares(nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->show_nas_shares: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Displays a specific NAS share.
    api_response = api_instance.show_nas_shares(nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->show_nas_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_share_id** | **int**| Numeric ID of NAS share. | 

### Return type

[**NasShare**](NasShare.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific NAS share. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_nas_shares_by_nas_pool**
> NasShare show_nas_shares_by_nas_pool(nas_pool_id, nas_share_id)

Displays a specific NAS share.

**API Key Scope**: nas_shares / show   Optional API Key Explicit Scope: nas_shares / get_password

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Displays a specific NAS share.
    api_response = api_instance.show_nas_shares_by_nas_pool(nas_pool_id, nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->show_nas_shares_by_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_share_id = 56 # int | Numeric ID of NAS share.

try:
    # Displays a specific NAS share.
    api_response = api_instance.show_nas_shares_by_nas_pool(nas_pool_id, nas_share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->show_nas_shares_by_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 
 **nas_share_id** | **int**| Numeric ID of NAS share. | 

### Return type

[**NasShare**](NasShare.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific NAS share. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_nas_share**
> ActiveJobStatus test_nas_share(nas_id, nas_share_body)

Test an unsaved NAS Share.

**API Key Scope**: nas_shares / test

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Test an unsaved NAS Share.
    api_response = api_instance.test_nas_share(nas_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->test_nas_share: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Test an unsaved NAS Share.
    api_response = api_instance.test_nas_share(nas_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->test_nas_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_id** | **str**| Numeric ID or name of NAS. | 
 **nas_share_body** | [**NasShare**](NasShare.md)|  | 

### Return type

[**ActiveJobStatus**](ActiveJobStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, queued, working, failed

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | An active job that may be queued, working, completed or failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_nas_share**
> ActiveJobStatus test_result_nas_share(nas_id, job_id=job_id)

Check result of a NAS Share test job.

**API Key Scope**: nas_shares / test

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
job_id = 'job_id_example' # str | ID of active job (optional)

try:
    # Check result of a NAS Share test job.
    api_response = api_instance.test_result_nas_share(nas_id, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->test_result_nas_share: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
job_id = 'job_id_example' # str | ID of active job (optional)

try:
    # Check result of a NAS Share test job.
    api_response = api_instance.test_result_nas_share(nas_id, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->test_result_nas_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_id** | **str**| Numeric ID or name of NAS. | 
 **job_id** | **str**| ID of active job | [optional] 

### Return type

[**ActiveJobStatus**](ActiveJobStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, queued, working, failed

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An active job that may be queued, working, completed or failed. |  -  |
**202** | An active job that may be queued, working, completed or failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nas_share**
> NasShare update_nas_share(nas_share_id, nas_share_body)

Updates a specific NAS share.

**API Key Scope**: nas_shares / update

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_share_id = 56 # int | Numeric ID of NAS share.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Updates a specific NAS share.
    api_response = api_instance.update_nas_share(nas_share_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->update_nas_share: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_share_id = 56 # int | Numeric ID of NAS share.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Updates a specific NAS share.
    api_response = api_instance.update_nas_share(nas_share_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->update_nas_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_share_id** | **int**| Numeric ID of NAS share. | 
 **nas_share_body** | [**NasShare**](NasShare.md)|  | 

### Return type

[**NasShare**](NasShare.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific NAS share. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nas_share_by_nas**
> NasShare update_nas_share_by_nas(nas_id, nas_share_id, nas_share_body)

Updates a specific NAS share.

**API Key Scope**: nas_shares / update

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_id = 56 # int | Numeric ID of NAS share.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Updates a specific NAS share.
    api_response = api_instance.update_nas_share_by_nas(nas_id, nas_share_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->update_nas_share_by_nas: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_id = 'nas_id_example' # str | Numeric ID or name of NAS.
nas_share_id = 56 # int | Numeric ID of NAS share.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Updates a specific NAS share.
    api_response = api_instance.update_nas_share_by_nas(nas_id, nas_share_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->update_nas_share_by_nas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_id** | **str**| Numeric ID or name of NAS. | 
 **nas_share_id** | **int**| Numeric ID of NAS share. | 
 **nas_share_body** | [**NasShare**](NasShare.md)|  | 

### Return type

[**NasShare**](NasShare.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific NAS share. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nas_share_by_nas_pool**
> NasShare update_nas_share_by_nas_pool(nas_pool_id, nas_share_id, nas_share_body)

Updates a specific NAS share.

**API Key Scope**: nas_shares / update

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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_share_id = 56 # int | Numeric ID of NAS share.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Updates a specific NAS share.
    api_response = api_instance.update_nas_share_by_nas_pool(nas_pool_id, nas_share_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->update_nas_share_by_nas_pool: %s\n" % e)
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
api_instance = nodeum_sdk.NasSharesApi(nodeum_sdk.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
nas_share_id = 56 # int | Numeric ID of NAS share.
nas_share_body = nodeum_sdk.NasShare() # NasShare | 

try:
    # Updates a specific NAS share.
    api_response = api_instance.update_nas_share_by_nas_pool(nas_pool_id, nas_share_id, nas_share_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NasSharesApi->update_nas_share_by_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 
 **nas_share_id** | **int**| Numeric ID of NAS share. | 
 **nas_share_body** | [**NasShare**](NasShare.md)|  | 

### Return type

[**NasShare**](NasShare.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific NAS share. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

