# nodeum_sdk.CloudBucketsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_cloud_buckets**](CloudBucketsApi.md#index_cloud_buckets) | **GET** /cloud_buckets | Lists all cloud buckets.
[**index_cloud_buckets_by_cloud_connector**](CloudBucketsApi.md#index_cloud_buckets_by_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets | Lists all cloud buckets.
[**index_cloud_buckets_by_pool**](CloudBucketsApi.md#index_cloud_buckets_by_pool) | **GET** /pools/{pool_id}/cloud_buckets | Lists all cloud buckets from pool.
[**mount_status_cloud_bucket**](CloudBucketsApi.md#mount_status_cloud_bucket) | **GET** /cloud_buckets/{cloud_bucket_id}/mount | Get mount status of Cloud bucket.
[**mount_status_cloud_bucket_by_cloud_connector**](CloudBucketsApi.md#mount_status_cloud_bucket_by_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets/{cloud_bucket_id}/mount | Get mount status of Cloud bucket.
[**mount_status_cloud_bucket_by_pool**](CloudBucketsApi.md#mount_status_cloud_bucket_by_pool) | **GET** /pools/{pool_id}/cloud_buckets/{cloud_bucket_id}/mount | Get mount status of Cloud bucket.
[**show_cloud_bucket**](CloudBucketsApi.md#show_cloud_bucket) | **GET** /cloud_buckets/{cloud_bucket_id} | Displays a specific cloud bucket.
[**show_cloud_bucket_by_cloud_connector**](CloudBucketsApi.md#show_cloud_bucket_by_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets/{cloud_bucket_id} | Displays a specific cloud bucket.
[**show_cloud_bucket_by_pool**](CloudBucketsApi.md#show_cloud_bucket_by_pool) | **GET** /pools/{pool_id}/cloud_buckets/{cloud_bucket_id} | Displays a specific cloud bucket.
[**sync_cloud_buckets**](CloudBucketsApi.md#sync_cloud_buckets) | **PUT** /cloud_connectors/{cloud_connector_id}/cloud_buckets/-/sync | Synchronize internal cloud buckets with their remote equivalent.
[**sync_result_cloud_buckets**](CloudBucketsApi.md#sync_result_cloud_buckets) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets/-/sync | Check result of cloud connector sync job.
[**update_cloud_bucket**](CloudBucketsApi.md#update_cloud_bucket) | **PUT** /cloud_buckets/{cloud_bucket_id} | Updates a specific cloud bucket.
[**update_cloud_bucket_by_cloud_connector**](CloudBucketsApi.md#update_cloud_bucket_by_cloud_connector) | **PUT** /cloud_connectors/{cloud_connector_id}/cloud_buckets/{cloud_bucket_id} | Updates a specific cloud bucket.
[**update_cloud_bucket_by_pool**](CloudBucketsApi.md#update_cloud_bucket_by_pool) | **PUT** /pools/{pool_id}/cloud_buckets/{cloud_bucket_id} | Updates a specific cloud bucket.
[**update_config_file_cloud_bucket**](CloudBucketsApi.md#update_config_file_cloud_bucket) | **PUT** /cloud_buckets/{cloud_bucket_id}/config_file | Updates a specific cloud bucket.


# **index_cloud_buckets**
> CloudBucketCollection index_cloud_buckets(limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_connector_id=cloud_connector_id, pool_id=pool_id, name=name, location=location, price=price)

Lists all cloud buckets.

**API Key Scope**: cloud_buckets / index

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **cloud_connector_id** | **str**| Filter on cloud connector id | [optional] 
 **pool_id** | **str**| Filter on a pool id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **location** | **str**| Filter on location | [optional] 
 **price** | **str**| Filter on price | [optional] 

### Return type

[**CloudBucketCollection**](CloudBucketCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of cloud buckets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_cloud_buckets_by_cloud_connector**
> CloudBucketCollection index_cloud_buckets_by_cloud_connector(cloud_connector_id, limit=limit, offset=offset, sort_by=sort_by, id=id, pool_id=pool_id, name=name, location=location, price=price)

Lists all cloud buckets.

**API Key Scope**: cloud_buckets / index

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
pool_id = 'pool_id_example' # str | Filter on a pool id (optional)
name = 'name_example' # str | Filter on name (optional)
location = 'location_example' # str | Filter on location (optional)
price = 'price_example' # str | Filter on price (optional)

    try:
        # Lists all cloud buckets.
        api_response = api_instance.index_cloud_buckets_by_cloud_connector(cloud_connector_id, limit=limit, offset=offset, sort_by=sort_by, id=id, pool_id=pool_id, name=name, location=location, price=price)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->index_cloud_buckets_by_cloud_connector: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
pool_id = 'pool_id_example' # str | Filter on a pool id (optional)
name = 'name_example' # str | Filter on name (optional)
location = 'location_example' # str | Filter on location (optional)
price = 'price_example' # str | Filter on price (optional)

    try:
        # Lists all cloud buckets.
        api_response = api_instance.index_cloud_buckets_by_cloud_connector(cloud_connector_id, limit=limit, offset=offset, sort_by=sort_by, id=id, pool_id=pool_id, name=name, location=location, price=price)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->index_cloud_buckets_by_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **pool_id** | **str**| Filter on a pool id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **location** | **str**| Filter on location | [optional] 
 **price** | **str**| Filter on price | [optional] 

### Return type

[**CloudBucketCollection**](CloudBucketCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of cloud buckets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_cloud_buckets_by_pool**
> CloudBucketCollection index_cloud_buckets_by_pool(pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_connector_id=cloud_connector_id, name=name, location=location, price=price)

Lists all cloud buckets from pool.

**API Key Scope**: cloud_buckets / index

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
cloud_connector_id = 'cloud_connector_id_example' # str | Filter on cloud connector id (optional)
name = 'name_example' # str | Filter on name (optional)
location = 'location_example' # str | Filter on location (optional)
price = 'price_example' # str | Filter on price (optional)

    try:
        # Lists all cloud buckets from pool.
        api_response = api_instance.index_cloud_buckets_by_pool(pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_connector_id=cloud_connector_id, name=name, location=location, price=price)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->index_cloud_buckets_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
cloud_connector_id = 'cloud_connector_id_example' # str | Filter on cloud connector id (optional)
name = 'name_example' # str | Filter on name (optional)
location = 'location_example' # str | Filter on location (optional)
price = 'price_example' # str | Filter on price (optional)

    try:
        # Lists all cloud buckets from pool.
        api_response = api_instance.index_cloud_buckets_by_pool(pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_connector_id=cloud_connector_id, name=name, location=location, price=price)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->index_cloud_buckets_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **cloud_connector_id** | **str**| Filter on cloud connector id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **location** | **str**| Filter on location | [optional] 
 **price** | **str**| Filter on price | [optional] 

### Return type

[**CloudBucketCollection**](CloudBucketCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of cloud buckets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mount_status_cloud_bucket**
> MountStatus mount_status_cloud_bucket(cloud_bucket_id)

Get mount status of Cloud bucket.

**API Key Scope**: cloud_buckets / mount_status

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Get mount status of Cloud bucket.
        api_response = api_instance.mount_status_cloud_bucket(cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->mount_status_cloud_bucket: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Get mount status of Cloud bucket.
        api_response = api_instance.mount_status_cloud_bucket(cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->mount_status_cloud_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 

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

# **mount_status_cloud_bucket_by_cloud_connector**
> MountStatus mount_status_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id)

Get mount status of Cloud bucket.

**API Key Scope**: cloud_buckets / mount_status

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Get mount status of Cloud bucket.
        api_response = api_instance.mount_status_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->mount_status_cloud_bucket_by_cloud_connector: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Get mount status of Cloud bucket.
        api_response = api_instance.mount_status_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->mount_status_cloud_bucket_by_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 

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

# **mount_status_cloud_bucket_by_pool**
> MountStatus mount_status_cloud_bucket_by_pool(pool_id, cloud_bucket_id)

Get mount status of Cloud bucket.

**API Key Scope**: cloud_buckets / mount_status

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Get mount status of Cloud bucket.
        api_response = api_instance.mount_status_cloud_bucket_by_pool(pool_id, cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->mount_status_cloud_bucket_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Get mount status of Cloud bucket.
        api_response = api_instance.mount_status_cloud_bucket_by_pool(pool_id, cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->mount_status_cloud_bucket_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 

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

# **show_cloud_bucket**
> CloudBucket show_cloud_bucket(cloud_bucket_id)

Displays a specific cloud bucket.

**API Key Scope**: cloud_buckets / show

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Displays a specific cloud bucket.
        api_response = api_instance.show_cloud_bucket(cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->show_cloud_bucket: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Displays a specific cloud bucket.
        api_response = api_instance.show_cloud_bucket(cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->show_cloud_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 

### Return type

[**CloudBucket**](CloudBucket.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific cloud bucket. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_cloud_bucket_by_cloud_connector**
> CloudBucket show_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id)

Displays a specific cloud bucket.

**API Key Scope**: cloud_buckets / show

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Displays a specific cloud bucket.
        api_response = api_instance.show_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->show_cloud_bucket_by_cloud_connector: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Displays a specific cloud bucket.
        api_response = api_instance.show_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->show_cloud_bucket_by_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 

### Return type

[**CloudBucket**](CloudBucket.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific cloud bucket. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_cloud_bucket_by_pool**
> CloudBucket show_cloud_bucket_by_pool(pool_id, cloud_bucket_id)

Displays a specific cloud bucket.

**API Key Scope**: cloud_buckets / show

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Displays a specific cloud bucket.
        api_response = api_instance.show_cloud_bucket_by_pool(pool_id, cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->show_cloud_bucket_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

    try:
        # Displays a specific cloud bucket.
        api_response = api_instance.show_cloud_bucket_by_pool(pool_id, cloud_bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->show_cloud_bucket_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 

### Return type

[**CloudBucket**](CloudBucket.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific cloud bucket. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_cloud_buckets**
> ActiveJobStatus sync_cloud_buckets(cloud_connector_id)

Synchronize internal cloud buckets with their remote equivalent.

**API Key Scope**: cloud_buckets / sync

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.

    try:
        # Synchronize internal cloud buckets with their remote equivalent.
        api_response = api_instance.sync_cloud_buckets(cloud_connector_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->sync_cloud_buckets: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.

    try:
        # Synchronize internal cloud buckets with their remote equivalent.
        api_response = api_instance.sync_cloud_buckets(cloud_connector_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->sync_cloud_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 

### Return type

[**ActiveJobStatus**](ActiveJobStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, queued, working, failed

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | An active job that may be queued, working, completed or failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_result_cloud_buckets**
> CloudBucketSimpleCollection sync_result_cloud_buckets(cloud_connector_id, job_id)

Check result of cloud connector sync job.

**API Key Scope**: cloud_buckets / sync

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
job_id = 'job_id_example' # str | ID of active job

    try:
        # Check result of cloud connector sync job.
        api_response = api_instance.sync_result_cloud_buckets(cloud_connector_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->sync_result_cloud_buckets: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
job_id = 'job_id_example' # str | ID of active job

    try:
        # Check result of cloud connector sync job.
        api_response = api_instance.sync_result_cloud_buckets(cloud_connector_id, job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->sync_result_cloud_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 
 **job_id** | **str**| ID of active job | 

### Return type

[**CloudBucketSimpleCollection**](CloudBucketSimpleCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, queued, working, failed, 

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Simple list of cloud buckets. |  -  |
**202** | An active job that may be queued, working, completed or failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_bucket**
> CloudBucket update_cloud_bucket(cloud_bucket_id, cloud_bucket_body)

Updates a specific cloud bucket.

**API Key Scope**: cloud_buckets / update

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.
cloud_bucket_body = nodeum_sdk.CloudBucket() # CloudBucket | 

    try:
        # Updates a specific cloud bucket.
        api_response = api_instance.update_cloud_bucket(cloud_bucket_id, cloud_bucket_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->update_cloud_bucket: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.
cloud_bucket_body = nodeum_sdk.CloudBucket() # CloudBucket | 

    try:
        # Updates a specific cloud bucket.
        api_response = api_instance.update_cloud_bucket(cloud_bucket_id, cloud_bucket_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->update_cloud_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 
 **cloud_bucket_body** | [**CloudBucket**](CloudBucket.md)|  | 

### Return type

[**CloudBucket**](CloudBucket.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific cloud bucket. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_bucket_by_cloud_connector**
> CloudBucket update_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id, cloud_bucket_body)

Updates a specific cloud bucket.

**API Key Scope**: cloud_buckets / update

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.
cloud_bucket_body = nodeum_sdk.CloudBucket() # CloudBucket | 

    try:
        # Updates a specific cloud bucket.
        api_response = api_instance.update_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id, cloud_bucket_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->update_cloud_bucket_by_cloud_connector: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.
cloud_bucket_body = nodeum_sdk.CloudBucket() # CloudBucket | 

    try:
        # Updates a specific cloud bucket.
        api_response = api_instance.update_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id, cloud_bucket_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->update_cloud_bucket_by_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 
 **cloud_bucket_body** | [**CloudBucket**](CloudBucket.md)|  | 

### Return type

[**CloudBucket**](CloudBucket.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific cloud bucket. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_bucket_by_pool**
> CloudBucket update_cloud_bucket_by_pool(pool_id, cloud_bucket_id, cloud_bucket_body)

Updates a specific cloud bucket.

**API Key Scope**: cloud_buckets / update

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.
cloud_bucket_body = nodeum_sdk.CloudBucket() # CloudBucket | 

    try:
        # Updates a specific cloud bucket.
        api_response = api_instance.update_cloud_bucket_by_pool(pool_id, cloud_bucket_id, cloud_bucket_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->update_cloud_bucket_by_pool: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    pool_id = 'pool_id_example' # str | Numeric ID, or name of pool.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.
cloud_bucket_body = nodeum_sdk.CloudBucket() # CloudBucket | 

    try:
        # Updates a specific cloud bucket.
        api_response = api_instance.update_cloud_bucket_by_pool(pool_id, cloud_bucket_id, cloud_bucket_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->update_cloud_bucket_by_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pool_id** | **str**| Numeric ID, or name of pool. | 
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 
 **cloud_bucket_body** | [**CloudBucket**](CloudBucket.md)|  | 

### Return type

[**CloudBucket**](CloudBucket.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A specific cloud bucket. |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_file_cloud_bucket**
> str update_config_file_cloud_bucket(cloud_bucket_id, config_file)

Updates a specific cloud bucket.

**API Key Scope**: cloud_buckets / update_config_file

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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.
config_file = '/path/to/file' # file | Config file to upload.

    try:
        # Updates a specific cloud bucket.
        api_response = api_instance.update_config_file_cloud_bucket(cloud_bucket_id, config_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->update_config_file_cloud_bucket: %s\n" % e)
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
    api_instance = nodeum_sdk.CloudBucketsApi(api_client)
    cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.
config_file = '/path/to/file' # file | Config file to upload.

    try:
        # Updates a specific cloud bucket.
        api_response = api_instance.update_config_file_cloud_bucket(cloud_bucket_id, config_file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CloudBucketsApi->update_config_file_cloud_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 
 **config_file** | **file**| Config file to upload. | 

### Return type

**str**

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Remote URI |  -  |
**404** | The requested resource was not found. The detailed error will be of type &#x60;not_found&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

