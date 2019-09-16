# swagger_client.ContainersApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_container**](ContainersApi.md#create_container) | **POST** /containers | Creates a new container.
[**create_container_privilege**](ContainersApi.md#create_container_privilege) | **POST** /containers/{container_id}/container_privileges | Creates a new privilege on the container.
[**destroy_container**](ContainersApi.md#destroy_container) | **DELETE** /containers/{container_id} | Destroys a specific container.
[**destroy_container_privilege**](ContainersApi.md#destroy_container_privilege) | **DELETE** /containers/{container_id}/container_privileges/{container_privilege_id} | Destroys a specific privilege.
[**index_container_privileges**](ContainersApi.md#index_container_privileges) | **GET** /containers/{container_id}/container_privileges | Lists all privilege on the container.
[**index_containers**](ContainersApi.md#index_containers) | **GET** /containers | Lists all containers.
[**show_container**](ContainersApi.md#show_container) | **GET** /containers/{container_id} | Displays a specific container.
[**show_container_privilege**](ContainersApi.md#show_container_privilege) | **GET** /containers/{container_id}/container_privileges/{container_privilege_id} | Displays a specific privilege.
[**update_container**](ContainersApi.md#update_container) | **PUT** /containers/{container_id} | Updates a specific container.
[**update_container_privilege**](ContainersApi.md#update_container_privilege) | **PUT** /containers/{container_id}/container_privileges/{container_privilege_id} | Updates a specific privilege.


# **create_container**
> Container create_container(container_body)

Creates a new container.

It **does not** yet create the file structure and configure the samba connection. Use API v1 instead.  **API Key Scope**: containers / create

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
container_body = swagger_client.Container() # Container | 

try:
    # Creates a new container.
    api_response = api_instance.create_container(container_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->create_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_body** | [**Container**](Container.md)|  | 

### Return type

[**Container**](Container.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_container_privilege**
> ContainerPrivilege create_container_privilege(container_id, container_privilege_body)

Creates a new privilege on the container.

**API Key Scope**: container_privileges / create

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.
container_privilege_body = swagger_client.ContainerPrivilege() # ContainerPrivilege | 

try:
    # Creates a new privilege on the container.
    api_response = api_instance.create_container_privilege(container_id, container_privilege_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->create_container_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 
 **container_privilege_body** | [**ContainerPrivilege**](ContainerPrivilege.md)|  | 

### Return type

[**ContainerPrivilege**](ContainerPrivilege.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_container**
> destroy_container(container_id)

Destroys a specific container.

**API Key Scope**: containers / destroy

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.

try:
    # Destroys a specific container.
    api_instance.destroy_container(container_id)
except ApiException as e:
    print("Exception when calling ContainersApi->destroy_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_container_privilege**
> destroy_container_privilege(container_id, container_privilege_id)

Destroys a specific privilege.

**API Key Scope**: container_privileges / destroy

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.
container_privilege_id = 56 # int | Numeric ID of container privilege.

try:
    # Destroys a specific privilege.
    api_instance.destroy_container_privilege(container_id, container_privilege_id)
except ApiException as e:
    print("Exception when calling ContainersApi->destroy_container_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 
 **container_privilege_id** | **int**| Numeric ID of container privilege. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_container_privileges**
> ContainerPrivilegeCollection index_container_privileges(container_id, limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, privilege=privilege, type=type)

Lists all privilege on the container.

**API Key Scope**: container_privileges / index

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
privilege = 'privilege_example' # str | Filter on privilege (optional)
type = 'type_example' # str | Filter on type (optional)

try:
    # Lists all privilege on the container.
    api_response = api_instance.index_container_privileges(container_id, limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, privilege=privilege, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->index_container_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **privilege** | **str**| Filter on privilege | [optional] 
 **type** | **str**| Filter on type | [optional] 

### Return type

[**ContainerPrivilegeCollection**](ContainerPrivilegeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_containers**
> ContainerCollection index_containers(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, quota_total_size=quota_total_size, quota_on_cache=quota_on_cache, stat_total_files=stat_total_files, stat_total_size=stat_total_size, stat_size_on_cache=stat_size_on_cache, guest_right=guest_right, last_update=last_update)

Lists all containers.

**API Key Scope**: containers / index

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
comment = 'comment_example' # str | Filter on comment (optional)
quota_total_size = 'quota_total_size_example' # str | Filter on quota total size (optional)
quota_on_cache = 'quota_on_cache_example' # str | Filter on quota on cache (optional)
stat_total_files = 'stat_total_files_example' # str | Filter on stat total files (optional)
stat_total_size = 'stat_total_size_example' # str | Filter on stat total size (optional)
stat_size_on_cache = 'stat_size_on_cache_example' # str | Filter on stat size on cache (optional)
guest_right = 'guest_right_example' # str | Filter on guest right (optional)
last_update = 'last_update_example' # str | Filter on last update (optional)

try:
    # Lists all containers.
    api_response = api_instance.index_containers(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, quota_total_size=quota_total_size, quota_on_cache=quota_on_cache, stat_total_files=stat_total_files, stat_total_size=stat_total_size, stat_size_on_cache=stat_size_on_cache, guest_right=guest_right, last_update=last_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->index_containers: %s\n" % e)
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
 **quota_total_size** | **str**| Filter on quota total size | [optional] 
 **quota_on_cache** | **str**| Filter on quota on cache | [optional] 
 **stat_total_files** | **str**| Filter on stat total files | [optional] 
 **stat_total_size** | **str**| Filter on stat total size | [optional] 
 **stat_size_on_cache** | **str**| Filter on stat size on cache | [optional] 
 **guest_right** | **str**| Filter on guest right | [optional] 
 **last_update** | **str**| Filter on last update | [optional] 

### Return type

[**ContainerCollection**](ContainerCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_container**
> Container show_container(container_id)

Displays a specific container.

**API Key Scope**: containers / show

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.

try:
    # Displays a specific container.
    api_response = api_instance.show_container(container_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->show_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 

### Return type

[**Container**](Container.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_container_privilege**
> ContainerPrivilege show_container_privilege(container_id, container_privilege_id)

Displays a specific privilege.

**API Key Scope**: container_privileges / show

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.
container_privilege_id = 56 # int | Numeric ID of container privilege.

try:
    # Displays a specific privilege.
    api_response = api_instance.show_container_privilege(container_id, container_privilege_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->show_container_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 
 **container_privilege_id** | **int**| Numeric ID of container privilege. | 

### Return type

[**ContainerPrivilege**](ContainerPrivilege.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_container**
> Container update_container(container_id, container_body)

Updates a specific container.

It **does not** yet create the file structure and configure the samba connection. Use API v1 instead.  **API Key Scope**: containers / update

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.
container_body = swagger_client.Container() # Container | 

try:
    # Updates a specific container.
    api_response = api_instance.update_container(container_id, container_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->update_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 
 **container_body** | [**Container**](Container.md)|  | 

### Return type

[**Container**](Container.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_container_privilege**
> ContainerPrivilege update_container_privilege(container_id, container_privilege_id, container_privilege_body)

Updates a specific privilege.

**API Key Scope**: container_privileges / update

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
api_instance = swagger_client.ContainersApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.
container_privilege_id = 56 # int | Numeric ID of container privilege.
container_privilege_body = swagger_client.ContainerPrivilege() # ContainerPrivilege | 

try:
    # Updates a specific privilege.
    api_response = api_instance.update_container_privilege(container_id, container_privilege_id, container_privilege_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContainersApi->update_container_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 
 **container_privilege_id** | **int**| Numeric ID of container privilege. | 
 **container_privilege_body** | [**ContainerPrivilege**](ContainerPrivilege.md)|  | 

### Return type

[**ContainerPrivilege**](ContainerPrivilege.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

