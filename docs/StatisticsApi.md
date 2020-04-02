# nodeum_sdk.StatisticsApi

All URIs are relative to *http://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_by_file_extension**](StatisticsApi.md#statistics_by_file_extension) | **GET** /statistics/by_file_extension | TODO
[**statistics_by_group_owner**](StatisticsApi.md#statistics_by_group_owner) | **GET** /statistics/by_group_owner | TODO
[**statistics_by_primary_name**](StatisticsApi.md#statistics_by_primary_name) | **GET** /statistics/by_primary_name | TODO
[**statistics_by_secondary_storage**](StatisticsApi.md#statistics_by_secondary_storage) | **GET** /statistics/by_secondary_storage | TODO
[**statistics_by_size**](StatisticsApi.md#statistics_by_size) | **GET** /statistics/by_size | TODO
[**statistics_by_user_owner**](StatisticsApi.md#statistics_by_user_owner) | **GET** /statistics/by_user_owner | TODO


# **statistics_by_file_extension**
> ByFileExtensionFacet statistics_by_file_extension(q=q, date_attr=date_attr)

TODO

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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_file_extension(q=q, date_attr=date_attr)
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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_file_extension(q=q, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_file_extension: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 

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
> ByGroupOwnerFacet statistics_by_group_owner(q=q, date_attr=date_attr)

TODO

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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_group_owner(q=q, date_attr=date_attr)
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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_group_owner(q=q, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_group_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 

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

# **statistics_by_primary_name**
> ByPrimaryFacet statistics_by_primary_name(q=q, date_attr=date_attr)

TODO

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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_primary_name(q=q, date_attr=date_attr)
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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_primary_name(q=q, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_primary_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 

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

# **statistics_by_secondary_storage**
> BySecondaryFacet statistics_by_secondary_storage(q=q, date_attr=date_attr)

TODO

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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_secondary_storage(q=q, date_attr=date_attr)
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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_secondary_storage(q=q, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_secondary_storage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 

### Return type

[**BySecondaryFacet**](BySecondaryFacet.md)

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
> BySizeFacet statistics_by_size(q=q, date_attr=date_attr)

TODO

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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_size(q=q, date_attr=date_attr)
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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_size(q=q, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
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
> ByUserOwnerFacet statistics_by_user_owner(q=q, date_attr=date_attr)

TODO

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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_user_owner(q=q, date_attr=date_attr)
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
date_attr = 'date_attr_example' # str | Type of date to facet on (optional)

    try:
        # TODO
        api_response = api_instance.statistics_by_user_owner(q=q, date_attr=date_attr)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatisticsApi->statistics_by_user_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Solr query | [optional] 
 **date_attr** | **str**| Type of date to facet on | [optional] 

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

