# postnl_service_shipment.DefaultApi

All URIs are relative to *https://api-sandbox.postnl.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipment_v22_label_post**](DefaultApi.md#shipment_v22_label_post) | **POST** /shipment/v2_2/label | 

# **shipment_v22_label_post**
> Response shipment_v22_label_post(body, apikey, confirm=confirm)



### Example
```python
from __future__ import print_function
import time
import postnl_service_shipment
from postnl_service_shipment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postnl_service_shipment.DefaultApi()
body = postnl_service_shipment.Request() # Request | 
apikey = 'apikey_example' # str | Authenticate using your API key
confirm = true # bool | true or false; whether or not to confirm the shipments. Default value true. (optional) (default to true)

try:
    api_response = api_instance.shipment_v22_label_post(body, apikey, confirm=confirm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->shipment_v22_label_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Request**](Request.md)|  | 
 **apikey** | **str**| Authenticate using your API key | 
 **confirm** | **bool**| true or false; whether or not to confirm the shipments. Default value true. | [optional] [default to true]

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

