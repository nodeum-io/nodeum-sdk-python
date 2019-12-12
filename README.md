# nodeum-sdk
# About  This document describes the Nodeum API version 2:  If you are looking for any information about the product itself, reach the product website https://www.nodeum.io. You can also contact us at this email address : info@nodeum.io  # Filter parameters When browsing a list of items, multiple filter parameters may be applied. Some operators can be added to the value as a prefix:  - `=` value is equal. Default operator, may be omitted  - `!=` value is different  - `>` greater than  - `>=` greater than or equal  - `<` lower than  - `>=` lower than or equal  - `><` included in list, items should be separated by `|`  - `!><` not included in list, items should be separated by `|`  - `~` pattern matching, may include `%` (any characters) and `_` (one character)  - `!~` pattern not matching, may include `%` (any characters) and `_` (one character)  

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.1.0
- Package version: 1.84.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import nodeum_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import nodeum_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = nodeum_sdk.CloudBucketsApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
cloud_connector_id = 'cloud_connector_id_example' # str | Filter on cloud connector id (optional)
pool_id = 'pool_id_example' # str | Filter on a pool id (optional)
name = 'name_example' # str | Filter on name (optional)
location = 'location_example' # str | Filter on location (optional)
price = 'price_example' # str | Filter on price (optional)

