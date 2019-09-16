# swagger_client.TapesApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_tapes**](TapesApi.md#index_tapes) | **GET** /tapes | Lists all tapes.
[**index_tapes_by_tape_library**](TapesApi.md#index_tapes_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tapes | Lists all tapes.
[**index_tapes_by_tape_pool**](TapesApi.md#index_tapes_by_tape_pool) | **GET** /tape_pools/{tape_pool_id}/tapes | Lists all tapes.
[**show_tape**](TapesApi.md#show_tape) | **GET** /tapes/{tape_id} | Displays a specific tape.
[**show_tape_by_tape_library**](TapesApi.md#show_tape_by_tape_library) | **GET** /tape_libraries/{tape_library_id}/tapes/{tape_id} | Displays a specific tape.
[**show_tape_by_tape_pool**](TapesApi.md#show_tape_by_tape_pool) | **GET** /tape_pools/{tape_pool_id}/tapes/{tape_id} | Displays a specific tape.


# **index_tapes**
> TapeCollection index_tapes(limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, tape_pool_id=tape_pool_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)

Lists all tapes.

**API Key Scope**: tapes / index

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
api_instance = swagger_client.TapesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tapes_by_tape_library**
> TapeCollection index_tapes_by_tape_library(tape_library_id, limit=limit, offset=offset, sort_by=sort_by, id=id, tape_pool_id=tape_pool_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)

Lists all tapes.

**API Key Scope**: tapes / index

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
api_instance = swagger_client.TapesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tapes_by_tape_pool**
> TapeCollection index_tapes_by_tape_pool(tape_pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, tape_library_id=tape_library_id, barcode=barcode, location=location, type=type, locked=locked, scratch=scratch, cleaning=cleaning, write_protect=write_protect, mounted=mounted, ejected=ejected, known=known, mount_count=mount_count, date_in=date_in, date_move=date_move, free=free, max=max, last_size_update=last_size_update, last_maintenance=last_maintenance, last_repack=last_repack, repack_status=repack_status, hash=hash, force_import_type=force_import_type, need_to_check=need_to_check)

Lists all tapes.

**API Key Scope**: tapes / index

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
api_instance = swagger_client.TapesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape**
> Tape show_tape(tape_id)

Displays a specific tape.

**API Key Scope**: tapes / show

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
api_instance = swagger_client.TapesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape_by_tape_library**
> Tape show_tape_by_tape_library(tape_library_id, tape_id)

Displays a specific tape.

**API Key Scope**: tapes / show

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
api_instance = swagger_client.TapesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape_by_tape_pool**
> Tape show_tape_by_tape_pool(tape_pool_id, tape_id)

Displays a specific tape.

**API Key Scope**: tapes / show

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
api_instance = swagger_client.TapesApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

