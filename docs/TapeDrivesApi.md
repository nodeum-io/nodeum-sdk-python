# nodeum_sdk.TapeDrivesApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tape_drive_by_tape_library**](TapeDrivesApi.md#create_tape_drive_by_tape_library) | **POST** /tape_libraries/{tape_library_id}/tape_drives | Creates a new tape drive.
[**destroy_tape_drive**](TapeDrivesApi.md#destroy_tape_drive) | **DELETE** /tape_drives/{tape_drive_id} | Destroys a specific tape drive.
[**destroy_tape_drive_by_tape_library**](TapeDrivesApi.md#destroy_tape_drive_by_tape_library) | **DELETE** /tape_libraries/{tape_library_id}/tape_drives/{tape_drive_id} | Destroys a specific tape drive.
[**index_tape_drive_devices**](TapeDrivesApi.md#index_tape_drive_devices) | **GET** /tape_libraries/{tape_library_id}/tape_drives/-/devices | Lists tape drives devices.
[**index_tape_drives**](TapeDrivesApi.md#index_tape_drives) | **GET** /tape_drives | Lists all tape drives.
[**index_tape_drives_by_tape_library**](TapeDrivesApi.md#index_tape_drives_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tape_drives | Lists all tape drives.
[**show_tape_drive**](TapeDrivesApi.md#show_tape_drive) | **GET** /tape_drives/{tape_drive_id} | Displays a specific tape drive.
[**show_tape_drive_by_tape_library**](TapeDrivesApi.md#show_tape_drive_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tape_drives/{tape_drive_id} | Displays a specific tape drive.
[**update_tape_drive**](TapeDrivesApi.md#update_tape_drive) | **PUT** /tape_drives/{tape_drive_id} | Updates a specific tape drive.
[**update_tape_drive_by_tape_library**](TapeDrivesApi.md#update_tape_drive_by_tape_library) | **PUT** /tape_libraries/{tape_library_id}/tape_drives/{tape_drive_id} | Updates a specific tape drive.


# **create_tape_drive_by_tape_library**
> TapeDrive create_tape_drive_by_tape_library(tape_library_id, tape_drive_body)

Creates a new tape drive.

**API Key Scope**: tape_drives / create

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_drive_body = nodeum_sdk.TapeDrive() # TapeDrive | 

try:
    # Creates a new tape drive.
    api_response = api_instance.create_tape_drive_by_tape_library(tape_library_id, tape_drive_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->create_tape_drive_by_tape_library: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_drive_body = nodeum_sdk.TapeDrive() # TapeDrive | 

try:
    # Creates a new tape drive.
    api_response = api_instance.create_tape_drive_by_tape_library(tape_library_id, tape_drive_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->create_tape_drive_by_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **tape_drive_body** | [**TapeDrive**](TapeDrive.md)|  | 

### Return type

[**TapeDrive**](TapeDrive.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific tape drive. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_tape_drive**
> destroy_tape_drive(tape_drive_id)

Destroys a specific tape drive.

**API Key Scope**: tape_drives / destroy

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.

try:
    # Destroys a specific tape drive.
    api_instance.destroy_tape_drive(tape_drive_id)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->destroy_tape_drive: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.

try:
    # Destroys a specific tape drive.
    api_instance.destroy_tape_drive(tape_drive_id)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->destroy_tape_drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_drive_id** | **str**| Numeric ID, serial, or name of tape drive. | 

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
**204** | Tape drive destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_tape_drive_by_tape_library**
> destroy_tape_drive_by_tape_library(tape_library_id, tape_drive_id)

Destroys a specific tape drive.

**API Key Scope**: tape_drives / destroy

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.

try:
    # Destroys a specific tape drive.
    api_instance.destroy_tape_drive_by_tape_library(tape_library_id, tape_drive_id)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->destroy_tape_drive_by_tape_library: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.

try:
    # Destroys a specific tape drive.
    api_instance.destroy_tape_drive_by_tape_library(tape_library_id, tape_drive_id)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->destroy_tape_drive_by_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **tape_drive_id** | **str**| Numeric ID, serial, or name of tape drive. | 

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
**204** | Tape drive destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tape_drive_devices**
> TapeDriveDeviceCollection index_tape_drive_devices(tape_library_id, job_id=job_id)

Lists tape drives devices.

**API Key Scope**: tape_drives / devices

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
job_id = 'job_id_example' # str | ID of active job (optional)

try:
    # Lists tape drives devices.
    api_response = api_instance.index_tape_drive_devices(tape_library_id, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->index_tape_drive_devices: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
job_id = 'job_id_example' # str | ID of active job (optional)

try:
    # Lists tape drives devices.
    api_response = api_instance.index_tape_drive_devices(tape_library_id, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->index_tape_drive_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **job_id** | **str**| ID of active job | [optional] 

### Return type

[**TapeDriveDeviceCollection**](TapeDriveDeviceCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, queued, working, failed, 

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tape drives devices. |  -  |
**202** | An active job that may be queued, working, completed or failed. |  -  |
**500** | An active job that may be queued, working, completed or failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tape_drives**
> TapeDriveCollection index_tape_drives(limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, name=name, serial=serial, comment=comment, scsi_address=scsi_address, vendor=vendor, product=product, firmware=firmware, device=device, sgdevice=sgdevice, libso=libso, acs=acs, lsm=lsm, panel=panel, transport=transport, status=status, full=full, mount_count=mount_count, use_to=use_to, use_by=use_by, use_file_processed_size=use_file_processed_size, use_file_size_to_process=use_file_size_to_process, use_file_name_processed=use_file_name_processed, bandwidth=bandwidth)

Lists all tape drives.

**API Key Scope**: tape_drives / index

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
tape_library_id = 'tape_library_id_example' # str | Filter on tape library id (optional)
name = 'name_example' # str | Filter on name (optional)
serial = 'serial_example' # str | Filter on serial (optional)
comment = 'comment_example' # str | Filter on comment (optional)
scsi_address = 'scsi_address_example' # str | Filter on scsi address (optional)
vendor = 'vendor_example' # str | Filter on vendor (optional)
product = 'product_example' # str | Filter on product (optional)
firmware = 'firmware_example' # str | Filter on firmware (optional)
device = 'device_example' # str | Filter on device (optional)
sgdevice = 'sgdevice_example' # str | Filter on sgdevice (optional)
libso = 'libso_example' # str | Filter on libso (optional)
acs = 'acs_example' # str | Filter on acs (optional)
lsm = 'lsm_example' # str | Filter on lsm (optional)
panel = 'panel_example' # str | Filter on panel (optional)
transport = 'transport_example' # str | Filter on transport (optional)
status = 'status_example' # str | Filter on status (optional)
full = 'full_example' # str | Filter on full (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
use_to = 'use_to_example' # str | Filter on use to (optional)
use_by = 'use_by_example' # str | Filter on use by (optional)
use_file_processed_size = 'use_file_processed_size_example' # str | Filter on use file processed size (optional)
use_file_size_to_process = 'use_file_size_to_process_example' # str | Filter on use file size to process (optional)
use_file_name_processed = 'use_file_name_processed_example' # str | Filter on use file name processed (optional)
bandwidth = 'bandwidth_example' # str | Filter on bandwidth (optional)

try:
    # Lists all tape drives.
    api_response = api_instance.index_tape_drives(limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, name=name, serial=serial, comment=comment, scsi_address=scsi_address, vendor=vendor, product=product, firmware=firmware, device=device, sgdevice=sgdevice, libso=libso, acs=acs, lsm=lsm, panel=panel, transport=transport, status=status, full=full, mount_count=mount_count, use_to=use_to, use_by=use_by, use_file_processed_size=use_file_processed_size, use_file_size_to_process=use_file_size_to_process, use_file_name_processed=use_file_name_processed, bandwidth=bandwidth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->index_tape_drives: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
tape_library_id = 'tape_library_id_example' # str | Filter on tape library id (optional)
name = 'name_example' # str | Filter on name (optional)
serial = 'serial_example' # str | Filter on serial (optional)
comment = 'comment_example' # str | Filter on comment (optional)
scsi_address = 'scsi_address_example' # str | Filter on scsi address (optional)
vendor = 'vendor_example' # str | Filter on vendor (optional)
product = 'product_example' # str | Filter on product (optional)
firmware = 'firmware_example' # str | Filter on firmware (optional)
device = 'device_example' # str | Filter on device (optional)
sgdevice = 'sgdevice_example' # str | Filter on sgdevice (optional)
libso = 'libso_example' # str | Filter on libso (optional)
acs = 'acs_example' # str | Filter on acs (optional)
lsm = 'lsm_example' # str | Filter on lsm (optional)
panel = 'panel_example' # str | Filter on panel (optional)
transport = 'transport_example' # str | Filter on transport (optional)
status = 'status_example' # str | Filter on status (optional)
full = 'full_example' # str | Filter on full (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
use_to = 'use_to_example' # str | Filter on use to (optional)
use_by = 'use_by_example' # str | Filter on use by (optional)
use_file_processed_size = 'use_file_processed_size_example' # str | Filter on use file processed size (optional)
use_file_size_to_process = 'use_file_size_to_process_example' # str | Filter on use file size to process (optional)
use_file_name_processed = 'use_file_name_processed_example' # str | Filter on use file name processed (optional)
bandwidth = 'bandwidth_example' # str | Filter on bandwidth (optional)

try:
    # Lists all tape drives.
    api_response = api_instance.index_tape_drives(limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, name=name, serial=serial, comment=comment, scsi_address=scsi_address, vendor=vendor, product=product, firmware=firmware, device=device, sgdevice=sgdevice, libso=libso, acs=acs, lsm=lsm, panel=panel, transport=transport, status=status, full=full, mount_count=mount_count, use_to=use_to, use_by=use_by, use_file_processed_size=use_file_processed_size, use_file_size_to_process=use_file_size_to_process, use_file_name_processed=use_file_name_processed, bandwidth=bandwidth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->index_tape_drives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **tape_library_id** | **str**| Filter on tape library id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **serial** | **str**| Filter on serial | [optional] 
 **comment** | **str**| Filter on comment | [optional] 
 **scsi_address** | **str**| Filter on scsi address | [optional] 
 **vendor** | **str**| Filter on vendor | [optional] 
 **product** | **str**| Filter on product | [optional] 
 **firmware** | **str**| Filter on firmware | [optional] 
 **device** | **str**| Filter on device | [optional] 
 **sgdevice** | **str**| Filter on sgdevice | [optional] 
 **libso** | **str**| Filter on libso | [optional] 
 **acs** | **str**| Filter on acs | [optional] 
 **lsm** | **str**| Filter on lsm | [optional] 
 **panel** | **str**| Filter on panel | [optional] 
 **transport** | **str**| Filter on transport | [optional] 
 **status** | **str**| Filter on status | [optional] 
 **full** | **str**| Filter on full | [optional] 
 **mount_count** | **str**| Filter on mount count | [optional] 
 **use_to** | **str**| Filter on use to | [optional] 
 **use_by** | **str**| Filter on use by | [optional] 
 **use_file_processed_size** | **str**| Filter on use file processed size | [optional] 
 **use_file_size_to_process** | **str**| Filter on use file size to process | [optional] 
 **use_file_name_processed** | **str**| Filter on use file name processed | [optional] 
 **bandwidth** | **str**| Filter on bandwidth | [optional] 

### Return type

[**TapeDriveCollection**](TapeDriveCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tape drives. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tape_drives_by_tape_library**
> TapeDriveCollection index_tape_drives_by_tape_library(tape_library_id, limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, serial=serial, comment=comment, scsi_address=scsi_address, vendor=vendor, product=product, firmware=firmware, device=device, sgdevice=sgdevice, libso=libso, acs=acs, lsm=lsm, panel=panel, transport=transport, status=status, full=full, mount_count=mount_count, use_to=use_to, use_by=use_by, use_file_processed_size=use_file_processed_size, use_file_size_to_process=use_file_size_to_process, use_file_name_processed=use_file_name_processed, bandwidth=bandwidth)

Lists all tape drives.

**API Key Scope**: tape_drives / index

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
serial = 'serial_example' # str | Filter on serial (optional)
comment = 'comment_example' # str | Filter on comment (optional)
scsi_address = 'scsi_address_example' # str | Filter on scsi address (optional)
vendor = 'vendor_example' # str | Filter on vendor (optional)
product = 'product_example' # str | Filter on product (optional)
firmware = 'firmware_example' # str | Filter on firmware (optional)
device = 'device_example' # str | Filter on device (optional)
sgdevice = 'sgdevice_example' # str | Filter on sgdevice (optional)
libso = 'libso_example' # str | Filter on libso (optional)
acs = 'acs_example' # str | Filter on acs (optional)
lsm = 'lsm_example' # str | Filter on lsm (optional)
panel = 'panel_example' # str | Filter on panel (optional)
transport = 'transport_example' # str | Filter on transport (optional)
status = 'status_example' # str | Filter on status (optional)
full = 'full_example' # str | Filter on full (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
use_to = 'use_to_example' # str | Filter on use to (optional)
use_by = 'use_by_example' # str | Filter on use by (optional)
use_file_processed_size = 'use_file_processed_size_example' # str | Filter on use file processed size (optional)
use_file_size_to_process = 'use_file_size_to_process_example' # str | Filter on use file size to process (optional)
use_file_name_processed = 'use_file_name_processed_example' # str | Filter on use file name processed (optional)
bandwidth = 'bandwidth_example' # str | Filter on bandwidth (optional)

try:
    # Lists all tape drives.
    api_response = api_instance.index_tape_drives_by_tape_library(tape_library_id, limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, serial=serial, comment=comment, scsi_address=scsi_address, vendor=vendor, product=product, firmware=firmware, device=device, sgdevice=sgdevice, libso=libso, acs=acs, lsm=lsm, panel=panel, transport=transport, status=status, full=full, mount_count=mount_count, use_to=use_to, use_by=use_by, use_file_processed_size=use_file_processed_size, use_file_size_to_process=use_file_size_to_process, use_file_name_processed=use_file_name_processed, bandwidth=bandwidth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->index_tape_drives_by_tape_library: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
serial = 'serial_example' # str | Filter on serial (optional)
comment = 'comment_example' # str | Filter on comment (optional)
scsi_address = 'scsi_address_example' # str | Filter on scsi address (optional)
vendor = 'vendor_example' # str | Filter on vendor (optional)
product = 'product_example' # str | Filter on product (optional)
firmware = 'firmware_example' # str | Filter on firmware (optional)
device = 'device_example' # str | Filter on device (optional)
sgdevice = 'sgdevice_example' # str | Filter on sgdevice (optional)
libso = 'libso_example' # str | Filter on libso (optional)
acs = 'acs_example' # str | Filter on acs (optional)
lsm = 'lsm_example' # str | Filter on lsm (optional)
panel = 'panel_example' # str | Filter on panel (optional)
transport = 'transport_example' # str | Filter on transport (optional)
status = 'status_example' # str | Filter on status (optional)
full = 'full_example' # str | Filter on full (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
use_to = 'use_to_example' # str | Filter on use to (optional)
use_by = 'use_by_example' # str | Filter on use by (optional)
use_file_processed_size = 'use_file_processed_size_example' # str | Filter on use file processed size (optional)
use_file_size_to_process = 'use_file_size_to_process_example' # str | Filter on use file size to process (optional)
use_file_name_processed = 'use_file_name_processed_example' # str | Filter on use file name processed (optional)
bandwidth = 'bandwidth_example' # str | Filter on bandwidth (optional)

try:
    # Lists all tape drives.
    api_response = api_instance.index_tape_drives_by_tape_library(tape_library_id, limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, serial=serial, comment=comment, scsi_address=scsi_address, vendor=vendor, product=product, firmware=firmware, device=device, sgdevice=sgdevice, libso=libso, acs=acs, lsm=lsm, panel=panel, transport=transport, status=status, full=full, mount_count=mount_count, use_to=use_to, use_by=use_by, use_file_processed_size=use_file_processed_size, use_file_size_to_process=use_file_size_to_process, use_file_name_processed=use_file_name_processed, bandwidth=bandwidth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->index_tape_drives_by_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **serial** | **str**| Filter on serial | [optional] 
 **comment** | **str**| Filter on comment | [optional] 
 **scsi_address** | **str**| Filter on scsi address | [optional] 
 **vendor** | **str**| Filter on vendor | [optional] 
 **product** | **str**| Filter on product | [optional] 
 **firmware** | **str**| Filter on firmware | [optional] 
 **device** | **str**| Filter on device | [optional] 
 **sgdevice** | **str**| Filter on sgdevice | [optional] 
 **libso** | **str**| Filter on libso | [optional] 
 **acs** | **str**| Filter on acs | [optional] 
 **lsm** | **str**| Filter on lsm | [optional] 
 **panel** | **str**| Filter on panel | [optional] 
 **transport** | **str**| Filter on transport | [optional] 
 **status** | **str**| Filter on status | [optional] 
 **full** | **str**| Filter on full | [optional] 
 **mount_count** | **str**| Filter on mount count | [optional] 
 **use_to** | **str**| Filter on use to | [optional] 
 **use_by** | **str**| Filter on use by | [optional] 
 **use_file_processed_size** | **str**| Filter on use file processed size | [optional] 
 **use_file_size_to_process** | **str**| Filter on use file size to process | [optional] 
 **use_file_name_processed** | **str**| Filter on use file name processed | [optional] 
 **bandwidth** | **str**| Filter on bandwidth | [optional] 

### Return type

[**TapeDriveCollection**](TapeDriveCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tape drives. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape_drive**
> TapeDrive show_tape_drive(tape_drive_id)

Displays a specific tape drive.

**API Key Scope**: tape_drives / show

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.

try:
    # Displays a specific tape drive.
    api_response = api_instance.show_tape_drive(tape_drive_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->show_tape_drive: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.

try:
    # Displays a specific tape drive.
    api_response = api_instance.show_tape_drive(tape_drive_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->show_tape_drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_drive_id** | **str**| Numeric ID, serial, or name of tape drive. | 

### Return type

[**TapeDrive**](TapeDrive.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific tape drive. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape_drive_by_tape_library**
> TapeDrive show_tape_drive_by_tape_library(tape_library_id, tape_drive_id)

Displays a specific tape drive.

**API Key Scope**: tape_drives / show

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.

try:
    # Displays a specific tape drive.
    api_response = api_instance.show_tape_drive_by_tape_library(tape_library_id, tape_drive_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->show_tape_drive_by_tape_library: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.

try:
    # Displays a specific tape drive.
    api_response = api_instance.show_tape_drive_by_tape_library(tape_library_id, tape_drive_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->show_tape_drive_by_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **tape_drive_id** | **str**| Numeric ID, serial, or name of tape drive. | 

### Return type

[**TapeDrive**](TapeDrive.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific tape drive. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tape_drive**
> TapeDrive update_tape_drive(tape_drive_id, tape_drive_body)

Updates a specific tape drive.

**API Key Scope**: tape_drives / update

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.
tape_drive_body = nodeum_sdk.TapeDrive() # TapeDrive | 

try:
    # Updates a specific tape drive.
    api_response = api_instance.update_tape_drive(tape_drive_id, tape_drive_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->update_tape_drive: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.
tape_drive_body = nodeum_sdk.TapeDrive() # TapeDrive | 

try:
    # Updates a specific tape drive.
    api_response = api_instance.update_tape_drive(tape_drive_id, tape_drive_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->update_tape_drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_drive_id** | **str**| Numeric ID, serial, or name of tape drive. | 
 **tape_drive_body** | [**TapeDrive**](TapeDrive.md)|  | 

### Return type

[**TapeDrive**](TapeDrive.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific tape drive. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tape_drive_by_tape_library**
> TapeDrive update_tape_drive_by_tape_library(tape_library_id, tape_drive_id, tape_drive_body)

Updates a specific tape drive.

**API Key Scope**: tape_drives / update

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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.
tape_drive_body = nodeum_sdk.TapeDrive() # TapeDrive | 

try:
    # Updates a specific tape drive.
    api_response = api_instance.update_tape_drive_by_tape_library(tape_library_id, tape_drive_id, tape_drive_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->update_tape_drive_by_tape_library: %s\n" % e)
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
api_instance = nodeum_sdk.TapeDrivesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_drive_id = 'tape_drive_id_example' # str | Numeric ID, serial, or name of tape drive.
tape_drive_body = nodeum_sdk.TapeDrive() # TapeDrive | 

try:
    # Updates a specific tape drive.
    api_response = api_instance.update_tape_drive_by_tape_library(tape_library_id, tape_drive_id, tape_drive_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeDrivesApi->update_tape_drive_by_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **tape_drive_id** | **str**| Numeric ID, serial, or name of tape drive. | 
 **tape_drive_body** | [**TapeDrive**](TapeDrive.md)|  | 

### Return type

[**TapeDrive**](TapeDrive.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific tape drive. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

