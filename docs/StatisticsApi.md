# nodeum_sdk.StatisticsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_by_date**](StatisticsApi.md#statistics_by_date) | **GET** /statistics/by_date | Get statistics about files, grouped by date
[**statistics_by_file_extension**](StatisticsApi.md#statistics_by_file_extension) | **GET** /statistics/by_file_extension | Get statistics about files, grouped by file extension
[**statistics_by_group_owner**](StatisticsApi.md#statistics_by_group_owner) | **GET** /statistics/by_group_owner | Get statistics about files, grouped by owner (group)
[**statistics_by_primary_cloud**](StatisticsApi.md#statistics_by_primary_cloud) | **GET** /statistics/by_primary_cloud | Get statistics about files, grouped by primary Cloud
[**statistics_by_primary_name**](StatisticsApi.md#statistics_by_primary_name) | **GET** /statistics/by_primary_name | Get statistics about files, grouped by primary storages
[**statistics_by_primary_nas**](StatisticsApi.md#statistics_by_primary_nas) | **GET** /statistics/by_primary_nas | Get statistics about files, grouped by primary NAS
[**statistics_by_primary_storage**](StatisticsApi.md#statistics_by_primary_storage) | **GET** /statistics/by_primary_storage | Get statistics about files, grouped by primary storage
[**statistics_by_secondary_cloud**](StatisticsApi.md#statistics_by_secondary_cloud) | **GET** /statistics/by_secondary_cloud | Get statistics about files, grouped by secondary Cloud
[**statistics_by_secondary_nas**](StatisticsApi.md#statistics_by_secondary_nas) | **GET** /statistics/by_secondary_nas | Get statistics about files, grouped by secondary NAS
[**statistics_by_secondary_storage**](StatisticsApi.md#statistics_by_secondary_storage) | **GET** /statistics/by_secondary_storage | Get statistics about files, grouped by secondary storage
[**statistics_by_secondary_tape**](StatisticsApi.md#statistics_by_secondary_tape) | **GET** /statistics/by_secondary_tape | Get statistics about files, grouped by secondary Tape
[**statistics_by_size**](StatisticsApi.md#statistics_by_size) | **GET** /statistics/by_size | Get statistics about files, grouped by size
[**statistics_by_user_owner**](StatisticsApi.md#statistics_by_user_owner) | **GET** /statistics/by_user_owner | Get statistics about files, grouped by owner (user)
[**statistics_storage**](StatisticsApi.md#statistics_storage) | **GET** /statistics/storage | Get statistics about storages, grouped by types
[**statistics_task_by_status**](StatisticsApi.md#statistics_task_by_status) | **GET** /statistics/task_by_status | Get statistics about tasks executions, grouped by status
[**statistics_task_by_storage**](StatisticsApi.md#statistics_task_by_storage) | **GET** /statistics/task_by_storage | Get statistics about tasks executions, grouped by source and destination
[**statistics_task_by_workflow**](StatisticsApi.md#statistics_task_by_workflow) | **GET** /statistics/task_by_workflow | Get statistics about tasks executions, grouped by workflow


# **statistics_by_date**
> ByDateFacet statistics_by_date(q=q, fq=fq, date_attr=date_attr)

Get statistics about files, grouped by date

**API Key Scope**: statistics / by_date

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # Get statistics about files, grouped by date
        api_response = api_instance.statistics_by_date(q=q, fq=fq, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_date: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # Get statistics about files, grouped by date
        api_response = api_instance.statistics_by_date(q=q, fq=fq, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 

### Return type

[**ByDateFacet**](ByDateFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_file_extension**
> ByFileExtensionFacet statistics_by_file_extension(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by file extension

**API Key Scope**: statistics / by_file_extension

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by file extension
        api_response = api_instance.statistics_by_file_extension(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_file_extension: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by file extension
        api_response = api_instance.statistics_by_file_extension(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_file_extension: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**ByFileExtensionFacet**](ByFileExtensionFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_group_owner**
> ByGroupOwnerFacet statistics_by_group_owner(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by owner (group)

**API Key Scope**: statistics / by_group_owner

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by owner (group)
        api_response = api_instance.statistics_by_group_owner(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_group_owner: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by owner (group)
        api_response = api_instance.statistics_by_group_owner(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_group_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**ByGroupOwnerFacet**](ByGroupOwnerFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_primary_cloud**
> ByPrimaryCloudFacet statistics_by_primary_cloud(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by primary Cloud

**API Key Scope**: statistics / by_primary_cloud

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by primary Cloud
        api_response = api_instance.statistics_by_primary_cloud(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_primary_cloud: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by primary Cloud
        api_response = api_instance.statistics_by_primary_cloud(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_primary_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**ByPrimaryCloudFacet**](ByPrimaryCloudFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_primary_name**
> ByPrimaryFacet statistics_by_primary_name(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by primary storages

**API Key Scope**: statistics / by_primary_name

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by primary storages
        api_response = api_instance.statistics_by_primary_name(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_primary_name: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by primary storages
        api_response = api_instance.statistics_by_primary_name(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_primary_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**ByPrimaryFacet**](ByPrimaryFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_primary_nas**
> ByPrimaryNasFacet statistics_by_primary_nas(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by primary NAS

**API Key Scope**: statistics / by_primary_nas

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by primary NAS
        api_response = api_instance.statistics_by_primary_nas(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_primary_nas: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by primary NAS
        api_response = api_instance.statistics_by_primary_nas(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_primary_nas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**ByPrimaryNasFacet**](ByPrimaryNasFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_primary_storage**
> ByPrimaryStorageFacet statistics_by_primary_storage(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by primary storage

**API Key Scope**: statistics / by_primary_storage

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by primary storage
        api_response = api_instance.statistics_by_primary_storage(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_primary_storage: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by primary storage
        api_response = api_instance.statistics_by_primary_storage(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_primary_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**ByPrimaryStorageFacet**](ByPrimaryStorageFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_secondary_cloud**
> BySecondaryCloudFacet statistics_by_secondary_cloud(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by secondary Cloud

**API Key Scope**: statistics / by_secondary_cloud

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by secondary Cloud
        api_response = api_instance.statistics_by_secondary_cloud(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_secondary_cloud: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by secondary Cloud
        api_response = api_instance.statistics_by_secondary_cloud(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_secondary_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**BySecondaryCloudFacet**](BySecondaryCloudFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_secondary_nas**
> BySecondaryNasFacet statistics_by_secondary_nas(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by secondary NAS

**API Key Scope**: statistics / by_secondary_nas

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by secondary NAS
        api_response = api_instance.statistics_by_secondary_nas(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_secondary_nas: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by secondary NAS
        api_response = api_instance.statistics_by_secondary_nas(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_secondary_nas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**BySecondaryNasFacet**](BySecondaryNasFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_secondary_storage**
> BySecondaryStorageFacet statistics_by_secondary_storage(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by secondary storage

**API Key Scope**: statistics / by_secondary_storage

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by secondary storage
        api_response = api_instance.statistics_by_secondary_storage(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_secondary_storage: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by secondary storage
        api_response = api_instance.statistics_by_secondary_storage(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_secondary_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**BySecondaryStorageFacet**](BySecondaryStorageFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_secondary_tape**
> BySecondaryTapeFacet statistics_by_secondary_tape(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by secondary Tape

**API Key Scope**: statistics / by_secondary_tape

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by secondary Tape
        api_response = api_instance.statistics_by_secondary_tape(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_secondary_tape: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by secondary Tape
        api_response = api_instance.statistics_by_secondary_tape(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_secondary_tape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**BySecondaryTapeFacet**](BySecondaryTapeFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_size**
> BySizeFacet statistics_by_size(q=q, fq=fq, date_attr=date_attr)

Get statistics about files, grouped by size

**API Key Scope**: statistics / by_size

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # Get statistics about files, grouped by size
        api_response = api_instance.statistics_by_size(q=q, fq=fq, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_size: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # Get statistics about files, grouped by size
        api_response = api_instance.statistics_by_size(q=q, fq=fq, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 

### Return type

[**BySizeFacet**](BySizeFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_by_user_owner**
> ByUserOwnerFacet statistics_by_user_owner(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)

Get statistics about files, grouped by owner (user)

**API Key Scope**: statistics / by_user_owner

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by owner (user)
        api_response = api_instance.statistics_by_user_owner(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_user_owner: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)
sort = 'count' # str | Sort results of facet (optional) (default to 'count')
limit = 10 # int | Limit results of facet (optional) (default to 10)

    try:
        # Get statistics about files, grouped by owner (user)
        api_response = api_instance.statistics_by_user_owner(q=q, fq=fq, date_attr=date_attr, sort=sort, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_user_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 
 **sort** | **str**| Sort results of facet | [optional] [default to &#39;count&#39;]
 **limit** | **int**| Limit results of facet | [optional] [default to 10]

### Return type

[**ByUserOwnerFacet**](ByUserOwnerFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_storage**
> StorageFacet statistics_storage(q=q, fq=fq)

Get statistics about storages, grouped by types

**API Key Scope**: statistics / storages

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)

    try:
        # Get statistics about storages, grouped by types
        api_response = api_instance.statistics_storage(q=q, fq=fq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_storage: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)

    try:
        # Get statistics about storages, grouped by types
        api_response = api_instance.statistics_storage(q=q, fq=fq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 

### Return type

[**StorageFacet**](StorageFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_task_by_status**
> ByTaskStatusFacet statistics_task_by_status(q=q, fq=fq)

Get statistics about tasks executions, grouped by status

**API Key Scope**: statistics / task_by_status

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)

    try:
        # Get statistics about tasks executions, grouped by status
        api_response = api_instance.statistics_task_by_status(q=q, fq=fq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_task_by_status: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)

    try:
        # Get statistics about tasks executions, grouped by status
        api_response = api_instance.statistics_task_by_status(q=q, fq=fq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_task_by_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 

### Return type

[**ByTaskStatusFacet**](ByTaskStatusFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_task_by_storage**
> ByTaskStorageFacet statistics_task_by_storage(q=q, fq=fq)

Get statistics about tasks executions, grouped by source and destination

**API Key Scope**: statistics / task_by_storage

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)

    try:
        # Get statistics about tasks executions, grouped by source and destination
        api_response = api_instance.statistics_task_by_storage(q=q, fq=fq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_task_by_storage: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)

    try:
        # Get statistics about tasks executions, grouped by source and destination
        api_response = api_instance.statistics_task_by_storage(q=q, fq=fq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_task_by_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 

### Return type

[**ByTaskStorageFacet**](ByTaskStorageFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_task_by_workflow**
> ByTaskWorkflowFacet statistics_task_by_workflow(q=q, fq=fq)

Get statistics about tasks executions, grouped by workflow

**API Key Scope**: statistics / task_by_workflow

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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)

    try:
        # Get statistics about tasks executions, grouped by workflow
        api_response = api_instance.statistics_task_by_workflow(q=q, fq=fq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_task_by_workflow: %s\n" % e)
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
    api_instance = nodeum_sdk.StatisticsApi(api_client)
    q = 'q_example' # str | Solr query (optional)
fq = ['fq_example'] # list[str] | Solr filter query  Multiple query can be separated by `|`. (optional)

    try:
        # Get statistics about tasks executions, grouped by workflow
        api_response = api_instance.statistics_task_by_workflow(q=q, fq=fq)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_task_by_workflow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **fq** | [**list[str]**](str.md)| Solr filter query  Multiple query can be separated by &#x60;|&#x60;. | [optional] 

### Return type

[**ByTaskWorkflowFacet**](ByTaskWorkflowFacet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

