# swagger_client.FilesApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_children**](FilesApi.md#files_children) | **GET** /files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_cloud_pool**](FilesApi.md#files_children_by_cloud_pool) | **GET** /cloud_pools/{cloud_pool_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_container**](FilesApi.md#files_children_by_container) | **GET** /containers/{container_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_nas_pool**](FilesApi.md#files_children_by_nas_pool) | **GET** /nas_pools/{nas_pool_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_tape_pool**](FilesApi.md#files_children_by_tape_pool) | **GET** /tape_pools/{tape_pool_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_task**](FilesApi.md#files_children_by_task) | **GET** /tasks/{task_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_task_execution**](FilesApi.md#files_children_by_task_execution) | **GET** /task_executions/{task_execution_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_task_execution_by_task**](FilesApi.md#files_children_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**index_files**](FilesApi.md#index_files) | **GET** /files | Lists files on root.
[**index_files_by_cloud_pool**](FilesApi.md#index_files_by_cloud_pool) | **GET** /cloud_pools/{cloud_pool_id}/files | Lists files on root.
[**index_files_by_container**](FilesApi.md#index_files_by_container) | **GET** /containers/{container_id}/files | Lists files on root.
[**index_files_by_nas_pool**](FilesApi.md#index_files_by_nas_pool) | **GET** /nas_pools/{nas_pool_id}/files | Lists files on root.
[**index_files_by_tape_pool**](FilesApi.md#index_files_by_tape_pool) | **GET** /tape_pools/{tape_pool_id}/files | Lists files on root.
[**index_files_by_task**](FilesApi.md#index_files_by_task) | **GET** /tasks/{task_id}/files | Lists files on root.
[**index_files_by_task_execution**](FilesApi.md#index_files_by_task_execution) | **GET** /task_executions/{task_execution_id}/files | Lists files on root.
[**index_files_by_task_execution_by_task**](FilesApi.md#index_files_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files | Lists files on root.
[**show_file**](FilesApi.md#show_file) | **GET** /files/{file_id} | Displays a specific file.
[**show_file_by_cloud_pool**](FilesApi.md#show_file_by_cloud_pool) | **GET** /cloud_pools/{cloud_pool_id}/files/{file_id} | Displays a specific file.
[**show_file_by_container**](FilesApi.md#show_file_by_container) | **GET** /containers/{container_id}/files/{file_id} | Displays a specific file.
[**show_file_by_nas_pool**](FilesApi.md#show_file_by_nas_pool) | **GET** /nas_pools/{nas_pool_id}/files/{file_id} | Displays a specific file.
[**show_file_by_tape_pool**](FilesApi.md#show_file_by_tape_pool) | **GET** /tape_pools/{tape_pool_id}/files/{file_id} | Displays a specific file.
[**show_file_by_task**](FilesApi.md#show_file_by_task) | **GET** /tasks/{task_id}/files/{file_id} | Displays a specific file.
[**show_file_by_task_execution**](FilesApi.md#show_file_by_task_execution) | **GET** /task_executions/{task_execution_id}/files/{file_id} | Displays a specific file.
[**show_file_by_task_execution_by_task**](FilesApi.md#show_file_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files/{file_id} | Displays a specific file.


# **files_children**
> NodeumFileCollection files_children(file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files under a specific folder.
    api_response = api_instance.files_children(file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_parent_id** | **int**| Numeric ID of parent folder. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_cloud_pool**
> NodeumFileCollection files_children_by_cloud_pool(cloud_pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files under a specific folder.
    api_response = api_instance.files_children_by_cloud_pool(cloud_pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_children_by_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Numeric ID or name of cloud pool. | 
 **file_parent_id** | **int**| Numeric ID of parent folder. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_container**
> NodeumFileCollection files_children_by_container(container_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files under a specific folder.
    api_response = api_instance.files_children_by_container(container_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_children_by_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 
 **file_parent_id** | **int**| Numeric ID of parent folder. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_nas_pool**
> NodeumFileCollection files_children_by_nas_pool(nas_pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files under a specific folder.
    api_response = api_instance.files_children_by_nas_pool(nas_pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_children_by_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 
 **file_parent_id** | **int**| Numeric ID of parent folder. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_tape_pool**
> NodeumFileCollection files_children_by_tape_pool(tape_pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files under a specific folder.
    api_response = api_instance.files_children_by_tape_pool(tape_pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_children_by_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_id** | **str**| Numeric ID, or name of tape pool. | 
 **file_parent_id** | **int**| Numeric ID of parent folder. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_task**
> NodeumFileCollection files_children_by_task(task_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files under a specific folder.
    api_response = api_instance.files_children_by_task(task_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_children_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **file_parent_id** | **int**| Numeric ID of parent folder. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_task_execution**
> NodeumFileCollection files_children_by_task_execution(task_execution_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
task_execution_id = 789 # int | Numeric ID of task execution.
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files under a specific folder.
    api_response = api_instance.files_children_by_task_execution(task_execution_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_children_by_task_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_execution_id** | **int**| Numeric ID of task execution. | 
 **file_parent_id** | **int**| Numeric ID of parent folder. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_task_execution_by_task**
> NodeumFileCollection files_children_by_task_execution_by_task(task_id, task_execution_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 789 # int | Numeric ID of task execution.
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files under a specific folder.
    api_response = api_instance.files_children_by_task_execution_by_task(task_id, task_execution_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->files_children_by_task_execution_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_execution_id** | **int**| Numeric ID of task execution. | 
 **file_parent_id** | **int**| Numeric ID of parent folder. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files**
> NodeumFileCollection index_files(limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files on root.
    api_response = api_instance.index_files(limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->index_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_cloud_pool**
> NodeumFileCollection index_files_by_cloud_pool(cloud_pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files on root.
    api_response = api_instance.index_files_by_cloud_pool(cloud_pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->index_files_by_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Numeric ID or name of cloud pool. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_container**
> NodeumFileCollection index_files_by_container(container_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files on root.
    api_response = api_instance.index_files_by_container(container_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->index_files_by_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_nas_pool**
> NodeumFileCollection index_files_by_nas_pool(nas_pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files on root.
    api_response = api_instance.index_files_by_nas_pool(nas_pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->index_files_by_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_tape_pool**
> NodeumFileCollection index_files_by_tape_pool(tape_pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files on root.
    api_response = api_instance.index_files_by_tape_pool(tape_pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->index_files_by_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_id** | **str**| Numeric ID, or name of tape pool. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_task**
> NodeumFileCollection index_files_by_task(task_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files on root.
    api_response = api_instance.index_files_by_task(task_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->index_files_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_task_execution**
> NodeumFileCollection index_files_by_task_execution(task_execution_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
task_execution_id = 789 # int | Numeric ID of task execution.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files on root.
    api_response = api_instance.index_files_by_task_execution(task_execution_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->index_files_by_task_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_execution_id** | **int**| Numeric ID of task execution. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_task_execution_by_task**
> NodeumFileCollection index_files_by_task_execution_by_task(task_id, task_execution_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 789 # int | Numeric ID of task execution.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
file_id = 'file_id_example' # str | Filter on file id (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
permission = 'permission_example' # str | Filter on permission (optional)
size = 'size_example' # str | Filter on size (optional)
change_date = 'change_date_example' # str | Filter on change date (optional)
modification_date = 'modification_date_example' # str | Filter on modification date (optional)
access_date = 'access_date_example' # str | Filter on access date (optional)
gid = 'gid_example' # str | Filter on gid (optional)
uid = 'uid_example' # str | Filter on uid (optional)

try:
    # Lists files on root.
    api_response = api_instance.index_files_by_task_execution_by_task(task_id, task_execution_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->index_files_by_task_execution_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_execution_id** | **int**| Numeric ID of task execution. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **file_id** | **str**| Filter on file id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **permission** | **str**| Filter on permission | [optional] 
 **size** | **str**| Filter on size | [optional] 
 **change_date** | **str**| Filter on change date | [optional] 
 **modification_date** | **str**| Filter on modification date | [optional] 
 **access_date** | **str**| Filter on access date | [optional] 
 **gid** | **str**| Filter on gid | [optional] 
 **uid** | **str**| Filter on uid | [optional] 

### Return type

[**NodeumFileCollection**](NodeumFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file**
> NodeumFileWithPath show_file(file_id)

Displays a specific file.

**API Key Scope**: files / show

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
file_id = 56 # int | Numeric ID of file.

try:
    # Displays a specific file.
    api_response = api_instance.show_file(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->show_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_cloud_pool**
> NodeumFileWithPath show_file_by_cloud_pool(cloud_pool_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.
file_id = 56 # int | Numeric ID of file.

try:
    # Displays a specific file.
    api_response = api_instance.show_file_by_cloud_pool(cloud_pool_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->show_file_by_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Numeric ID or name of cloud pool. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_container**
> NodeumFileWithPath show_file_by_container(container_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
container_id = 'container_id_example' # str | Numeric ID or name of container.
file_id = 56 # int | Numeric ID of file.

try:
    # Displays a specific file.
    api_response = api_instance.show_file_by_container(container_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->show_file_by_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Numeric ID or name of container. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_nas_pool**
> NodeumFileWithPath show_file_by_nas_pool(nas_pool_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
nas_pool_id = 'nas_pool_id_example' # str | Numeric ID or name of NAS pool.
file_id = 56 # int | Numeric ID of file.

try:
    # Displays a specific file.
    api_response = api_instance.show_file_by_nas_pool(nas_pool_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->show_file_by_nas_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nas_pool_id** | **str**| Numeric ID or name of NAS pool. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_tape_pool**
> NodeumFileWithPath show_file_by_tape_pool(tape_pool_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
file_id = 56 # int | Numeric ID of file.

try:
    # Displays a specific file.
    api_response = api_instance.show_file_by_tape_pool(tape_pool_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->show_file_by_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_id** | **str**| Numeric ID, or name of tape pool. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_task**
> NodeumFileWithPath show_file_by_task(task_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
file_id = 56 # int | Numeric ID of file.

try:
    # Displays a specific file.
    api_response = api_instance.show_file_by_task(task_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->show_file_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_task_execution**
> NodeumFileWithPath show_file_by_task_execution(task_execution_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
task_execution_id = 789 # int | Numeric ID of task execution.
file_id = 56 # int | Numeric ID of file.

try:
    # Displays a specific file.
    api_response = api_instance.show_file_by_task_execution(task_execution_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->show_file_by_task_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_execution_id** | **int**| Numeric ID of task execution. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_task_execution_by_task**
> NodeumFileWithPath show_file_by_task_execution_by_task(task_id, task_execution_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 789 # int | Numeric ID of task execution.
file_id = 56 # int | Numeric ID of file.

try:
    # Displays a specific file.
    api_response = api_instance.show_file_by_task_execution_by_task(task_id, task_execution_id, file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->show_file_by_task_execution_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_execution_id** | **int**| Numeric ID of task execution. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

