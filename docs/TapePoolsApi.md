# swagger_client.TapePoolsApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tape_pool**](TapePoolsApi.md#create_tape_pool) | **POST** /tape_pools | Creates a new tape pool.
[**destroy_tape_pool**](TapePoolsApi.md#destroy_tape_pool) | **DELETE** /tape_pools/{tape_pool_id} | Destroys a specific tape pool.
[**index_tape_pools**](TapePoolsApi.md#index_tape_pools) | **GET** /tape_pools | Lists all tape pools.
[**show_tape_pool**](TapePoolsApi.md#show_tape_pool) | **GET** /tape_pools/{tape_pool_id} | Displays a specific tape pool.
[**update_tape_pool**](TapePoolsApi.md#update_tape_pool) | **PUT** /tape_pools/{tape_pool_id} | Updates a specific tape pool.


# **create_tape_pool**
> TapePool create_tape_pool(tape_pool_body)

Creates a new tape pool.

**API Key Scope**: tape_pools / create

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
api_instance = swagger_client.TapePoolsApi(swagger_client.ApiClient(configuration))
tape_pool_body = swagger_client.TapePoolUp() # TapePoolUp | 

try:
    # Creates a new tape pool.
    api_response = api_instance.create_tape_pool(tape_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapePoolsApi->create_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_body** | [**TapePoolUp**](TapePoolUp.md)|  | 

### Return type

[**TapePool**](TapePool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_tape_pool**
> destroy_tape_pool(tape_pool_id)

Destroys a specific tape pool.

**API Key Scope**: tape_pools / destroy

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
api_instance = swagger_client.TapePoolsApi(swagger_client.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.

try:
    # Destroys a specific tape pool.
    api_instance.destroy_tape_pool(tape_pool_id)
except ApiException as e:
    print("Exception when calling TapePoolsApi->destroy_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_id** | **str**| Numeric ID, or name of tape pool. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_tape_pools**
> TapePoolCollection index_tape_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type)

Lists all tape pools.

**API Key Scope**: tape_pools / index

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
api_instance = swagger_client.TapePoolsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
comment = 'comment_example' # str | Filter on comment (optional)
type = 'type_example' # str | Filter on type (optional)

try:
    # Lists all tape pools.
    api_response = api_instance.index_tape_pools(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, comment=comment, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapePoolsApi->index_tape_pools: %s\n" % e)
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
 **type** | **str**| Filter on type | [optional] 

### Return type

[**TapePoolCollection**](TapePoolCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_tape_pool**
> TapePool show_tape_pool(tape_pool_id)

Displays a specific tape pool.

**API Key Scope**: tape_pools / show

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
api_instance = swagger_client.TapePoolsApi(swagger_client.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.

try:
    # Displays a specific tape pool.
    api_response = api_instance.show_tape_pool(tape_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapePoolsApi->show_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_id** | **str**| Numeric ID, or name of tape pool. | 

### Return type

[**TapePool**](TapePool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tape_pool**
> TapePool update_tape_pool(tape_pool_id, tape_pool_body)

Updates a specific tape pool.

**API Key Scope**: tape_pools / update

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
api_instance = swagger_client.TapePoolsApi(swagger_client.ApiClient(configuration))
tape_pool_id = 'tape_pool_id_example' # str | Numeric ID, or name of tape pool.
tape_pool_body = swagger_client.TapePoolUp() # TapePoolUp | 

try:
    # Updates a specific tape pool.
    api_response = api_instance.update_tape_pool(tape_pool_id, tape_pool_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TapePoolsApi->update_tape_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tape_pool_id** | **str**| Numeric ID, or name of tape pool. | 
 **tape_pool_body** | [**TapePoolUp**](TapePoolUp.md)|  | 

### Return type

[**TapePool**](TapePool.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

