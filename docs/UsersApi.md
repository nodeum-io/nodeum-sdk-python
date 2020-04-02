# nodeum_sdk.UsersApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](UsersApi.md#create_api_key) | **POST** /users/me/api_keys | Creates a new API Key for current user.
[**destroy_api_key**](UsersApi.md#destroy_api_key) | **DELETE** /users/me/api_keys/{api_key_id} | Destroys a specific API Key.
[**index_api_keys**](UsersApi.md#index_api_keys) | **GET** /users/me/api_keys | Lists all API keys of current user.
[**index_system_groups**](UsersApi.md#index_system_groups) | **GET** /groups/-/systems | List all system groups.
[**index_system_users**](UsersApi.md#index_system_users) | **GET** /users/-/systems | List all system users.
[**show_api_key**](UsersApi.md#show_api_key) | **GET** /users/me/api_keys/{api_key_id} | Displays a specific API Key with its scopes.
[**update_api_key**](UsersApi.md#update_api_key) | **PUT** /users/me/api_keys/{api_key_id} | Updates a specific API Key.


# **create_api_key**
> ApiKeyFull create_api_key(api_key_body)

Creates a new API Key for current user.

**API Key Scope**: api_keys / create

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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    api_key_body = nodeum_sdk.ApiKeyFull() # ApiKeyFull | 

    try:
        # Creates a new API Key for current user.
        api_response = api_instance.create_api_key(api_key_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_api_key: %s\n" % e)
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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    api_key_body = nodeum_sdk.ApiKeyFull() # ApiKeyFull | 

    try:
        # Creates a new API Key for current user.
        api_response = api_instance.create_api_key(api_key_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_body** | [**ApiKeyFull**](ApiKeyFull.md)|  | 

### Return type

[**ApiKeyFull**](ApiKeyFull.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_api_key**
> destroy_api_key(api_key_id)

Destroys a specific API Key.

**API Key Scope**: api_keys / destroy

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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    api_key_id = 56 # int | Numeric ID of API Key.

    try:
        # Destroys a specific API Key.
        api_instance.destroy_api_key(api_key_id)
    except ApiException as e:
        print("Exception when calling UsersApi->destroy_api_key: %s\n" % e)
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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    api_key_id = 56 # int | Numeric ID of API Key.

    try:
        # Destroys a specific API Key.
        api_instance.destroy_api_key(api_key_id)
    except ApiException as e:
        print("Exception when calling UsersApi->destroy_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**| Numeric ID of API Key. | 

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
**204** | API Key destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_api_keys**
> ApiKeyCollection index_api_keys(limit=limit, offset=offset)

Lists all API keys of current user.

**API Key Scope**: api_keys / index

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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)

    try:
        # Lists all API keys of current user.
        api_response = api_instance.index_api_keys(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->index_api_keys: %s\n" % e)
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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)

    try:
        # Lists all API keys of current user.
        api_response = api_instance.index_api_keys(limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->index_api_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 

### Return type

[**ApiKeyCollection**](ApiKeyCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of API Keys. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_system_groups**
> SystemGroupCollection index_system_groups()

List all system groups.

**API Key Scope**: groups / systems

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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    
    try:
        # List all system groups.
        api_response = api_instance.index_system_groups()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->index_system_groups: %s\n" % e)
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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    
    try:
        # List all system groups.
        api_response = api_instance.index_system_groups()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->index_system_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemGroupCollection**](SystemGroupCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_system_users**
> SystemUserCollection index_system_users()

List all system users.

**API Key Scope**: users / systems

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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    
    try:
        # List all system users.
        api_response = api_instance.index_system_users()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->index_system_users: %s\n" % e)
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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    
    try:
        # List all system users.
        api_response = api_instance.index_system_users()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->index_system_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemUserCollection**](SystemUserCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_api_key**
> ApiKeyFull show_api_key(api_key_id)

Displays a specific API Key with its scopes.

**API Key Scope**: api_keys / show

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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    api_key_id = 56 # int | Numeric ID of API Key.

    try:
        # Displays a specific API Key with its scopes.
        api_response = api_instance.show_api_key(api_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->show_api_key: %s\n" % e)
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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    api_key_id = 56 # int | Numeric ID of API Key.

    try:
        # Displays a specific API Key with its scopes.
        api_response = api_instance.show_api_key(api_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->show_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**| Numeric ID of API Key. | 

### Return type

[**ApiKeyFull**](ApiKeyFull.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_key**
> ApiKeyFull update_api_key(api_key_id, api_key_body)

Updates a specific API Key.

**API Key Scope**: api_keys / update

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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    api_key_id = 56 # int | Numeric ID of API Key.
api_key_body = nodeum_sdk.ApiKeyFull() # ApiKeyFull | 

    try:
        # Updates a specific API Key.
        api_response = api_instance.update_api_key(api_key_id, api_key_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update_api_key: %s\n" % e)
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

# Enter a context with an instance of the API client
with nodeum_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = nodeum_sdk.UsersApi(api_client)
    api_key_id = 56 # int | Numeric ID of API Key.
api_key_body = nodeum_sdk.ApiKeyFull() # ApiKeyFull | 

    try:
        # Updates a specific API Key.
        api_response = api_instance.update_api_key(api_key_id, api_key_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_id** | **int**| Numeric ID of API Key. | 
 **api_key_body** | [**ApiKeyFull**](ApiKeyFull.md)|  | 

### Return type

[**ApiKeyFull**](ApiKeyFull.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

