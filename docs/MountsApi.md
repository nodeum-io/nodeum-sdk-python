# swagger_client.MountsApi

All URIs are relative to *https://localhost/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**index_mounts**](MountsApi.md#index_mounts) | **GET** /mounts | List all mounted storages


# **index_mounts**
> MountCollection index_mounts()

List all mounted storages

**API Key Scope**: mounts / index

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
api_instance = swagger_client.MountsApi(swagger_client.ApiClient(configuration))

try:
    # List all mounted storages
    api_response = api_instance.index_mounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MountsApi->index_mounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MountCollection**](MountCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

