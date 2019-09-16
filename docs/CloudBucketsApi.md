# swagger_client.CloudBucketsApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_cloud_buckets**](CloudBucketsApi.md#index_cloud_buckets) | **GET** /cloud_buckets | Lists all cloud buckets.
[**index_cloud_buckets_by_cloud_connector**](CloudBucketsApi.md#index_cloud_buckets_by_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets | Lists all cloud buckets.
[**index_cloud_buckets_by_cloud_pool**](CloudBucketsApi.md#index_cloud_buckets_by_cloud_pool) | **GET** /cloud_pools/{cloud_pool_id}/cloud_buckets | Lists all cloud buckets.
[**show_cloud_bucket**](CloudBucketsApi.md#show_cloud_bucket) | **GET** /cloud_buckets/{cloud_bucket_id} | Displays a specific cloud bucket.
[**show_cloud_bucket_by_cloud_connector**](CloudBucketsApi.md#show_cloud_bucket_by_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets/{cloud_bucket_id} | Displays a specific cloud bucket.
[**show_cloud_bucket_by_cloud_pool**](CloudBucketsApi.md#show_cloud_bucket_by_cloud_pool) | **GET** /cloud_pools/{cloud_pool_id}/cloud_buckets/{cloud_bucket_id} | Displays a specific cloud bucket.
[**sync_cloud_buckets**](CloudBucketsApi.md#sync_cloud_buckets) | **PUT** /cloud_connectors/{cloud_connector_id}/cloud_buckets/-/sync | Synchronize internal cloud buckets with their remote equivalent.
[**sync_result_cloud_buckets**](CloudBucketsApi.md#sync_result_cloud_buckets) | **GET** /cloud_connectors/{cloud_connector_id}/cloud_buckets/-/sync | Check result of cloud connector sync job.


# **index_cloud_buckets**
> CloudBucketCollection index_cloud_buckets(limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_connector_id=cloud_connector_id, cloud_pool_id=cloud_pool_id, name=name, location=location, price=price)

Lists all cloud buckets.

**API Key Scope**: cloud_buckets / index

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
api_instance = swagger_client.CloudBucketsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
cloud_connector_id = 'cloud_connector_id_example' # str | Filter on cloud connector id (optional)
cloud_pool_id = 'cloud_pool_id_example' # str | Filter on cloud pool id (optional)
name = 'name_example' # str | Filter on name (optional)
location = 'location_example' # str | Filter on location (optional)
price = 'price_example' # str | Filter on price (optional)

try:
    # Lists all cloud buckets.
    api_response = api_instance.index_cloud_buckets(limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_connector_id=cloud_connector_id, cloud_pool_id=cloud_pool_id, name=name, location=location, price=price)
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
 **cloud_pool_id** | **str**| Filter on cloud pool id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **location** | **str**| Filter on location | [optional] 
 **price** | **str**| Filter on price | [optional] 

### Return type

[**CloudBucketCollection**](CloudBucketCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_cloud_buckets_by_cloud_connector**
> CloudBucketCollection index_cloud_buckets_by_cloud_connector(cloud_connector_id, limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_pool_id=cloud_pool_id, name=name, location=location, price=price)

Lists all cloud buckets.

**API Key Scope**: cloud_buckets / index

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
api_instance = swagger_client.CloudBucketsApi(swagger_client.ApiClient(configuration))
cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
cloud_pool_id = 'cloud_pool_id_example' # str | Filter on cloud pool id (optional)
name = 'name_example' # str | Filter on name (optional)
location = 'location_example' # str | Filter on location (optional)
price = 'price_example' # str | Filter on price (optional)

try:
    # Lists all cloud buckets.
    api_response = api_instance.index_cloud_buckets_by_cloud_connector(cloud_connector_id, limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_pool_id=cloud_pool_id, name=name, location=location, price=price)
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
 **cloud_pool_id** | **str**| Filter on cloud pool id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **location** | **str**| Filter on location | [optional] 
 **price** | **str**| Filter on price | [optional] 

### Return type

[**CloudBucketCollection**](CloudBucketCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_cloud_buckets_by_cloud_pool**
> CloudBucketCollection index_cloud_buckets_by_cloud_pool(cloud_pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_connector_id=cloud_connector_id, name=name, location=location, price=price)

Lists all cloud buckets.

**API Key Scope**: cloud_buckets / index

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
api_instance = swagger_client.CloudBucketsApi(swagger_client.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
cloud_connector_id = 'cloud_connector_id_example' # str | Filter on cloud connector id (optional)
name = 'name_example' # str | Filter on name (optional)
location = 'location_example' # str | Filter on location (optional)
price = 'price_example' # str | Filter on price (optional)

try:
    # Lists all cloud buckets.
    api_response = api_instance.index_cloud_buckets_by_cloud_pool(cloud_pool_id, limit=limit, offset=offset, sort_by=sort_by, id=id, cloud_connector_id=cloud_connector_id, name=name, location=location, price=price)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudBucketsApi->index_cloud_buckets_by_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Numeric ID or name of cloud pool. | 
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_cloud_bucket**
> CloudBucket show_cloud_bucket(cloud_bucket_id)

Displays a specific cloud bucket.

**API Key Scope**: cloud_buckets / show

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
api_instance = swagger_client.CloudBucketsApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_cloud_bucket_by_cloud_connector**
> CloudBucket show_cloud_bucket_by_cloud_connector(cloud_connector_id, cloud_bucket_id)

Displays a specific cloud bucket.

**API Key Scope**: cloud_buckets / show

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
api_instance = swagger_client.CloudBucketsApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_cloud_bucket_by_cloud_pool**
> CloudBucket show_cloud_bucket_by_cloud_pool(cloud_pool_id, cloud_bucket_id)

Displays a specific cloud bucket.

**API Key Scope**: cloud_buckets / show

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
api_instance = swagger_client.CloudBucketsApi(swagger_client.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Numeric ID or name of cloud pool.
cloud_bucket_id = 'cloud_bucket_id_example' # str | Numeric ID or name of cloud bucket.

try:
    # Displays a specific cloud bucket.
    api_response = api_instance.show_cloud_bucket_by_cloud_pool(cloud_pool_id, cloud_bucket_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudBucketsApi->show_cloud_bucket_by_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Numeric ID or name of cloud pool. | 
 **cloud_bucket_id** | **str**| Numeric ID or name of cloud bucket. | 

### Return type

[**CloudBucket**](CloudBucket.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_cloud_buckets**
> ActiveJobStatus sync_cloud_buckets(cloud_connector_id)

Synchronize internal cloud buckets with their remote equivalent.

**API Key Scope**: cloud_buckets / sync

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
api_instance = swagger_client.CloudBucketsApi(swagger_client.ApiClient(configuration))
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_result_cloud_buckets**
> CloudBucketSimpleCollection sync_result_cloud_buckets(cloud_connector_id, job_id=job_id)

Check result of cloud connector sync job.

**API Key Scope**: cloud_buckets / sync

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
api_instance = swagger_client.CloudBucketsApi(swagger_client.ApiClient(configuration))
cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
job_id = 'job_id_example' # str | ID of active job (optional)

try:
    # Check result of cloud connector sync job.
    api_response = api_instance.sync_result_cloud_buckets(cloud_connector_id, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudBucketsApi->sync_result_cloud_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 
 **job_id** | **str**| ID of active job | [optional] 

### Return type

[**CloudBucketSimpleCollection**](CloudBucketSimpleCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

