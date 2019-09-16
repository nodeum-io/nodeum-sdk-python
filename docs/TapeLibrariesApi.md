# swagger_client.TapeLibrariesApi

All URIs are relative to *https://localhost/api/v2*

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
api_instance = swagger_client.TapeLibrariesApi(swagger_client.ApiClient(configuration))
tape_library_body = swagger_client.TapeLibrary() # TapeLibrary | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_tape_library**
> destroy_tape_library(tape_library_id)

Destroys a specific tape library.

**API Key Scope**: tape_libraries / destroy

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
api_instance = swagger_client.TapeLibrariesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tape_libraries**
> TapeLibraryCollection index_tape_libraries(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, serial=serial, comment=comment, protocol=protocol, vendor=vendor, product=product, firmware=firmware, device=device, libso=libso, acs=acs, status=status, storage_slots=storage_slots, storage_slots_address=storage_slots_address, io_slots=io_slots, io_slots_address=io_slots_address, price=price)

Lists all tape libraries.

**API Key Scope**: tape_libraries / index

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
api_instance = swagger_client.TapeLibrariesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tape_library_devices**
> TapeLibraryDeviceCollection index_tape_library_devices(job_id=job_id)

Lists tape libraries devices.

**API Key Scope**: tape_libraries / devices

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
api_instance = swagger_client.TapeLibrariesApi(swagger_client.ApiClient(configuration))
job_id = 'job_id_example' # str | ID of active job (optional)

try:
    # Lists tape libraries devices.
    api_response = api_instance.index_tape_library_devices(job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapeLibrariesApi->index_tape_library_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| ID of active job | [optional] 

### Return type

[**TapeLibraryDeviceCollection**](TapeLibraryDeviceCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape_library**
> TapeLibrary show_tape_library(tape_library_id)

Displays a specific tape library.

**API Key Scope**: tape_libraries / show

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
api_instance = swagger_client.TapeLibrariesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tape_library**
> TapeLibrary update_tape_library(tape_library_id, tape_library_body)

Updates a specific tape library.

**API Key Scope**: tape_libraries / update

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
api_instance = swagger_client.TapeLibrariesApi(swagger_client.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_library_body = swagger_client.TapeLibrary() # TapeLibrary | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

