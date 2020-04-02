# nodeum_sdk.FilesApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**files_children**](FilesApi.md#files_children) | **GET** /files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_container**](FilesApi.md#files_children_by_container) | **GET** /containers/{container_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_pool**](FilesApi.md#files_children_by_pool) | **GET** /pools/{pool_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_task**](FilesApi.md#files_children_by_task) | **GET** /tasks/{task_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_task_execution**](FilesApi.md#files_children_by_task_execution) | **GET** /task_executions/{task_execution_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**files_children_by_task_execution_by_task**](FilesApi.md#files_children_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files/{file_parent_id}/children | Lists files under a specific folder.
[**import_files_children_by_pool**](FilesApi.md#import_files_children_by_pool) | **GET** /pools/{pool_id}/import_files/{file_parent_id}/children | Lists files under a specific folder on tape of pools, specific for Data Exchange.
[**index_files**](FilesApi.md#index_files) | **GET** /files | Lists files on root.
[**index_files_by_container**](FilesApi.md#index_files_by_container) | **GET** /containers/{container_id}/files | Lists files on root.
[**index_files_by_pool**](FilesApi.md#index_files_by_pool) | **GET** /pools/{pool_id}/files | Lists files on root.
[**index_files_by_task**](FilesApi.md#index_files_by_task) | **GET** /tasks/{task_id}/files | Lists files on root.
[**index_files_by_task_execution**](FilesApi.md#index_files_by_task_execution) | **GET** /task_executions/{task_execution_id}/files | Lists files on root.
[**index_files_by_task_execution_by_task**](FilesApi.md#index_files_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files | Lists files on root.
[**index_import_files_by_pool**](FilesApi.md#index_import_files_by_pool) | **GET** /pools/{pool_id}/import_files | Lists files on root of tape of pools, specific for Data Exchange.
[**index_on_tapes_files_by_pool**](FilesApi.md#index_on_tapes_files_by_pool) | **GET** /pools/{pool_id}/on_tapes_files | Lists files on root of tape of pools, specific for Active and Offline.
[**index_tapes_by_file_by_pool**](FilesApi.md#index_tapes_by_file_by_pool) | **GET** /pools/{pool_id}/files/{file_id}/tapes | Displays tapes containing specific file, related to the specific pool.
[**index_tapes_by_file_by_task**](FilesApi.md#index_tapes_by_file_by_task) | **GET** /tasks/{task_id}/files/{file_id}/tapes | Displays tapes containing specific file, related to the specific task.
[**index_tapes_by_file_by_task_execution**](FilesApi.md#index_tapes_by_file_by_task_execution) | **GET** /task_executions/{task_execution_id}/files/{file_id}/tapes | Displays tapes containing specific file, related to the specific task.
[**index_tapes_by_file_by_task_execution_by_task**](FilesApi.md#index_tapes_by_file_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files/{file_id}/tapes | Displays tapes containing specific file, related to the specific task.
[**on_tapes_files_children_by_pool**](FilesApi.md#on_tapes_files_children_by_pool) | **GET** /pools/{pool_id}/on_tapes_files/{file_parent_id}/children | Lists files under a specific folder on tape of pools, specific for Active and Offline.
[**show_file**](FilesApi.md#show_file) | **GET** /files/{file_id} | Displays a specific file.
[**show_file_by_container**](FilesApi.md#show_file_by_container) | **GET** /containers/{container_id}/files/{file_id} | Displays a specific file.
[**show_file_by_pool**](FilesApi.md#show_file_by_pool) | **GET** /pools/{pool_id}/files/{file_id} | Displays a specific file.
[**show_file_by_task**](FilesApi.md#show_file_by_task) | **GET** /tasks/{task_id}/files/{file_id} | Displays a specific file.
[**show_file_by_task_execution**](FilesApi.md#show_file_by_task_execution) | **GET** /task_executions/{task_execution_id}/files/{file_id} | Displays a specific file.
[**show_file_by_task_execution_by_task**](FilesApi.md#show_file_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files/{file_id} | Displays a specific file.
[**show_import_file_by_pool**](FilesApi.md#show_import_file_by_pool) | **GET** /pools/{pool_id}/import_files/{file_id} | Displays a specific file on tape of pools, specific for Data Exchange.
[**show_on_tape_file_by_pool**](FilesApi.md#show_on_tape_file_by_pool) | **GET** /pools/{pool_id}/on_tapes_files/{file_id} | Displays a specific file on tape of pools, specific for Active and Offline.


# **files_children**
> NodeumFileCollection files_children(file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_container**
> NodeumFileCollection files_children_by_container(container_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_pool**
> NodeumFileCollection files_children_by_pool(pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
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
        api_response = api_instance.files_children_by_pool(pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->files_children_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
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
        api_response = api_instance.files_children_by_pool(pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->files_children_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_task**
> NodeumFileCollection files_children_by_task(task_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_task_execution**
> NodeumFileCollection files_children_by_task_execution(task_execution_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
 **task_execution_id** | **str**| Numeric ID of task execution. | 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **files_children_by_task_execution_by_task**
> NodeumFileCollection files_children_by_task_execution_by_task(task_id, task_execution_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
 **task_execution_id** | **str**| Numeric ID of task execution. | 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_files_children_by_pool**
> ImportFileCollection import_files_children_by_pool(pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files under a specific folder on tape of pools, specific for Data Exchange.

**API Key Scope**: import_files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
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
        # Lists files under a specific folder on tape of pools, specific for Data Exchange.
        api_response = api_instance.import_files_children_by_pool(pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->import_files_children_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
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
        # Lists files under a specific folder on tape of pools, specific for Data Exchange.
        api_response = api_instance.import_files_children_by_pool(pool_id, file_parent_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->import_files_children_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
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

[**ImportFileCollection**](ImportFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of imported files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files**
> NodeumFileCollection index_files(limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_container**
> NodeumFileCollection index_files_by_container(container_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_pool**
> NodeumFileCollection index_files_by_pool(pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
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
        api_response = api_instance.index_files_by_pool(pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_files_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
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
        api_response = api_instance.index_files_by_pool(pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_files_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_task**
> NodeumFileCollection index_files_by_task(task_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_task_execution**
> NodeumFileCollection index_files_by_task_execution(task_execution_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
 **task_execution_id** | **str**| Numeric ID of task execution. | 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files_by_task_execution_by_task**
> NodeumFileCollection index_files_by_task_execution_by_task(task_id, task_execution_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root.

**API Key Scope**: files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
 **task_execution_id** | **str**| Numeric ID of task execution. | 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_import_files_by_pool**
> ImportFileCollection index_import_files_by_pool(pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)

Lists files on root of tape of pools, specific for Data Exchange.

**API Key Scope**: import_files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
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
        # Lists files on root of tape of pools, specific for Data Exchange.
        api_response = api_instance.index_import_files_by_pool(pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_import_files_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
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
        # Lists files on root of tape of pools, specific for Data Exchange.
        api_response = api_instance.index_import_files_by_pool(pool_id, limit=limit, offset=offset, file_id=file_id, name=name, type=type, permission=permission, size=size, change_date=change_date, modification_date=modification_date, access_date=access_date, gid=gid, uid=uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_import_files_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
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

[**ImportFileCollection**](ImportFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of imported files. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_on_tapes_files_by_pool**
> OnTapesFileCollection index_on_tapes_files_by_pool(pool_id, limit=limit, offset=offset, name=name, type=type, size=size)

Lists files on root of tape of pools, specific for Active and Offline.

**API Key Scope**: on_tapes_files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
size = 'size_example' # str | Filter on size (optional)

    try:
        # Lists files on root of tape of pools, specific for Active and Offline.
        api_response = api_instance.index_on_tapes_files_by_pool(pool_id, limit=limit, offset=offset, name=name, type=type, size=size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_on_tapes_files_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
size = 'size_example' # str | Filter on size (optional)

    try:
        # Lists files on root of tape of pools, specific for Active and Offline.
        api_response = api_instance.index_on_tapes_files_by_pool(pool_id, limit=limit, offset=offset, name=name, type=type, size=size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_on_tapes_files_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **size** | **str**| Filter on size | [optional] 

### Return type

[**OnTapesFileCollection**](OnTapesFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files on tapes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tapes_by_file_by_pool**
> TapeCollection index_tapes_by_file_by_pool(pool_id, file_id)

Displays tapes containing specific file, related to the specific pool.

**API Key Scope**: files / tapes

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays tapes containing specific file, related to the specific pool.
        api_response = api_instance.index_tapes_by_file_by_pool(pool_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_tapes_by_file_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays tapes containing specific file, related to the specific pool.
        api_response = api_instance.index_tapes_by_file_by_pool(pool_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_tapes_by_file_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**TapeCollection**](TapeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tapes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tapes_by_file_by_task**
> TapeCollection index_tapes_by_file_by_task(task_id, file_id)

Displays tapes containing specific file, related to the specific task.

**API Key Scope**: files / tapes

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays tapes containing specific file, related to the specific task.
        api_response = api_instance.index_tapes_by_file_by_task(task_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_tapes_by_file_by_task: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays tapes containing specific file, related to the specific task.
        api_response = api_instance.index_tapes_by_file_by_task(task_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_tapes_by_file_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**TapeCollection**](TapeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tapes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tapes_by_file_by_task_execution**
> TapeCollection index_tapes_by_file_by_task_execution(task_execution_id, file_id)

Displays tapes containing specific file, related to the specific task.

**API Key Scope**: files / tapes

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays tapes containing specific file, related to the specific task.
        api_response = api_instance.index_tapes_by_file_by_task_execution(task_execution_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_tapes_by_file_by_task_execution: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays tapes containing specific file, related to the specific task.
        api_response = api_instance.index_tapes_by_file_by_task_execution(task_execution_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_tapes_by_file_by_task_execution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_execution_id** | **str**| Numeric ID of task execution. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**TapeCollection**](TapeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tapes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tapes_by_file_by_task_execution_by_task**
> TapeCollection index_tapes_by_file_by_task_execution_by_task(task_id, task_execution_id, file_id)

Displays tapes containing specific file, related to the specific task.

**API Key Scope**: files / tapes

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays tapes containing specific file, related to the specific task.
        api_response = api_instance.index_tapes_by_file_by_task_execution_by_task(task_id, task_execution_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_tapes_by_file_by_task_execution_by_task: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays tapes containing specific file, related to the specific task.
        api_response = api_instance.index_tapes_by_file_by_task_execution_by_task(task_id, task_execution_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->index_tapes_by_file_by_task_execution_by_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Numeric ID or name of task. Task names are not unique, it&#39;s recommanded to use numeric ID. | 
 **task_execution_id** | **str**| Numeric ID of task execution. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**TapeCollection**](TapeCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tapes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **on_tapes_files_children_by_pool**
> OnTapesFileCollection on_tapes_files_children_by_pool(pool_id, file_parent_id, limit=limit, offset=offset, name=name, type=type, size=size)

Lists files under a specific folder on tape of pools, specific for Active and Offline.

**API Key Scope**: on_tapes_files / index

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
size = 'size_example' # str | Filter on size (optional)

    try:
        # Lists files under a specific folder on tape of pools, specific for Active and Offline.
        api_response = api_instance.on_tapes_files_children_by_pool(pool_id, file_parent_id, limit=limit, offset=offset, name=name, type=type, size=size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->on_tapes_files_children_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_parent_id = 56 # int | Numeric ID of parent folder.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
name = 'name_example' # str | Filter on name (optional)
type = 'type_example' # str | Filter on type (optional)
size = 'size_example' # str | Filter on size (optional)

    try:
        # Lists files under a specific folder on tape of pools, specific for Active and Offline.
        api_response = api_instance.on_tapes_files_children_by_pool(pool_id, file_parent_id, limit=limit, offset=offset, name=name, type=type, size=size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->on_tapes_files_children_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **file_parent_id** | **int**| Numeric ID of parent folder. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **size** | **str**| Filter on size | [optional] 

### Return type

[**OnTapesFileCollection**](OnTapesFileCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of files on tapes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file**
> NodeumFileWithPath show_file(file_id)

Displays a specific file.

**API Key Scope**: files / show

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file.
        api_response = api_instance.show_file(file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_file: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_container**
> NodeumFileWithPath show_file_by_container(container_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    container_id = 'container_id_example' # str | Numeric ID or name of container.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file.
        api_response = api_instance.show_file_by_container(container_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_file_by_container: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_pool**
> NodeumFileWithPath show_file_by_pool(pool_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file.
        api_response = api_instance.show_file_by_pool(pool_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_file_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file.
        api_response = api_instance.show_file_by_pool(pool_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_file_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

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

# **show_file_by_task**
> NodeumFileWithPath show_file_by_task(task_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file.
        api_response = api_instance.show_file_by_task(task_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_file_by_task: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_file_by_task_execution**
> NodeumFileWithPath show_file_by_task_execution(task_execution_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file.
        api_response = api_instance.show_file_by_task_execution(task_execution_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_file_by_task_execution: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
 **task_execution_id** | **str**| Numeric ID of task execution. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

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

# **show_file_by_task_execution_by_task**
> NodeumFileWithPath show_file_by_task_execution_by_task(task_id, task_execution_id, file_id)

Displays a specific file.

**API Key Scope**: files / show

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file.
        api_response = api_instance.show_file_by_task_execution_by_task(task_id, task_execution_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_file_by_task_execution_by_task: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    task_id = 'task_id_example' # str | Numeric ID or name of task. Task names are not unique, it's recommanded to use numeric ID.
task_execution_id = 'task_execution_id_example' # str | Numeric ID of task execution.
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
 **task_execution_id** | **str**| Numeric ID of task execution. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**NodeumFileWithPath**](NodeumFileWithPath.md)

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

# **show_import_file_by_pool**
> ImportFileWithPath show_import_file_by_pool(pool_id, file_id)

Displays a specific file on tape of pools, specific for Data Exchange.

**API Key Scope**: import_files / show

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file on tape of pools, specific for Data Exchange.
        api_response = api_instance.show_import_file_by_pool(pool_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_import_file_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file on tape of pools, specific for Data Exchange.
        api_response = api_instance.show_import_file_by_pool(pool_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_import_file_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**ImportFileWithPath**](ImportFileWithPath.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific imported file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_on_tape_file_by_pool**
> OnTapesFile show_on_tape_file_by_pool(pool_id, file_id)

Displays a specific file on tape of pools, specific for Active and Offline.

**API Key Scope**: on_tapes_files / show

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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file on tape of pools, specific for Active and Offline.
        api_response = api_instance.show_on_tape_file_by_pool(pool_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_on_tape_file_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.FilesApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
file_id = 56 # int | Numeric ID of file.

    try:
        # Displays a specific file on tape of pools, specific for Active and Offline.
        api_response = api_instance.show_on_tape_file_by_pool(pool_id, file_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FilesApi->show_on_tape_file_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **file_id** | **int**| Numeric ID of file. | 

### Return type

[**OnTapesFile**](OnTapesFile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific file on tapes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