try:
    # Lists all cloud buckets.
    api_response = api_instance.index_cloud_buckets(limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_connector_id=cloud_connector_id, pool_id=pool_id, name=name, location=location, price=price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudBucketsApi->index_cloud_buckets: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CloudBucketsApi* | [**index_cloud_buckets**](docs/CloudBucketsApi.md#index_cloud_buckets) | **GET** /cloud_buckets | Lists all cloud buckets.
*CloudBucketsApi* | [**index_cloud_buckets_by_cloud_connector**](docs/CloudBucketsApi.md#index_cloud_buckets_by_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets | Lists all cloud buckets.
*CloudBucketsApi* | [**index_cloud_buckets_by_pool**](docs/CloudBucketsApi.md#index_cloud_buckets_by_pool) | **GET** /pools/{pool_id}/cloud_buckets | Lists all cloud buckets from pool.
*CloudBucketsApi* | [**mount_status_cloud_bucket**](docs/CloudBucketsApi.md#mount_status_cloud_bucket) | **GET** /cloud_buckets/{cloud_bucket_id}/mount | Get mount status of Cloud bucket.
*CloudBucketsApi* | [**mount_status_cloud_bucket_by_cloud_connector**](docs/CloudBucketsApi.md#mount_status_cloud_bucket_by_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets/{cloud_bucket_id}/mount | Get mount status of Cloud bucket.
*CloudBucketsApi* | [**mount_status_cloud_bucket_by_pool**](docs/CloudBucketsApi.md#mount_status_cloud_bucket_by_pool) | **GET** /pools/{pool_id}/cloud_buckets/{cloud_bucket_id}/mount | Get mount status of Cloud bucket.
*CloudBucketsApi* | [**show_cloud_bucket**](docs/CloudBucketsApi.md#show_cloud_bucket) | **GET** /cloud_buckets/{cloud_bucket_id} | Displays a specific cloud bucket.
*CloudBucketsApi* | [**show_cloud_bucket_by_cloud_connector**](docs/CloudBucketsApi.md#show_cloud_bucket_by_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets/{cloud_bucket_id} | Displays a specific cloud bucket.
*CloudBucketsApi* | [**show_cloud_bucket_by_pool**](docs/CloudBucketsApi.md#show_cloud_bucket_by_pool) | **GET** /pools/{pool_id}/cloud_buckets/{cloud_bucket_id} | Displays a specific cloud bucket.
*CloudBucketsApi* | [**sync_cloud_buckets**](docs/CloudBucketsApi.md#sync_cloud_buckets) | **PUT** /cloud_connectors/{cloud_connector_id}/cloud_buckets/-/sync | Synchronize internal cloud buckets with their remote equivalent.
*CloudBucketsApi* | [**sync_result_cloud_buckets**](docs/CloudBucketsApi.md#sync_result_cloud_buckets) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets/-/sync | Check result of cloud connector sync job.
*CloudBucketsApi* | [**update_cloud_bucket**](docs/CloudBucketsApi.md#update_cloud_bucket) | **PUT** /cloud_buckets/{cloud_bucket_id} | Updates a specific cloud bucket.
*CloudBucketsApi* | [**update_cloud_bucket_by_cloud_connector**](docs/CloudBucketsApi.md#update_cloud_bucket_by_cloud_connector) | **PUT** /cloud_connectors/{cloud_connector_id}/cloud_buckets/{cloud_bucket_id} | Updates a specific cloud bucket.
*CloudBucketsApi* | [**update_cloud_bucket_by_pool**](docs/CloudBucketsApi.md#update_cloud_bucket_by_pool) | **PUT** /pools/{pool_id}/cloud_buckets/{cloud_bucket_id} | Updates a specific cloud bucket.
*CloudConnectorsApi* | [**create_cloud_connector**](docs/CloudConnectorsApi.md#create_cloud_connector) | **POST** /cloud_connectors | Creates a new cloud connector.
*CloudConnectorsApi* | [**destroy_cloud_connector**](docs/CloudConnectorsApi.md#destroy_cloud_connector) | **DELETE** /cloud_connectors/{cloud_connector_id} | Destroys a specific cloud connector.
*CloudConnectorsApi* | [**index_cloud_connectors**](docs/CloudConnectorsApi.md#index_cloud_connectors) | **GET** /cloud_connectors | Lists all cloud connectors.
*CloudConnectorsApi* | [**show_cloud_connector**](docs/CloudConnectorsApi.md#show_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id} | Displays a specific cloud connector.
*CloudConnectorsApi* | [**test_cloud_connector**](docs/CloudConnectorsApi.md#test_cloud_connector) | **PUT** /cloud_connectors/-/test | Test an unsaved cloud connector.
*CloudConnectorsApi* | [**test_result_cloud_connector**](docs/CloudConnectorsApi.md#test_result_cloud_connector) | **GET** /cloud_connectors/-/test | Check result of cloud connector test job.
*CloudConnectorsApi* | [**update_cloud_connector**](docs/CloudConnectorsApi.md#update_cloud_connector) | **PUT** /cloud_connectors/{cloud_connector_id} | Updates a specific cloud connector.
*ContainersApi* | [**create_container**](docs/ContainersApi.md#create_container) | **POST** /containers | Creates a new container.
*ContainersApi* | [**create_container_privilege**](docs/ContainersApi.md#create_container_privilege) | **POST** /containers/{container_id}/container_privileges | Creates a new privilege on the container.
*ContainersApi* | [**destroy_container**](docs/ContainersApi.md#destroy_container) | **DELETE** /containers/{container_id} | Destroys a specific container.
*ContainersApi* | [**destroy_container_privilege**](docs/ContainersApi.md#destroy_container_privilege) | **DELETE** /containers/{container_id}/container_privileges/{container_privilege_id} | Destroys a specific privilege.
*ContainersApi* | [**index_container_privileges**](docs/ContainersApi.md#index_container_privileges) | **GET** /containers/{container_id}/container_privileges | Lists all privilege on the container.
*ContainersApi* | [**index_containers**](docs/ContainersApi.md#index_containers) | **GET** /containers | Lists all containers.
*ContainersApi* | [**show_container**](docs/ContainersApi.md#show_container) | **GET** /containers/{container_id} | Displays a specific container.
*ContainersApi* | [**show_container_privilege**](docs/ContainersApi.md#show_container_privilege) | **GET** /containers/{container_id}/container_privileges/{container_privilege_id} | Displays a specific privilege.
*ContainersApi* | [**update_container**](docs/ContainersApi.md#update_container) | **PUT** /containers/{container_id} | Updates a specific container.
*ContainersApi* | [**update_container_privilege**](docs/ContainersApi.md#update_container_privilege) | **PUT** /containers/{container_id}/container_privileges/{container_privilege_id} | Updates a specific privilege.
*FilesApi* | [**files_children**](docs/FilesApi.md#files_children) | **GET** /files/{file_parent_id}/children | Lists files under a specific folder.
*FilesApi* | [**files_children_by_container**](docs/FilesApi.md#files_children_by_container) | **GET** /containers/{container_id}/files/{file_parent_id}/children | Lists files under a specific folder.
*FilesApi* | [**files_children_by_pool**](docs/FilesApi.md#files_children_by_pool) | **GET** /pools/{pool_id}/files/{file_parent_id}/children | Lists files under a specific folder.
*FilesApi* | [**files_children_by_task**](docs/FilesApi.md#files_children_by_task) | **GET** /tasks/{task_id}/files/{file_parent_id}/children | Lists files under a specific folder.
*FilesApi* | [**files_children_by_task_execution**](docs/FilesApi.md#files_children_by_task_execution) | **GET** /task_executions/{task_execution_id}/files/{file_parent_id}/children | Lists files under a specific folder.
*FilesApi* | [**files_children_by_task_execution_by_task**](docs/FilesApi.md#files_children_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files/{file_parent_id}/children | Lists files under a specific folder.
*FilesApi* | [**import_files_children_by_pool**](docs/FilesApi.md#import_files_children_by_pool) | **GET** /pools/{pool_id}/import_files/{file_parent_id}/children | Lists files under a specific folder on tape of pools, specific for Data Exchange.
*FilesApi* | [**index_files**](docs/FilesApi.md#index_files) | **GET** /files | Lists files on root.
*FilesApi* | [**index_files_by_container**](docs/FilesApi.md#index_files_by_container) | **GET** /containers/{container_id}/files | Lists files on root.
*FilesApi* | [**index_files_by_pool**](docs/FilesApi.md#index_files_by_pool) | **GET** /pools/{pool_id}/files | Lists files on root.
*FilesApi* | [**index_files_by_task**](docs/FilesApi.md#index_files_by_task) | **GET** /tasks/{task_id}/files | Lists files on root.
*FilesApi* | [**index_files_by_task_execution**](docs/FilesApi.md#index_files_by_task_execution) | **GET** /task_executions/{task_execution_id}/files | Lists files on root.
*FilesApi* | [**index_files_by_task_execution_by_task**](docs/FilesApi.md#index_files_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files | Lists files on root.
*FilesApi* | [**index_import_files_by_pool**](docs/FilesApi.md#index_import_files_by_pool) | **GET** /pools/{pool_id}/import_files | Lists files on root of tape of pools, specific for Data Exchange.
*FilesApi* | [**index_on_tapes_files_by_pool**](docs/FilesApi.md#index_on_tapes_files_by_pool) | **GET** /pools/{pool_id}/on_tapes_files | Lists files on root of tape of pools, specific for Active and Offline.
*FilesApi* | [**index_tapes_by_file_by_pool**](docs/FilesApi.md#index_tapes_by_file_by_pool) | **GET** /pools/{pool_id}/files/{file_id}/tapes | Displays tapes containing specific file, related to the specific pool.
*FilesApi* | [**index_tapes_by_file_by_task**](docs/FilesApi.md#index_tapes_by_file_by_task) | **GET** /tasks/{task_id}/files/{file_id}/tapes | Displays tapes containing specific file, related to the specific task.
*FilesApi* | [**index_tapes_by_file_by_task_execution**](docs/FilesApi.md#index_tapes_by_file_by_task_execution) | **GET** /task_executions/{task_execution_id}/files/{file_id}/tapes | Displays tapes containing specific file, related to the specific task.
*FilesApi* | [**index_tapes_by_file_by_task_execution_by_task**](docs/FilesApi.md#index_tapes_by_file_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files/{file_id}/tapes | Displays tapes containing specific file, related to the specific task.
*FilesApi* | [**on_tapes_files_children_by_pool**](docs/FilesApi.md#on_tapes_files_children_by_pool) | **GET** /pools/{pool_id}/on_tapes_files/{file_parent_id}/children | Lists files under a specific folder on tape of pools, specific for Active and Offline.
*FilesApi* | [**show_file**](docs/FilesApi.md#show_file) | **GET** /files/{file_id} | Displays a specific file.
*FilesApi* | [**show_file_by_container**](docs/FilesApi.md#show_file_by_container) | **GET** /containers/{container_id}/files/{file_id} | Displays a specific file.
*FilesApi* | [**show_file_by_pool**](docs/FilesApi.md#show_file_by_pool) | **GET** /pools/{pool_id}/files/{file_id} | Displays a specific file.
*FilesApi* | [**show_file_by_task**](docs/FilesApi.md#show_file_by_task) | **GET** /tasks/{task_id}/files/{file_id} | Displays a specific file.
*FilesApi* | [**show_file_by_task_execution**](docs/FilesApi.md#show_file_by_task_execution) | **GET** /task_executions/{task_execution_id}/files/{file_id} | Displays a specific file.
*FilesApi* | [**show_file_by_task_execution_by_task**](docs/FilesApi.md#show_file_by_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id}/files/{file_id} | Displays a specific file.
*FilesApi* | [**show_import_file_by_pool**](docs/FilesApi.md#show_import_file_by_pool) | **GET** /pools/{pool_id}/import_files/{file_id} | Displays a specific file on tape of pools, specific for Data Exchange.
*FilesApi* | [**show_on_tape_file_by_pool**](docs/FilesApi.md#show_on_tape_file_by_pool) | **GET** /pools/{pool_id}/on_tapes_files/{file_id} | Displays a specific file on tape of pools, specific for Active and Offline.
*MountsApi* | [**index_mounts**](docs/MountsApi.md#index_mounts) | **GET** /mounts | List all mounted storages.
*NasApi* | [**create_nas**](docs/NasApi.md#create_nas) | **POST** /nas | Creates a new NAS.
*NasApi* | [**destroy_nas**](docs/NasApi.md#destroy_nas) | **DELETE** /nas/{nas_id} | Destroys a specific NAS.
*NasApi* | [**index_nas**](docs/NasApi.md#index_nas) | **GET** /nas | Lists all NAS.
*NasApi* | [**show_nas**](docs/NasApi.md#show_nas) | **GET** /nas/{nas_id} | Displays a specific NAS.
*NasApi* | [**update_nas**](docs/NasApi.md#update_nas) | **PUT** /nas/{nas_id} | Updates a specific NAS.
*NasSharesApi* | [**create_nas_share_by_nas**](docs/NasSharesApi.md#create_nas_share_by_nas) | **POST** /nas/{nas_id}/nas_shares | Creates a new NAS share.
*NasSharesApi* | [**destroy_nas_share**](docs/NasSharesApi.md#destroy_nas_share) | **DELETE** /nas_shares/{nas_share_id} | Destroys a specific NAS share.
*NasSharesApi* | [**destroy_nas_share_by_nas**](docs/NasSharesApi.md#destroy_nas_share_by_nas) | **DELETE** /nas/{nas_id}/nas_shares/{nas_share_id} | Destroys a specific NAS share.
*NasSharesApi* | [**destroy_nas_share_by_pool**](docs/NasSharesApi.md#destroy_nas_share_by_pool) | **DELETE** /pools/{pool_id}/nas_shares/{nas_share_id} | Destroys a specific NAS share.
*NasSharesApi* | [**index_nas_shares**](docs/NasSharesApi.md#index_nas_shares) | **GET** /nas_shares | Lists all NAS shares.
*NasSharesApi* | [**index_nas_shares_by_nas**](docs/NasSharesApi.md#index_nas_shares_by_nas) | **GET** /nas/{nas_id}/nas_shares | Lists all NAS shares.
*NasSharesApi* | [**index_nas_shares_by_pool**](docs/NasSharesApi.md#index_nas_shares_by_pool) | **GET** /pools/{pool_id}/nas_shares | Lists all NAS shares from pool.
*NasSharesApi* | [**mount_status_nas_share**](docs/NasSharesApi.md#mount_status_nas_share) | **GET** /nas_shares/{nas_share_id}/mount | Get mount status of NAS Share.
*NasSharesApi* | [**mount_status_nas_share_by_nas**](docs/NasSharesApi.md#mount_status_nas_share_by_nas) | **GET** /nas/{nas_id}/nas_shares/{nas_share_id}/mount | Get mount status of NAS Share.
*NasSharesApi* | [**mount_status_nas_share_by_pool**](docs/NasSharesApi.md#mount_status_nas_share_by_pool) | **GET** /pools/{pool_id}/nas_shares/{nas_share_id}/mount | Get mount status of NAS Share.
*NasSharesApi* | [**show_nas_share**](docs/NasSharesApi.md#show_nas_share) | **GET** /nas_shares/{nas_share_id} | Displays a specific NAS share.
*NasSharesApi* | [**show_nas_share_by_nas**](docs/NasSharesApi.md#show_nas_share_by_nas) | **GET** /nas/{nas_id}/nas_shares/{nas_share_id} | Displays a specific NAS share.
*NasSharesApi* | [**show_nas_share_by_pool**](docs/NasSharesApi.md#show_nas_share_by_pool) | **GET** /pools/{pool_id}/nas_shares/{nas_share_id} | Displays a specific NAS share.
*NasSharesApi* | [**test_nas_share**](docs/NasSharesApi.md#test_nas_share) | **PUT** /nas/{nas_id}/nas_shares/-/test | Test an unsaved NAS Share.
*NasSharesApi* | [**test_result_nas_share**](docs/NasSharesApi.md#test_result_nas_share) | **GET** /nas/{nas_id}/nas_shares/-/test | Check result of a NAS Share test job.
*NasSharesApi* | [**update_nas_share**](docs/NasSharesApi.md#update_nas_share) | **PUT** /nas_shares/{nas_share_id} | Updates a specific NAS share.
*NasSharesApi* | [**update_nas_share_by_nas**](docs/NasSharesApi.md#update_nas_share_by_nas) | **PUT** /nas/{nas_id}/nas_shares/{nas_share_id} | Updates a specific NAS share.
*NasSharesApi* | [**update_nas_share_by_pool**](docs/NasSharesApi.md#update_nas_share_by_pool) | **PUT** /pools/{pool_id}/nas_shares/{nas_share_id} | Updates a specific NAS share.
*PoolsApi* | [**create_pool**](docs/PoolsApi.md#create_pool) | **POST** /pools | Creates a new pool.
*PoolsApi* | [**create_primary_scan**](docs/PoolsApi.md#create_primary_scan) | **POST** /pools/{pool_id}/primary_scan | Set a new primary pool scan option.
*PoolsApi* | [**destroy_pool**](docs/PoolsApi.md#destroy_pool) | **DELETE** /pools/{pool_id} | Destroys a specific tape pool.
*PoolsApi* | [**destroy_primary_scan**](docs/PoolsApi.md#destroy_primary_scan) | **DELETE** /pools/{pool_id}/primary_scan | Disable the primary pool scan.
*PoolsApi* | [**index_pools**](docs/PoolsApi.md#index_pools) | **GET** /pools | Lists all pools.
*PoolsApi* | [**mount_pool**](docs/PoolsApi.md#mount_pool) | **PUT** /pools/{pool_id}/mount | Mount Pool.
*PoolsApi* | [**mount_status_pool**](docs/PoolsApi.md#mount_status_pool) | **GET** /pools/{pool_id}/mount | Get mount status of Pool.
*PoolsApi* | [**show_pool**](docs/PoolsApi.md#show_pool) | **GET** /pools/{pool_id} | Displays a specific pool.
*PoolsApi* | [**show_primary_scan**](docs/PoolsApi.md#show_primary_scan) | **GET** /pools/{pool_id}/primary_scan | Displays the primary pool scan status.
*PoolsApi* | [**sync_primary_pool**](docs/PoolsApi.md#sync_primary_pool) | **POST** /pools/{pool_id}/sync | Synchronize a primary after a scan (for internal use only).
*PoolsApi* | [**unmount_pool**](docs/PoolsApi.md#unmount_pool) | **DELETE** /pools/{pool_id}/mount | Unmount Pool.
*PoolsApi* | [**update_pool**](docs/PoolsApi.md#update_pool) | **PUT** /pools/{pool_id} | Updates a specific pool.
*PoolsApi* | [**update_primary_scan**](docs/PoolsApi.md#update_primary_scan) | **PUT** /pools/{pool_id}/primary_scan | Updates the existing primary pool scan option.
*SystemsApi* | [**result_download_traces**](docs/SystemsApi.md#result_download_traces) | **GET** /systems/download_traces | Check result of a download traces job.
*SystemsApi* | [**trigger_download_traces**](docs/SystemsApi.md#trigger_download_traces) | **PUT** /systems/download_traces | Trigger a download traces request.
*TapeDrivesApi* | [**create_tape_drive_by_tape_library**](docs/TapeDrivesApi.md#create_tape_drive_by_tape_library) | **POST** /tape_libraries/{tape_library_id}/tape_drives | Creates a new tape drive.
*TapeDrivesApi* | [**destroy_tape_drive**](docs/TapeDrivesApi.md#destroy_tape_drive) | **DELETE** /tape_drives/{tape_drive_id} | Destroys a specific tape drive.
*TapeDrivesApi* | [**destroy_tape_drive_by_tape_library**](docs/TapeDrivesApi.md#destroy_tape_drive_by_tape_library) | **DELETE** /tape_libraries/{tape_library_id}/tape_drives/{tape_drive_id} | Destroys a specific tape drive.
*TapeDrivesApi* | [**index_tape_drive_devices**](docs/TapeDrivesApi.md#index_tape_drive_devices) | **GET** /tape_libraries/{tape_library_id}/tape_drives/-/devices | Lists tape drives devices.
*TapeDrivesApi* | [**index_tape_drives**](docs/TapeDrivesApi.md#index_tape_drives) | **GET** /tape_drives | Lists all tape drives.
*TapeDrivesApi* | [**index_tape_drives_by_tape_library**](docs/TapeDrivesApi.md#index_tape_drives_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tape_drives | Lists all tape drives.
*TapeDrivesApi* | [**show_tape_drive**](docs/TapeDrivesApi.md#show_tape_drive) | **GET** /tape_drives/{tape_drive_id} | Displays a specific tape drive.
*TapeDrivesApi* | [**show_tape_drive_by_tape_library**](docs/TapeDrivesApi.md#show_tape_drive_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tape_drives/{tape_drive_id} | Displays a specific tape drive.
*TapeDrivesApi* | [**update_tape_drive**](docs/TapeDrivesApi.md#update_tape_drive) | **PUT** /tape_drives/{tape_drive_id} | Updates a specific tape drive.
*TapeDrivesApi* | [**update_tape_drive_by_tape_library**](docs/TapeDrivesApi.md#update_tape_drive_by_tape_library) | **PUT** /tape_libraries/{tape_library_id}/tape_drives/{tape_drive_id} | Updates a specific tape drive.
*TapeLibrariesApi* | [**create_tape_library**](docs/TapeLibrariesApi.md#create_tape_library) | **POST** /tape_libraries | Creates a new tape library.
*TapeLibrariesApi* | [**destroy_tape_library**](docs/TapeLibrariesApi.md#destroy_tape_library) | **DELETE** /tape_libraries/{tape_library_id} | Destroys a specific tape library.
*TapeLibrariesApi* | [**index_tape_libraries**](docs/TapeLibrariesApi.md#index_tape_libraries) | **GET** /tape_libraries | Lists all tape libraries.
*TapeLibrariesApi* | [**index_tape_library_devices**](docs/TapeLibrariesApi.md#index_tape_library_devices) | **GET** /tape_libraries/-/devices | Lists tape libraries devices.
*TapeLibrariesApi* | [**show_tape_library**](docs/TapeLibrariesApi.md#show_tape_library) | **GET** /tape_libraries/{tape_library_id} | Displays a specific tape library.
*TapeLibrariesApi* | [**update_tape_library**](docs/TapeLibrariesApi.md#update_tape_library) | **PUT** /tape_libraries/{tape_library_id} | Updates a specific tape library.
*TapesApi* | [**index_tape_stats**](docs/TapesApi.md#index_tape_stats) | **GET** /tape_stats | List all tape statistics.
*TapesApi* | [**index_tapes**](docs/TapesApi.md#index_tapes) | **GET** /tapes | Lists all tapes.
*TapesApi* | [**index_tapes_by_pool**](docs/TapesApi.md#index_tapes_by_pool) | **GET** /pools/{pool_id}/tapes | Lists all tapes.
*TapesApi* | [**index_tapes_by_tape_library**](docs/TapesApi.md#index_tapes_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tapes | Lists all tapes.
*TapesApi* | [**mount_status_tape**](docs/TapesApi.md#mount_status_tape) | **GET** /tapes/{tape_id}/mount | Get mount status of Tape.
*TapesApi* | [**mount_status_tape_by_pool**](docs/TapesApi.md#mount_status_tape_by_pool) | **GET** /pools/{pool_id}/tapes/{tape_id}/mount | Get mount status of Tape.
*TapesApi* | [**mount_status_tape_by_tape_library**](docs/TapesApi.md#mount_status_tape_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tapes/{tape_id}/mount | Get mount status of Tape.
*TapesApi* | [**show_tape**](docs/TapesApi.md#show_tape) | **GET** /tapes/{tape_id} | Displays a specific tape.
*TapesApi* | [**show_tape_by_pool**](docs/TapesApi.md#show_tape_by_pool) | **GET** /pools/{pool_id}/tapes/{tape_id} | Displays a specific tape.
*TapesApi* | [**show_tape_by_tape_library**](docs/TapesApi.md#show_tape_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tapes/{tape_id} | Displays a specific tape.
*TapesApi* | [**show_tape_stat**](docs/TapesApi.md#show_tape_stat) | **GET** /tapes/{tape_id}/tape_stat | Display statistic for a specific tape.
*TapesApi* | [**show_tape_stat_by_pool**](docs/TapesApi.md#show_tape_stat_by_pool) | **GET** /pools/{pool_id}/tapes/{tape_id}/tape_stat | Display statistic for a specific tape.
*TapesApi* | [**show_tape_stat_by_tape_library**](docs/TapesApi.md#show_tape_stat_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tapes/{tape_id}/tape_stat | Display statistic for a specific tape.
*TaskCallbacksApi* | [**create_task_callback**](docs/TaskCallbacksApi.md#create_task_callback) | **POST** /tasks/{task_id}/task_callbacks | Creates a new task callback.
*TaskCallbacksApi* | [**destroy_task_callback**](docs/TaskCallbacksApi.md#destroy_task_callback) | **DELETE** /tasks/{task_id}/task_callbacks/{task_callback_id} | Destroys a specific task callback.
*TaskCallbacksApi* | [**index_task_callbacks**](docs/TaskCallbacksApi.md#index_task_callbacks) | **GET** /tasks/{task_id}/task_callbacks | Lists all task callbacks.
*TaskCallbacksApi* | [**show_task_callback**](docs/TaskCallbacksApi.md#show_task_callback) | **GET** /tasks/{task_id}/task_callbacks/{task_callback_id} | Displays a specific task callback.
*TaskCallbacksApi* | [**update_task_callback**](docs/TaskCallbacksApi.md#update_task_callback) | **PUT** /tasks/{task_id}/task_callbacks/{task_callback_id} | Updates a specific task callback.
*TaskDestinationsApi* | [**create_task_destination**](docs/TaskDestinationsApi.md#create_task_destination) | **POST** /tasks/{task_id}/task_destinations | Creates a new task destination.
*TaskDestinationsApi* | [**destroy_task_destination**](docs/TaskDestinationsApi.md#destroy_task_destination) | **DELETE** /tasks/{task_id}/task_destinations/{task_destination_id} | Destroys a specific task destination.
*TaskDestinationsApi* | [**index_task_destinations**](docs/TaskDestinationsApi.md#index_task_destinations) | **GET** /tasks/{task_id}/task_destinations | Lists all task destinations.
*TaskDestinationsApi* | [**show_task_destination**](docs/TaskDestinationsApi.md#show_task_destination) | **GET** /tasks/{task_id}/task_destinations/{task_destination_id} | Displays a specific task destination.
*TaskDestinationsApi* | [**update_task_destination**](docs/TaskDestinationsApi.md#update_task_destination) | **PUT** /tasks/{task_id}/task_destinations/{task_destination_id} | Updates a specific task destination.
*TaskExecutionsApi* | [**index_task_executions**](docs/TaskExecutionsApi.md#index_task_executions) | **GET** /task_executions | Lists all task executions.
*TaskExecutionsApi* | [**index_task_executions_by_task**](docs/TaskExecutionsApi.md#index_task_executions_by_task) | **GET** /tasks/{task_id}/task_executions | Lists all task executions.
*TaskExecutionsApi* | [**show_task_execution**](docs/TaskExecutionsApi.md#show_task_execution) | **GET** /task_executions/{task_execution_id} | Displays a specific task execution.
*TaskExecutionsApi* | [**show_task_execution_by_task**](docs/TaskExecutionsApi.md#show_task_execution_by_task) | **GET** /tasks/{task_id}/task_executions/{task_execution_id} | Displays a specific task execution.
*TaskMetadataApi* | [**create_task_metadatum**](docs/TaskMetadataApi.md#create_task_metadatum) | **POST** /tasks/{task_id}/task_metadata | Creates a new task metadatum.
*TaskMetadataApi* | [**destroy_task_metadatum**](docs/TaskMetadataApi.md#destroy_task_metadatum) | **DELETE** /tasks/{task_id}/task_metadata/{task_metadatum_id} | Destroys a specific task metadatum.
*TaskMetadataApi* | [**index_task_metadata**](docs/TaskMetadataApi.md#index_task_metadata) | **GET** /tasks/{task_id}/task_metadata | Lists all task metadata.
*TaskMetadataApi* | [**show_task_metadatum**](docs/TaskMetadataApi.md#show_task_metadatum) | **GET** /tasks/{task_id}/task_metadata/{task_metadatum_id} | Displays a specific task metadatum.
*TaskMetadataApi* | [**update_task_metadatum**](docs/TaskMetadataApi.md#update_task_metadatum) | **PUT** /tasks/{task_id}/task_metadata/{task_metadatum_id} | Updates a specific task metadatum.
*TaskOptionsApi* | [**create_task_option**](docs/TaskOptionsApi.md#create_task_option) | **POST** /tasks/{task_id}/task_options | Creates a new task option.
*TaskOptionsApi* | [**destroy_task_option**](docs/TaskOptionsApi.md#destroy_task_option) | **DELETE** /tasks/{task_id}/task_options/{task_option_id} | Destroys a specific task option.
*TaskOptionsApi* | [**index_task_options**](docs/TaskOptionsApi.md#index_task_options) | **GET** /tasks/{task_id}/task_options | Lists all task options.
*TaskOptionsApi* | [**show_task_option**](docs/TaskOptionsApi.md#show_task_option) | **GET** /tasks/{task_id}/task_options/{task_option_id} | Displays a specific task option.
*TaskOptionsApi* | [**update_task_option**](docs/TaskOptionsApi.md#update_task_option) | **PUT** /tasks/{task_id}/task_options/{task_option_id} | Updates a specific task option.
*TaskSchedulesApi* | [**create_task_schedule**](docs/TaskSchedulesApi.md#create_task_schedule) | **POST** /tasks/{task_id}/task_schedule | Creates a new task schedule. Only one should be created.
*TaskSchedulesApi* | [**destroy_task_schedule**](docs/TaskSchedulesApi.md#destroy_task_schedule) | **DELETE** /tasks/{task_id}/task_schedule | Destroys the task schedule.
*TaskSchedulesApi* | [**index_task_schedules**](docs/TaskSchedulesApi.md#index_task_schedules) | **GET** /task_schedules | Lists all task schedules.
*TaskSchedulesApi* | [**show_task_schedule**](docs/TaskSchedulesApi.md#show_task_schedule) | **GET** /tasks/{task_id}/task_schedule | Displays the task schedule.
*TaskSchedulesApi* | [**update_task_schedule**](docs/TaskSchedulesApi.md#update_task_schedule) | **PUT** /tasks/{task_id}/task_schedule | Updates the existing task schedule.
*TaskSourcesApi* | [**create_task_source**](docs/TaskSourcesApi.md#create_task_source) | **POST** /tasks/{task_id}/task_sources | Creates a new task source.
*TaskSourcesApi* | [**destroy_task_source**](docs/TaskSourcesApi.md#destroy_task_source) | **DELETE** /tasks/{task_id}/task_sources/{task_source_id} | Destroys a specific task source.
*TaskSourcesApi* | [**index_task_sources**](docs/TaskSourcesApi.md#index_task_sources) | **GET** /tasks/{task_id}/task_sources | Lists all task sources.
*TaskSourcesApi* | [**show_task_source**](docs/TaskSourcesApi.md#show_task_source) | **GET** /tasks/{task_id}/task_sources/{task_source_id} | Displays a specific task source.
*TaskSourcesApi* | [**update_task_source**](docs/TaskSourcesApi.md#update_task_source) | **PUT** /tasks/{task_id}/task_sources/{task_source_id} | Updates a specific task source.
*TasksApi* | [**create_task**](docs/TasksApi.md#create_task) | **POST** /tasks | Creates a new task.
*TasksApi* | [**destroy_task**](docs/TasksApi.md#destroy_task) | **DELETE** /tasks/{task_id} | Destroys a specific task.
*TasksApi* | [**index_tasks**](docs/TasksApi.md#index_tasks) | **GET** /tasks | Lists all tasks.
*TasksApi* | [**pause_task**](docs/TasksApi.md#pause_task) | **PUT** /tasks/{task_id}/action/pause | Pause a task.
*TasksApi* | [**pause_task_result**](docs/TasksApi.md#pause_task_result) | **GET** /tasks/{task_id}/action/pause | Check result of a task pause request.
*TasksApi* | [**resume_task**](docs/TasksApi.md#resume_task) | **PUT** /tasks/{task_id}/action/resume | Resume a task.
*TasksApi* | [**resume_task_result**](docs/TasksApi.md#resume_task_result) | **GET** /tasks/{task_id}/action/resume | Check result of a task resume request.
*TasksApi* | [**run_task**](docs/TasksApi.md#run_task) | **PUT** /tasks/{task_id}/action/run | Run a task.
*TasksApi* | [**run_task_result**](docs/TasksApi.md#run_task_result) | **GET** /tasks/{task_id}/action/run | Check result of a task run request.
*TasksApi* | [**show_task**](docs/TasksApi.md#show_task) | **GET** /tasks/{task_id} | Displays a specific task.
*TasksApi* | [**stop_task**](docs/TasksApi.md#stop_task) | **PUT** /tasks/{task_id}/action/stop | Stop a task.
*TasksApi* | [**stop_task_result**](docs/TasksApi.md#stop_task_result) | **GET** /tasks/{task_id}/action/stop | Check result of a task stop request.
*TasksApi* | [**update_task**](docs/TasksApi.md#update_task) | **PUT** /tasks/{task_id} | Updates a specific task.
*UsersApi* | [**create_api_key**](docs/UsersApi.md#create_api_key) | **POST** /users/me/api_keys | Creates a new API Key for current user.
*UsersApi* | [**destroy_api_key**](docs/UsersApi.md#destroy_api_key) | **DELETE** /users/me/api_keys/{api_key_id} | Destroys a specific API Key.
*UsersApi* | [**index_api_keys**](docs/UsersApi.md#index_api_keys) | **GET** /users/me/api_keys | Lists all API keys of current user.
*UsersApi* | [**show_api_key**](docs/UsersApi.md#show_api_key) | **GET** /users/me/api_keys/{api_key_id} | Displays a specific API Key with its scopes.
*UsersApi* | [**update_api_key**](docs/UsersApi.md#update_api_key) | **PUT** /users/me/api_keys/{api_key_id} | Updates a specific API Key.


## Documentation For Models

 - [ActiveJobStatus](docs/ActiveJobStatus.md)
 - [ApiKey](docs/ApiKey.md)
 - [ApiKeyCollection](docs/ApiKeyCollection.md)
 - [ApiKeyFull](docs/ApiKeyFull.md)
 - [ApiKeyFullAllOf](docs/ApiKeyFullAllOf.md)
 - [ApiKeyScope](docs/ApiKeyScope.md)
 - [AttributeError](docs/AttributeError.md)
 - [Blank](docs/Blank.md)
 - [CloudBucket](docs/CloudBucket.md)
 - [CloudBucketCollection](docs/CloudBucketCollection.md)
 - [CloudBucketSimpleCollection](docs/CloudBucketSimpleCollection.md)
 - [CloudConnector](docs/CloudConnector.md)
 - [CloudConnectorCollection](docs/CloudConnectorCollection.md)
 - [Container](docs/Container.md)
 - [ContainerCollection](docs/ContainerCollection.md)
 - [ContainerPrivilege](docs/ContainerPrivilege.md)
 - [ContainerPrivilegeCollection](docs/ContainerPrivilegeCollection.md)
 - [Error](docs/Error.md)
 - [Frozen](docs/Frozen.md)
 - [GreaterThan](docs/GreaterThan.md)
 - [GreaterThanAllOf](docs/GreaterThanAllOf.md)
 - [GreaterThanOrEqualTo](docs/GreaterThanOrEqualTo.md)
 - [ImportFile](docs/ImportFile.md)
 - [ImportFileCollection](docs/ImportFileCollection.md)
 - [ImportFileWithPath](docs/ImportFileWithPath.md)
 - [Invalid](docs/Invalid.md)
 - [LessThan](docs/LessThan.md)
 - [LessThanAllOf](docs/LessThanAllOf.md)
 - [LessThanOrEqualTo](docs/LessThanOrEqualTo.md)
 - [MountCollection](docs/MountCollection.md)
 - [MountInfo](docs/MountInfo.md)
 - [MountNotification](docs/MountNotification.md)
 - [MountStatus](docs/MountStatus.md)
 - [Nas](docs/Nas.md)
 - [NasCollection](docs/NasCollection.md)
 - [NasShare](docs/NasShare.md)
 - [NasShareCollection](docs/NasShareCollection.md)
 - [NodeumFile](docs/NodeumFile.md)
 - [NodeumFileCollection](docs/NodeumFileCollection.md)
 - [NodeumFileWithPath](docs/NodeumFileWithPath.md)
 - [NodeumFileWithPathAllOf](docs/NodeumFileWithPathAllOf.md)
 - [OccurrenceLessThan](docs/OccurrenceLessThan.md)
 - [OccurrenceLessThanAllOf](docs/OccurrenceLessThanAllOf.md)
 - [OccurrenceLessThanOrEqualTo](docs/OccurrenceLessThanOrEqualTo.md)
 - [OnTapesFile](docs/OnTapesFile.md)
 - [OnTapesFileCollection](docs/OnTapesFileCollection.md)
 - [Pool](docs/Pool.md)
 - [PoolCollection](docs/PoolCollection.md)
 - [PoolUp](docs/PoolUp.md)
 - [PoolUpAllOf](docs/PoolUpAllOf.md)
 - [PrimaryScan](docs/PrimaryScan.md)
 - [QuotaOnCache](docs/QuotaOnCache.md)
 - [Taken](docs/Taken.md)
 - [TakenAllOf](docs/TakenAllOf.md)
 - [Tape](docs/Tape.md)
 - [TapeCollection](docs/TapeCollection.md)
 - [TapeDrive](docs/TapeDrive.md)
 - [TapeDriveAllOf](docs/TapeDriveAllOf.md)
 - [TapeDriveCollection](docs/TapeDriveCollection.md)
 - [TapeDriveDevice](docs/TapeDriveDevice.md)
 - [TapeDriveDeviceCollection](docs/TapeDriveDeviceCollection.md)
 - [TapeLibrary](docs/TapeLibrary.md)
 - [TapeLibraryAllOf](docs/TapeLibraryAllOf.md)
 - [TapeLibraryCollection](docs/TapeLibraryCollection.md)
 - [TapeLibraryDevice](docs/TapeLibraryDevice.md)
 - [TapeLibraryDeviceCollection](docs/TapeLibraryDeviceCollection.md)
 - [TapeStat](docs/TapeStat.md)
 - [TapeStatCollection](docs/TapeStatCollection.md)
 - [Task](docs/Task.md)
 - [TaskCallback](docs/TaskCallback.md)
 - [TaskCallbackCollection](docs/TaskCallbackCollection.md)
 - [TaskCollection](docs/TaskCollection.md)
 - [TaskDestinationCollection](docs/TaskDestinationCollection.md)
 - [TaskDestinationDown](docs/TaskDestinationDown.md)
 - [TaskDestinationUp](docs/TaskDestinationUp.md)
 - [TaskExecution](docs/TaskExecution.md)
 - [TaskExecutionCollection](docs/TaskExecutionCollection.md)
 - [TaskMetadatum](docs/TaskMetadatum.md)
 - [TaskMetadatumCollection](docs/TaskMetadatumCollection.md)
 - [TaskOption](docs/TaskOption.md)
 - [TaskOptionCollection](docs/TaskOptionCollection.md)
 - [TaskSchedule](docs/TaskSchedule.md)
 - [TaskScheduleCollection](docs/TaskScheduleCollection.md)
 - [TaskSourceCollection](docs/TaskSourceCollection.md)
 - [TaskSourceDown](docs/TaskSourceDown.md)
 - [TaskSourceUp](docs/TaskSourceUp.md)
 - [TooLong](docs/TooLong.md)
 - [TooLongAllOf](docs/TooLongAllOf.md)
 - [TooShort](docs/TooShort.md)
 - [TooShortAllOf](docs/TooShortAllOf.md)


## Documentation For Authorization


## BasicAuth

- **Type**: HTTP basic authentication


## BearerAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




