# nodeum_sdk.TapeLibrariesApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tape_library**](TapeLibrariesApi.md#create_tape_library) | **POST** /tape_libraries | Creates a new tape library.
[**destroy_tape_library**](TapeLibrariesApi.md#destroy_tape_library) | **DELETE** /tape_libraries/{tape_library_id} | Destroys a specific tape library.
[**index_tape_libraries**](TapeLibrariesApi.md#index_tape_libraries) | **GET** /tape_libraries | Lists all tape libraries.
[**index_tape_library_devices**](TapeLibrariesApi.md#index_tape_library_devices) | **GET** /tape_libraries/-/devices | Lists tape libraries devices.
[**show_tape_library**](TapeLibrariesApi.md#show_tape_library) | **GET** /tape_libraries/{tape_library_id} | Displays a specific tape library.
[**update_tape_library**](TapeLibrariesApi.md#update_tape_library) | **PUT** /tape_libraries/{tape_library_id} | Updates a specific tape library.


# **create_tape_library**
> TapeLibrary create_tape_library(tape_library_body)

Creates a new tape library.

**API Key Scope**: tape_libraries / create

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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    tape_library_body = nodeum_sdk.TapeLibrary() # TapeLibrary | 

    try:
        # Creates a new tape library.
        api_response = api_instance.create_tape_library(tape_library_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->create_tape_library: %s\n" % e)
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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    tape_library_body = nodeum_sdk.TapeLibrary() # TapeLibrary | 

    try:
        # Creates a new tape library.
        api_response = api_instance.create_tape_library(tape_library_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->create_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_body** | [**TapeLibrary**](TapeLibrary.md)|  | 

### Return type

[**TapeLibrary**](TapeLibrary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A specific tape library. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_tape_library**
> destroy_tape_library(tape_library_id)

Destroys a specific tape library.

**API Key Scope**: tape_libraries / destroy

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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.

    try:
        # Destroys a specific tape library.
        api_instance.destroy_tape_library(tape_library_id)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->destroy_tape_library: %s\n" % e)
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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.

    try:
        # Destroys a specific tape library.
        api_instance.destroy_tape_library(tape_library_id)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->destroy_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 

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
**204** | Tape library destroyed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tape_libraries**
> TapeLibraryCollection index_tape_libraries(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, serial=serial, comment=comment, protocol=protocol, vendor=vendor, product=product, firmware=firmware, device=device, libso=libso, acs=acs, status=status, storage_slots=storage_slots, storage_slots_address=storage_slots_address, io_slots=io_slots, io_slots_address=io_slots_address, price=price)

Lists all tape libraries.

**API Key Scope**: tape_libraries / index

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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
serial = 'serial_example' # str | Filter on serial (optional)
comment = 'comment_example' # str | Filter on comment (optional)
protocol = 'protocol_example' # str | Filter on protocol (optional)
vendor = 'vendor_example' # str | Filter on vendor (optional)
product = 'product_example' # str | Filter on product (optional)
firmware = 'firmware_example' # str | Filter on firmware (optional)
device = 'device_example' # str | Filter on device (optional)
libso = 'libso_example' # str | Filter on libso (optional)
acs = 'acs_example' # str | Filter on acs (optional)
status = 'status_example' # str | Filter on status (optional)
storage_slots = 'storage_slots_example' # str | Filter on storage slots (optional)
storage_slots_address = 'storage_slots_address_example' # str | Filter on storage slots address (optional)
io_slots = 'io_slots_example' # str | Filter on io slots (optional)
io_slots_address = 'io_slots_address_example' # str | Filter on io slots address (optional)
price = 'price_example' # str | Filter on price (optional)

    try:
        # Lists all tape libraries.
        api_response = api_instance.index_tape_libraries(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, serial=serial, comment=comment, protocol=protocol, vendor=vendor, product=product, firmware=firmware, device=device, libso=libso, acs=acs, status=status, storage_slots=storage_slots, storage_slots_address=storage_slots_address, io_slots=io_slots, io_slots_address=io_slots_address, price=price)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->index_tape_libraries: %s\n" % e)
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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
serial = 'serial_example' # str | Filter on serial (optional)
comment = 'comment_example' # str | Filter on comment (optional)
protocol = 'protocol_example' # str | Filter on protocol (optional)
vendor = 'vendor_example' # str | Filter on vendor (optional)
product = 'product_example' # str | Filter on product (optional)
firmware = 'firmware_example' # str | Filter on firmware (optional)
device = 'device_example' # str | Filter on device (optional)
libso = 'libso_example' # str | Filter on libso (optional)
acs = 'acs_example' # str | Filter on acs (optional)
status = 'status_example' # str | Filter on status (optional)
storage_slots = 'storage_slots_example' # str | Filter on storage slots (optional)
storage_slots_address = 'storage_slots_address_example' # str | Filter on storage slots address (optional)
io_slots = 'io_slots_example' # str | Filter on io slots (optional)
io_slots_address = 'io_slots_address_example' # str | Filter on io slots address (optional)
price = 'price_example' # str | Filter on price (optional)

    try:
        # Lists all tape libraries.
        api_response = api_instance.index_tape_libraries(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, serial=serial, comment=comment, protocol=protocol, vendor=vendor, product=product, firmware=firmware, device=device, libso=libso, acs=acs, status=status, storage_slots=storage_slots, storage_slots_address=storage_slots_address, io_slots=io_slots, io_slots_address=io_slots_address, price=price)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->index_tape_libraries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **serial** | **str**| Filter on serial | [optional] 
 **comment** | **str**| Filter on comment | [optional] 
 **protocol** | **str**| Filter on protocol | [optional] 
 **vendor** | **str**| Filter on vendor | [optional] 
 **product** | **str**| Filter on product | [optional] 
 **firmware** | **str**| Filter on firmware | [optional] 
 **device** | **str**| Filter on device | [optional] 
 **libso** | **str**| Filter on libso | [optional] 
 **acs** | **str**| Filter on acs | [optional] 
 **status** | **str**| Filter on status | [optional] 
 **storage_slots** | **str**| Filter on storage slots | [optional] 
 **storage_slots_address** | **str**| Filter on storage slots address | [optional] 
 **io_slots** | **str**| Filter on io slots | [optional] 
 **io_slots_address** | **str**| Filter on io slots address | [optional] 
 **price** | **str**| Filter on price | [optional] 

### Return type

[**TapeLibraryCollection**](TapeLibraryCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tape libraries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tape_library_devices**
> TapeLibraryDeviceCollection index_tape_library_devices(job_id)

Lists tape libraries devices.

**API Key Scope**: tape_libraries / devices

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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    job_id = 'job_id_example' # str | ID of active job

    try:
        # Lists tape libraries devices.
        api_response = api_instance.index_tape_library_devices(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->index_tape_library_devices: %s\n" % e)
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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    job_id = 'job_id_example' # str | ID of active job

    try:
        # Lists tape libraries devices.
        api_response = api_instance.index_tape_library_devices(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->index_tape_library_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| ID of active job | 

### Return type

[**TapeLibraryDeviceCollection**](TapeLibraryDeviceCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, queued, working, failed, 

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of tape libraries devices. |  -  |
**202** | An active job that may be queued, working, completed or failed. |  -  |
**500** | An active job that may be queued, working, completed or failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape_library**
> TapeLibrary show_tape_library(tape_library_id)

Displays a specific tape library.

**API Key Scope**: tape_libraries / show

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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.

    try:
        # Displays a specific tape library.
        api_response = api_instance.show_tape_library(tape_library_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->show_tape_library: %s\n" % e)
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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.

    try:
        # Displays a specific tape library.
        api_response = api_instance.show_tape_library(tape_library_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->show_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 

### Return type

[**TapeLibrary**](TapeLibrary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific tape library. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tape_library**
> TapeLibrary update_tape_library(tape_library_id, tape_library_body)

Updates a specific tape library.

**API Key Scope**: tape_libraries / update

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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_library_body = nodeum_sdk.TapeLibrary() # TapeLibrary | 

    try:
        # Updates a specific tape library.
        api_response = api_instance.update_tape_library(tape_library_id, tape_library_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->update_tape_library: %s\n" % e)
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
    api_instance = nodeum_sdk.TapeLibrariesApi(api_client)
    tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_library_body = nodeum_sdk.TapeLibrary() # TapeLibrary | 

    try:
        # Updates a specific tape library.
        api_response = api_instance.update_tape_library(tape_library_id, tape_library_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TapeLibrariesApi->update_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **tape_library_body** | [**TapeLibrary**](TapeLibrary.md)|  | 

### Return type

[**TapeLibrary**](TapeLibrary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific tape library. |  -  |
**422** | The received resource was not correctly formatted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

