# nodeum_sdk.TapesApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_tapes**](TapesApi.md#index_tapes) | **GET** /tapes | Lists all tapes.
[**index_tapes_by_tape_library**](TapesApi.md#index_tapes_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tapes | Lists all tapes.
[**index_tapes_by_tape_pool**](TapesApi.md#index_tapes_by_tape_pool) | **GET** /tape_pools/{tape_pool_id}/tapes | Lists all tapes.
[**mount_status_tape**](TapesApi.md#mount_status_tape) | **GET** /tapes/{tape_id}/mount | Get mount status of Tape.
[**mount_status_tape_by_tape_library**](TapesApi.md#mount_status_tape_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tapes/{tape_id}/mount | Get mount status of Tape.
[**mount_status_tape_by_tape_pool**](TapesApi.md#mount_status_tape_by_tape_pool) | **GET** /tape_pools/{tape_pool_id}/tapes/{tape_id}/mount | Get mount status of Tape.
[**show_tape**](TapesApi.md#show_tape) | **GET** /tapes/{tape_id} | Displays a specific tape.
[**show_tape_by_tape_library**](TapesApi.md#show_tape_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tapes/{tape_id} | Displays a specific tape.
[**show_tape_by_tape_pool**](TapesApi.md#show_tape_by_tape_pool) | **GET** /tape_pools/{tape_pool_id}/tapes/{tape_id} | Displays a specific tape.


# **index_tapes**
> TapeCollection index_tapes(limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, tape_pool_id=tape_pool_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)

Lists all tapes.

**API Key Scope**: tapes / index

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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
tape_library_id = 'tape_library_id_example' # str | Filter on tape library id (optional)
tape_pool_id = 'tape_pool_id_example' # str | Filter on tape pool id (optional)
barcode = 'barcode_example' # str | Filter on barcode (optional)
location = 'location_example' # str | Filter on location (optional)
type = 'type_example' # str | Filter on type (optional)
locked = 'locked_example' # str | Filter on locked (optional)
scratch = 'scratch_example' # str | Filter on scratch (optional)
cleaning = 'cleaning_example' # str | Filter on cleaning (optional)
write_protect = 'write_protect_example' # str | Filter on write protect (optional)
mounted = 'mounted_example' # str | Filter on mounted (optional)
ejected = 'ejected_example' # str | Filter on ejected (optional)
known = 'known_example' # str | Filter on known (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
date_in = 'date_in_example' # str | Filter on date in (optional)
date_move = 'date_move_example' # str | Filter on date move (optional)
free = 'free_example' # str | Filter on free (optional)
max = 'max_example' # str | Filter on max (optional)
last_size_update = 'last_size_update_example' # str | Filter on last size update (optional)
last_maintenance = 'last_maintenance_example' # str | Filter on last maintenance (optional)
last_repack = 'last_repack_example' # str | Filter on last repack (optional)
repack_status = 'repack_status_example' # str | Filter on repack status (optional)
hash = 'hash_example' # str | Filter on hash (optional)
force_import_type = 'force_import_type_example' # str | Filter on force import type (optional)
need_to_check = 'need_to_check_example' # str | Filter on need to check (optional)

try:
    # Lists all tapes.
    api_response = api_instance.index_tapes(limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, tape_pool_id=tape_pool_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->index_tapes: %s\n" % e)
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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
tape_library_id = 'tape_library_id_example' # str | Filter on tape library id (optional)
tape_pool_id = 'tape_pool_id_example' # str | Filter on tape pool id (optional)
barcode = 'barcode_example' # str | Filter on barcode (optional)
location = 'location_example' # str | Filter on location (optional)
type = 'type_example' # str | Filter on type (optional)
locked = 'locked_example' # str | Filter on locked (optional)
scratch = 'scratch_example' # str | Filter on scratch (optional)
cleaning = 'cleaning_example' # str | Filter on cleaning (optional)
write_protect = 'write_protect_example' # str | Filter on write protect (optional)
mounted = 'mounted_example' # str | Filter on mounted (optional)
ejected = 'ejected_example' # str | Filter on ejected (optional)
known = 'known_example' # str | Filter on known (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
date_in = 'date_in_example' # str | Filter on date in (optional)
date_move = 'date_move_example' # str | Filter on date move (optional)
free = 'free_example' # str | Filter on free (optional)
max = 'max_example' # str | Filter on max (optional)
last_size_update = 'last_size_update_example' # str | Filter on last size update (optional)
last_maintenance = 'last_maintenance_example' # str | Filter on last maintenance (optional)
last_repack = 'last_repack_example' # str | Filter on last repack (optional)
repack_status = 'repack_status_example' # str | Filter on repack status (optional)
hash = 'hash_example' # str | Filter on hash (optional)
force_import_type = 'force_import_type_example' # str | Filter on force import type (optional)
need_to_check = 'need_to_check_example' # str | Filter on need to check (optional)

try:
    # Lists all tapes.
    api_response = api_instance.index_tapes(limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, tape_pool_id=tape_pool_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->index_tapes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **tape_library_id** | **str**| Filter on tape library id | [optional] 
 **tape_pool_id** | **str**| Filter on tape pool id | [optional] 
 **barcode** | **str**| Filter on barcode | [optional] 
 **location** | **str**| Filter on location | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **locked** | **str**| Filter on locked | [optional] 
 **scratch** | **str**| Filter on scratch | [optional] 
 **cleaning** | **str**| Filter on cleaning | [optional] 
 **write_protect** | **str**| Filter on write protect | [optional] 
 **mounted** | **str**| Filter on mounted | [optional] 
 **ejected** | **str**| Filter on ejected | [optional] 
 **known** | **str**| Filter on known | [optional] 
 **mount_count** | **str**| Filter on mount count | [optional] 
 **date_in** | **str**| Filter on date in | [optional] 
 **date_move** | **str**| Filter on date move | [optional] 
 **free** | **str**| Filter on free | [optional] 
 **max** | **str**| Filter on max | [optional] 
 **last_size_update** | **str**| Filter on last size update | [optional] 
 **last_maintenance** | **str**| Filter on last maintenance | [optional] 
 **last_repack** | **str**| Filter on last repack | [optional] 
 **repack_status** | **str**| Filter on repack status | [optional] 
 **hash** | **str**| Filter on hash | [optional] 
 **force_import_type** | **str**| Filter on force import type | [optional] 
 **need_to_check** | **str**| Filter on need to check | [optional] 

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

# **index_tapes_by_tape_library**
> TapeCollection index_tapes_by_tape_library(tape_library_id, limit=limit, offset=offset, sort_by=sort_by, id=id, tape_pool_id=tape_pool_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)

Lists all tapes.

**API Key Scope**: tapes / index

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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
tape_pool_id = 'tape_pool_id_example' # str | Filter on tape pool id (optional)
barcode = 'barcode_example' # str | Filter on barcode (optional)
location = 'location_example' # str | Filter on location (optional)
type = 'type_example' # str | Filter on type (optional)
locked = 'locked_example' # str | Filter on locked (optional)
scratch = 'scratch_example' # str | Filter on scratch (optional)
cleaning = 'cleaning_example' # str | Filter on cleaning (optional)
write_protect = 'write_protect_example' # str | Filter on write protect (optional)
mounted = 'mounted_example' # str | Filter on mounted (optional)
ejected = 'ejected_example' # str | Filter on ejected (optional)
known = 'known_example' # str | Filter on known (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
date_in = 'date_in_example' # str | Filter on date in (optional)
date_move = 'date_move_example' # str | Filter on date move (optional)
free = 'free_example' # str | Filter on free (optional)
max = 'max_example' # str | Filter on max (optional)
last_size_update = 'last_size_update_example' # str | Filter on last size update (optional)
last_maintenance = 'last_maintenance_example' # str | Filter on last maintenance (optional)
last_repack = 'last_repack_example' # str | Filter on last repack (optional)
repack_status = 'repack_status_example' # str | Filter on repack status (optional)
hash = 'hash_example' # str | Filter on hash (optional)
force_import_type = 'force_import_type_example' # str | Filter on force import type (optional)
need_to_check = 'need_to_check_example' # str | Filter on need to check (optional)

try:
    # Lists all tapes.
    api_response = api_instance.index_tapes_by_tape_library(tape_library_id, limit=limit, offset=offset, sort_by=sort_by, id=id, tape_pool_id=tape_pool_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->index_tapes_by_tape_library: %s\n" % e)
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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
tape_pool_id = 'tape_pool_id_example' # str | Filter on tape pool id (optional)
barcode = 'barcode_example' # str | Filter on barcode (optional)
location = 'location_example' # str | Filter on location (optional)
type = 'type_example' # str | Filter on type (optional)
locked = 'locked_example' # str | Filter on locked (optional)
scratch = 'scratch_example' # str | Filter on scratch (optional)
cleaning = 'cleaning_example' # str | Filter on cleaning (optional)
write_protect = 'write_protect_example' # str | Filter on write protect (optional)
mounted = 'mounted_example' # str | Filter on mounted (optional)
ejected = 'ejected_example' # str | Filter on ejected (optional)
known = 'known_example' # str | Filter on known (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
date_in = 'date_in_example' # str | Filter on date in (optional)
date_move = 'date_move_example' # str | Filter on date move (optional)
free = 'free_example' # str | Filter on free (optional)
max = 'max_example' # str | Filter on max (optional)
last_size_update = 'last_size_update_example' # str | Filter on last size update (optional)
last_maintenance = 'last_maintenance_example' # str | Filter on last maintenance (optional)
last_repack = 'last_repack_example' # str | Filter on last repack (optional)
repack_status = 'repack_status_example' # str | Filter on repack status (optional)
hash = 'hash_example' # str | Filter on hash (optional)
force_import_type = 'force_import_type_example' # str | Filter on force import type (optional)
need_to_check = 'need_to_check_example' # str | Filter on need to check (optional)

try:
    # Lists all tapes.
    api_response = api_instance.index_tapes_by_tape_library(tape_library_id, limit=limit, offset=offset, sort_by=sort_by, id=id, tape_pool_id=tape_pool_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->index_tapes_by_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **tape_pool_id** | **str**| Filter on tape pool id | [optional] 
 **barcode** | **str**| Filter on barcode | [optional] 
 **location** | **str**| Filter on location | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **locked** | **str**| Filter on locked | [optional] 
 **scratch** | **str**| Filter on scratch | [optional] 
 **cleaning** | **str**| Filter on cleaning | [optional] 
 **write_protect** | **str**| Filter on write protect | [optional] 
 **mounted** | **str**| Filter on mounted | [optional] 
 **ejected** | **str**| Filter on ejected | [optional] 
 **known** | **str**| Filter on known | [optional] 
 **mount_count** | **str**| Filter on mount count | [optional] 
 **date_in** | **str**| Filter on date in | [optional] 
 **date_move** | **str**| Filter on date move | [optional] 
 **free** | **str**| Filter on free | [optional] 
 **max** | **str**| Filter on max | [optional] 
 **last_size_update** | **str**| Filter on last size update | [optional] 
 **last_maintenance** | **str**| Filter on last maintenance | [optional] 
 **last_repack** | **str**| Filter on last repack | [optional] 
 **repack_status** | **str**| Filter on repack status | [optional] 
 **hash** | **str**| Filter on hash | [optional] 
 **force_import_type** | **str**| Filter on force import type | [optional] 
 **need_to_check** | **str**| Filter on need to check | [optional] 

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

# **index_tapes_by_tape_pool**
> TapeCollection index_tapes_by_tape_pool(tape_pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)

Lists all tapes.

**API Key Scope**: tapes / index

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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
tape_library_id = 'tape_library_id_example' # str | Filter on tape library id (optional)
barcode = 'barcode_example' # str | Filter on barcode (optional)
location = 'location_example' # str | Filter on location (optional)
type = 'type_example' # str | Filter on type (optional)
locked = 'locked_example' # str | Filter on locked (optional)
scratch = 'scratch_example' # str | Filter on scratch (optional)
cleaning = 'cleaning_example' # str | Filter on cleaning (optional)
write_protect = 'write_protect_example' # str | Filter on write protect (optional)
mounted = 'mounted_example' # str | Filter on mounted (optional)
ejected = 'ejected_example' # str | Filter on ejected (optional)
known = 'known_example' # str | Filter on known (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
date_in = 'date_in_example' # str | Filter on date in (optional)
date_move = 'date_move_example' # str | Filter on date move (optional)
free = 'free_example' # str | Filter on free (optional)
max = 'max_example' # str | Filter on max (optional)
last_size_update = 'last_size_update_example' # str | Filter on last size update (optional)
last_maintenance = 'last_maintenance_example' # str | Filter on last maintenance (optional)
last_repack = 'last_repack_example' # str | Filter on last repack (optional)
repack_status = 'repack_status_example' # str | Filter on repack status (optional)
hash = 'hash_example' # str | Filter on hash (optional)
force_import_type = 'force_import_type_example' # str | Filter on force import type (optional)
need_to_check = 'need_to_check_example' # str | Filter on need to check (optional)

try:
    # Lists all tapes.
    api_response = api_instance.index_tapes_by_tape_pool(tape_pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->index_tapes_by_tape_pool: %s\n" % e)
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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
tape_library_id = 'tape_library_id_example' # str | Filter on tape library id (optional)
barcode = 'barcode_example' # str | Filter on barcode (optional)
location = 'location_example' # str | Filter on location (optional)
type = 'type_example' # str | Filter on type (optional)
locked = 'locked_example' # str | Filter on locked (optional)
scratch = 'scratch_example' # str | Filter on scratch (optional)
cleaning = 'cleaning_example' # str | Filter on cleaning (optional)
write_protect = 'write_protect_example' # str | Filter on write protect (optional)
mounted = 'mounted_example' # str | Filter on mounted (optional)
ejected = 'ejected_example' # str | Filter on ejected (optional)
known = 'known_example' # str | Filter on known (optional)
mount_count = 'mount_count_example' # str | Filter on mount count (optional)
date_in = 'date_in_example' # str | Filter on date in (optional)
date_move = 'date_move_example' # str | Filter on date move (optional)
free = 'free_example' # str | Filter on free (optional)
max = 'max_example' # str | Filter on max (optional)
last_size_update = 'last_size_update_example' # str | Filter on last size update (optional)
last_maintenance = 'last_maintenance_example' # str | Filter on last maintenance (optional)
last_repack = 'last_repack_example' # str | Filter on last repack (optional)
repack_status = 'repack_status_example' # str | Filter on repack status (optional)
hash = 'hash_example' # str | Filter on hash (optional)
force_import_type = 'force_import_type_example' # str | Filter on force import type (optional)
need_to_check = 'need_to_check_example' # str | Filter on need to check (optional)

try:
    # Lists all tapes.
    api_response = api_instance.index_tapes_by_tape_pool(tape_pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->index_tapes_by_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_id** | **str**| Numeric ID, or name of tape pool. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **tape_library_id** | **str**| Filter on tape library id | [optional] 
 **barcode** | **str**| Filter on barcode | [optional] 
 **location** | **str**| Filter on location | [optional] 
 **type** | **str**| Filter on type | [optional] 
 **locked** | **str**| Filter on locked | [optional] 
 **scratch** | **str**| Filter on scratch | [optional] 
 **cleaning** | **str**| Filter on cleaning | [optional] 
 **write_protect** | **str**| Filter on write protect | [optional] 
 **mounted** | **str**| Filter on mounted | [optional] 
 **ejected** | **str**| Filter on ejected | [optional] 
 **known** | **str**| Filter on known | [optional] 
 **mount_count** | **str**| Filter on mount count | [optional] 
 **date_in** | **str**| Filter on date in | [optional] 
 **date_move** | **str**| Filter on date move | [optional] 
 **free** | **str**| Filter on free | [optional] 
 **max** | **str**| Filter on max | [optional] 
 **last_size_update** | **str**| Filter on last size update | [optional] 
 **last_maintenance** | **str**| Filter on last maintenance | [optional] 
 **last_repack** | **str**| Filter on last repack | [optional] 
 **repack_status** | **str**| Filter on repack status | [optional] 
 **hash** | **str**| Filter on hash | [optional] 
 **force_import_type** | **str**| Filter on force import type | [optional] 
 **need_to_check** | **str**| Filter on need to check | [optional] 

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

# **mount_status_tape**
> MountStatus mount_status_tape(tape_id)

Get mount status of Tape.

**API Key Scope**: tapes / mount_status

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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Get mount status of Tape.
    api_response = api_instance.mount_status_tape(tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->mount_status_tape: %s\n" % e)
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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Get mount status of Tape.
    api_response = api_instance.mount_status_tape(tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->mount_status_tape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_id** | **str**| Numeric ID, or barcode of tape. | 

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

# **mount_status_tape_by_tape_library**
> MountStatus mount_status_tape_by_tape_library(tape_library_id, tape_id)

Get mount status of Tape.

**API Key Scope**: tapes / mount_status

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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Get mount status of Tape.
    api_response = api_instance.mount_status_tape_by_tape_library(tape_library_id, tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->mount_status_tape_by_tape_library: %s\n" % e)
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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Get mount status of Tape.
    api_response = api_instance.mount_status_tape_by_tape_library(tape_library_id, tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->mount_status_tape_by_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **tape_id** | **str**| Numeric ID, or barcode of tape. | 

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

# **mount_status_tape_by_tape_pool**
> MountStatus mount_status_tape_by_tape_pool(tape_pool_id, tape_id)

Get mount status of Tape.

**API Key Scope**: tapes / mount_status

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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Get mount status of Tape.
    api_response = api_instance.mount_status_tape_by_tape_pool(tape_pool_id, tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->mount_status_tape_by_tape_pool: %s\n" % e)
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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Get mount status of Tape.
    api_response = api_instance.mount_status_tape_by_tape_pool(tape_pool_id, tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->mount_status_tape_by_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_id** | **str**| Numeric ID, or name of tape pool. | 
 **tape_id** | **str**| Numeric ID, or barcode of tape. | 

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

# **show_tape**
> Tape show_tape(tape_id)

Displays a specific tape.

**API Key Scope**: tapes / show

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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Displays a specific tape.
    api_response = api_instance.show_tape(tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->show_tape: %s\n" % e)
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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Displays a specific tape.
    api_response = api_instance.show_tape(tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->show_tape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_id** | **str**| Numeric ID, or barcode of tape. | 

### Return type

[**Tape**](Tape.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific tape. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape_by_tape_library**
> Tape show_tape_by_tape_library(tape_library_id, tape_id)

Displays a specific tape.

**API Key Scope**: tapes / show

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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Displays a specific tape.
    api_response = api_instance.show_tape_by_tape_library(tape_library_id, tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->show_tape_by_tape_library: %s\n" % e)
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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_library_id = 'tape_library_id_example' # str | Numeric ID, serial, or name of tape library.
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Displays a specific tape.
    api_response = api_instance.show_tape_by_tape_library(tape_library_id, tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->show_tape_by_tape_library: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_library_id** | **str**| Numeric ID, serial, or name of tape library. | 
 **tape_id** | **str**| Numeric ID, or barcode of tape. | 

### Return type

[**Tape**](Tape.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific tape. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape_by_tape_pool**
> Tape show_tape_by_tape_pool(tape_pool_id, tape_id)

Displays a specific tape.

**API Key Scope**: tapes / show

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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Displays a specific tape.
    api_response = api_instance.show_tape_by_tape_pool(tape_pool_id, tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->show_tape_by_tape_pool: %s\n" % e)
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
api_instance = nodeum_sdk.TapesApi(nodeum_sdk.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
tape_id = 'tape_id_example' # str | Numeric ID, or barcode of tape.

try:
    # Displays a specific tape.
    api_response = api_instance.show_tape_by_tape_pool(tape_pool_id, tape_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapesApi->show_tape_by_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_id** | **str**| Numeric ID, or name of tape pool. | 
 **tape_id** | **str**| Numeric ID, or barcode of tape. | 

### Return type

[**Tape**](Tape.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific tape. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

