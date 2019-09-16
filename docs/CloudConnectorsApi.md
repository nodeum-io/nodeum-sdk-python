# swagger_client.CloudConnectorsApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_connector**](CloudConnectorsApi.md#create_cloud_connector) | **POST** /cloud_connectors | Creates a new cloud connector.
[**destroy_cloud_connector**](CloudConnectorsApi.md#destroy_cloud_connector) | **DELETE** /cloud_connectors/{cloud_connector_id} | Destroys a specific cloud connector.
[**index_cloud_connectors**](CloudConnectorsApi.md#index_cloud_connectors) | **GET** /cloud_connectors | Lists all cloud connectors.
[**show_cloud_connector**](CloudConnectorsApi.md#show_cloud_connector) | **GET** /cloud_connectors/{cloud_connector_id} | Displays a specific cloud connector.
[**test_cloud_connector**](CloudConnectorsApi.md#test_cloud_connector) | **PUT** /cloud_connectors/-/test | Test an unsaved cloud connector.
[**test_result_cloud_connector**](CloudConnectorsApi.md#test_result_cloud_connector) | **GET** /cloud_connectors/-/test | Check result of cloud connector test job.
[**update_cloud_connector**](CloudConnectorsApi.md#update_cloud_connector) | **PUT** /cloud_connectors/{cloud_connector_id} | Updates a specific cloud connector.


# **create_cloud_connector**
> CloudConnector create_cloud_connector(cloud_connector_body)

Creates a new cloud connector.

**API Key Scope**: cloud_connectors / create

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
api_instance = swagger_client.CloudConnectorsApi(swagger_client.ApiClient(configuration))
cloud_connector_body = swagger_client.CloudConnector() # CloudConnector | 

try:
    # Creates a new cloud connector.
    api_response = api_instance.create_cloud_connector(cloud_connector_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudConnectorsApi->create_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_body** | [**CloudConnector**](CloudConnector.md)|  | 

### Return type

[**CloudConnector**](CloudConnector.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_cloud_connector**
> destroy_cloud_connector(cloud_connector_id)

Destroys a specific cloud connector.

**API Key Scope**: cloud_connectors / destroy

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
api_instance = swagger_client.CloudConnectorsApi(swagger_client.ApiClient(configuration))
cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.

try:
    # Destroys a specific cloud connector.
    api_instance.destroy_cloud_connector(cloud_connector_id)
except ApiException as e:
    print("Exception when calling CloudConnectorsApi->destroy_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_cloud_connectors**
> CloudConnectorCollection index_cloud_connectors(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, url=url, url_proxy=url_proxy, provider=provider, region=region, access_key=access_key)

Lists all cloud connectors.

**API Key Scope**: cloud_connectors / index   Optional API Key Explicit Scope: cloud_connectors / get_secret_key

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
api_instance = swagger_client.CloudConnectorsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of items to display for pagination. (optional)
offset = 56 # int | The number of items to skip for pagination. (optional)
sort_by = ['sort_by_example'] # list[str] | Sort results by attribute.  Can sort on multiple attributes, separated by `|`. Order direction can be suffixing the attribute by either `:asc` (default) or `:desc`. (optional)
id = 'id_example' # str | Filter on id (optional)
name = 'name_example' # str | Filter on name (optional)
url = 'url_example' # str | Filter on url (optional)
url_proxy = 'url_proxy_example' # str | Filter on url proxy (optional)
provider = 'provider_example' # str | Filter on provider (optional)
region = 'region_example' # str | Filter on region (optional)
access_key = 'access_key_example' # str | Filter on access key (optional)

try:
    # Lists all cloud connectors.
    api_response = api_instance.index_cloud_connectors(limit=limit, offset=offset, sort_by=sort_by, id=id, name=name, url=url, url_proxy=url_proxy, provider=provider, region=region, access_key=access_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudConnectorsApi->index_cloud_connectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of items to display for pagination. | [optional] 
 **offset** | **int**| The number of items to skip for pagination. | [optional] 
 **sort_by** | [**list[str]**](str.md)| Sort results by attribute.  Can sort on multiple attributes, separated by &#x60;|&#x60;. Order direction can be suffixing the attribute by either &#x60;:asc&#x60; (default) or &#x60;:desc&#x60;. | [optional] 
 **id** | **str**| Filter on id | [optional] 
 **name** | **str**| Filter on name | [optional] 
 **url** | **str**| Filter on url | [optional] 
 **url_proxy** | **str**| Filter on url proxy | [optional] 
 **provider** | **str**| Filter on provider | [optional] 
 **region** | **str**| Filter on region | [optional] 
 **access_key** | **str**| Filter on access key | [optional] 

### Return type

[**CloudConnectorCollection**](CloudConnectorCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_cloud_connector**
> CloudConnector show_cloud_connector(cloud_connector_id)

Displays a specific cloud connector.

**API Key Scope**: cloud_connectors / show   Optional API Key Explicit Scope: cloud_connectors / get_secret_key

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
api_instance = swagger_client.CloudConnectorsApi(swagger_client.ApiClient(configuration))
cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.

try:
    # Displays a specific cloud connector.
    api_response = api_instance.show_cloud_connector(cloud_connector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudConnectorsApi->show_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 

### Return type

[**CloudConnector**](CloudConnector.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_cloud_connector**
> ActiveJobStatus test_cloud_connector(cloud_connector_body)

Test an unsaved cloud connector.

**API Key Scope**: cloud_connectors / test

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
api_instance = swagger_client.CloudConnectorsApi(swagger_client.ApiClient(configuration))
cloud_connector_body = swagger_client.CloudConnector() # CloudConnector | 

try:
    # Test an unsaved cloud connector.
    api_response = api_instance.test_cloud_connector(cloud_connector_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudConnectorsApi->test_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_body** | [**CloudConnector**](CloudConnector.md)|  | 

### Return type

[**ActiveJobStatus**](ActiveJobStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_result_cloud_connector**
> CloudBucketSimpleCollection test_result_cloud_connector(job_id=job_id)

Check result of cloud connector test job.

**API Key Scope**: cloud_connectors / test

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
api_instance = swagger_client.CloudConnectorsApi(swagger_client.ApiClient(configuration))
job_id = 'job_id_example' # str | ID of active job (optional)

try:
    # Check result of cloud connector test job.
    api_response = api_instance.test_result_cloud_connector(job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudConnectorsApi->test_result_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| ID of active job | [optional] 

### Return type

[**CloudBucketSimpleCollection**](CloudBucketSimpleCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_connector**
> CloudConnector update_cloud_connector(cloud_connector_id, cloud_connector_body)

Updates a specific cloud connector.

**API Key Scope**: cloud_connectors / update

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
api_instance = swagger_client.CloudConnectorsApi(swagger_client.ApiClient(configuration))
cloud_connector_id = 'cloud_connector_id_example' # str | Numeric ID or name of cloud connector.
cloud_connector_body = swagger_client.CloudConnector() # CloudConnector | 

try:
    # Updates a specific cloud connector.
    api_response = api_instance.update_cloud_connector(cloud_connector_id, cloud_connector_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudConnectorsApi->update_cloud_connector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_connector_id** | **str**| Numeric ID or name of cloud connector. | 
 **cloud_connector_body** | [**CloudConnector**](CloudConnector.md)|  | 

### Return type

[**CloudConnector**](CloudConnector.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

