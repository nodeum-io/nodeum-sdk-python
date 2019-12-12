# nodeum_sdk.MountPointsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mount_point**](MountPointsApi.md#create_mount_point) | **POST** /mount_points | Creates a new mount point.
[**destroy_mount_point**](MountPointsApi.md#destroy_mount_point) | **DELETE** /mount_points/{mount_point_id} | Destroys a specific mount point.
[**index_mount_points**](MountPointsApi.md#index_mount_points) | **GET** /mount_points | Lists all mount points.
[**mount_mount_point**](MountPointsApi.md#mount_mount_point) | **PUT** /mount_points/{mount_point_id}/mount | Mount Mount Point.
[**mount_status_mount_point**](MountPointsApi.md#mount_status_mount_point) | **GET** /mount_points/{mount_point_id}/mount | Get mount status of Mount Point.
[**show_mount_point**](MountPointsApi.md#show_mount_point) | **GET** /mount_points/{mount_point_id} | Displays a specific mount point&#x60;.
[**unmount_mount_point**](MountPointsApi.md#unmount_mount_point) | **DELETE** /mount_points/{mount_point_id}/mount | Unmount Mount Point.
[**update_mount_point**](MountPointsApi.md#update_mount_point) | **PUT** /mount_points/{mount_point_id} | Updates a specific mount point&#x60;.


# **create_mount_point**
> MountPoint create_mount_point(mount_point_body)

Creates a new mount point.

It **does not** create and mount the file structure. Use API v1 instead.  **API Key Scope**: mount_points / create

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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_body = nodeum_sdk.MountPoint() # MountPoint | 

try:
    # Creates a new mount point.
    api_response = api_instance.create_mount_point(mount_point_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->create_mount_point: %s\n" % e)
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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_body = nodeum_sdk.MountPoint() # MountPoint | 

try:
    # Creates a new mount point.
    api_response = api_instance.create_mount_point(mount_point_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->create_mount_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_point_body** | [**MountPoint**](MountPoint.md)|  | 

### Return type

[**MountPoint**](MountPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific mount point. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_mount_point**
> destroy_mount_point(mount_point_id)

Destroys a specific mount point.

**API Key Scope**: mount_points / destroy

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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Destroys a specific mount point.
    api_instance.destroy_mount_point(mount_point_id)
except ApiException as e:
    print("Exception when calling MountPointsApi->destroy_mount_point: %s\n" % e)
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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Destroys a specific mount point.
    api_instance.destroy_mount_point(mount_point_id)
except ApiException as e:
    print("Exception when calling MountPointsApi->destroy_mount_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_point_id** | **str**| Numeric ID or name of mount point. | 

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
**204** | Mount point destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_mount_points**
> MountPointCollection index_mount_points(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, target=target, type=type, options=options, username=username, comment=comment, scan_interval=scan_interval, price=price)

Lists all mount points.

**API Key Scope**: mount_points / index   Optional API Key Explicit Scope: mount_points / get_password

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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
target = 'target_example' # str | Filter on mount point target (optional)
type = 'type_example' # str | Filter on type (optional)
options = 'options_example' # str | Filter on options (optional)
username = 'username_example' # str | Filter on username (optional)
comment = 'comment_example' # str | Filter on comment (optional)
scan_interval = 'scan_interval_example' # str | Filter on mount point scan interval (optional)
price = 'price_example' # str | Filter on price (optional)

try:
    # Lists all mount points.
    api_response = api_instance.index_mount_points(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, target=target, type=type, options=options, username=username, comment=comment, scan_interval=scan_interval, price=price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->index_mount_points: %s\n" % e)
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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
target = 'target_example' # str | Filter on mount point target (optional)
type = 'type_example' # str | Filter on type (optional)
options = 'options_example' # str | Filter on options (optional)
username = 'username_example' # str | Filter on username (optional)
comment = 'comment_example' # str | Filter on comment (optional)
scan_interval = 'scan_interval_example' # str | Filter on mount point scan interval (optional)
price = 'price_example' # str | Filter on price (optional)

try:
    # Lists all mount points.
    api_response = api_instance.index_mount_points(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, target=target, type=type, options=options, username=username, comment=comment, scan_interval=scan_interval, price=price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->index_mount_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **target** | **str**| Filter on mount point target | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **options** | **str**| Filter on options | [optional] 
 **username** | **str**| Filter on username | [optional] 
 **comment** | **str**| Filter on comment | [optional] 
 **scan_interval** | **str**| Filter on mount point scan interval | [optional] 
 **price** | **str**| Filter on price | [optional] 

### Return type

[**MountPointCollection**](MountPointCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of mount points. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mount_mount_point**
> MountStatus mount_mount_point(mount_point_id)

Mount Mount Point.

**API Key Scope**: mount_points / mount

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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Mount Mount Point.
    api_response = api_instance.mount_mount_point(mount_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->mount_mount_point: %s\n" % e)
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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Mount Mount Point.
    api_response = api_instance.mount_mount_point(mount_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->mount_mount_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_point_id** | **str**| Numeric ID or name of mount point. | 

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

# **mount_status_mount_point**
> MountStatus mount_status_mount_point(mount_point_id)

Get mount status of Mount Point.

**API Key Scope**: mount_points / mount_status

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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Get mount status of Mount Point.
    api_response = api_instance.mount_status_mount_point(mount_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->mount_status_mount_point: %s\n" % e)
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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Get mount status of Mount Point.
    api_response = api_instance.mount_status_mount_point(mount_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->mount_status_mount_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_point_id** | **str**| Numeric ID or name of mount point. | 

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

# **show_mount_point**
> MountPoint show_mount_point(mount_point_id)

Displays a specific mount point`.

**API Key Scope**: mount_points / show   Optional API Key Explicit Scope: mount_points / get_password

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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Displays a specific mount point`.
    api_response = api_instance.show_mount_point(mount_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->show_mount_point: %s\n" % e)
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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Displays a specific mount point`.
    api_response = api_instance.show_mount_point(mount_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->show_mount_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_point_id** | **str**| Numeric ID or name of mount point. | 

### Return type

[**MountPoint**](MountPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific mount point. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmount_mount_point**
> MountStatus unmount_mount_point(mount_point_id)

Unmount Mount Point.

**API Key Scope**: mount_points / unmount

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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Unmount Mount Point.
    api_response = api_instance.unmount_mount_point(mount_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->unmount_mount_point: %s\n" % e)
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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.

try:
    # Unmount Mount Point.
    api_response = api_instance.unmount_mount_point(mount_point_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->unmount_mount_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_point_id** | **str**| Numeric ID or name of mount point. | 

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

# **update_mount_point**
> MountPoint update_mount_point(mount_point_id, mount_point_body)

Updates a specific mount point`.

It **does not** create and mount the file structure. Use API v1 instead.  **API Key Scope**: mount_points / update

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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.
mount_point_body = nodeum_sdk.MountPoint() # MountPoint | 

try:
    # Updates a specific mount point`.
    api_response = api_instance.update_mount_point(mount_point_id, mount_point_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->update_mount_point: %s\n" % e)
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
api_instance = nodeum_sdk.MountPointsApi(nodeum_sdk.ApiClient(configuration))
mount_point_id = 'mount_point_id_example' # str | Numeric ID or name of mount point.
mount_point_body = nodeum_sdk.MountPoint() # MountPoint | 

try:
    # Updates a specific mount point`.
    api_response = api_instance.update_mount_point(mount_point_id, mount_point_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountPointsApi->update_mount_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mount_point_id** | **str**| Numeric ID or name of mount point. | 
 **mount_point_body** | [**MountPoint**](MountPoint.md)|  | 

### Return type

[**MountPoint**](MountPoint.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific mount point. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

