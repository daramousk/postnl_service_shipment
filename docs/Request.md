# Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**RequestCustomer**](RequestCustomer.md) |  | 
**label_signature** | **str** | GIF image of the signature (as a base64 encoded string). The value of this element can have a maximum size of 65536 characters. Note that the total request can have a maximum size of 200KB. Larger requests will not be accepted by the server for performance reasons. Requests that exceed this limit will not return a validation error,but a HTTP 404 error. | [optional] 
**message** | [**RequestMessage**](RequestMessage.md) |  | 
**shipments** | [**list[RequestShipments]**](RequestShipments.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

