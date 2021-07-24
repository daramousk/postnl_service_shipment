# RequestCustoms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **bool** | At least one of the three types Certificate, Invoice or License is mandatory for Commercial Goods,Commercial Sample and Returned Goods | [optional] 
**certificate_nr** | **str** | Mandatory when Certificate is true.  | [optional] 
**license** | **bool** | At least one of the three types Certificate, Invoice or License is mandatory for Commercial Goods,Commercial Sample and Returned Goods | [optional] 
**license_nr** | **str** | Mandatory when License is true. | [optional] 
**invoice** | **bool** | At least one of the three types Certificate, Invoice or License is mandatory for Commercial Goods,Commercial Sample and Returned Goods | [optional] 
**invoice_nr** | **str** | Mandatory when Invoice is true | [optional] [default to 'INV_0120330']
**handle_as_non_deliverable** | **bool** | Determines what to do when the shipment cannot be delivered the first time (if this is set to true,the shipment will be returned after the first failed attempt) | [optional] 
**currency** | **str** | Currency code,only EUR and USS are allowed | [default to 'EUR']
**shipment_type** | **str** | Type of shipment,possible values: Gift,Documents,Commercial Goods,Commercial Sample,Returned Goods | [optional] [default to 'Commercial Goods']
**trusted_shipper_id** | **str** | Trusted shipper ID; Mandatory for US shipments | [optional] 
**importer_reference_code** | **str** | Importer reference code; Mandatory for US shipments | [optional] 
**transaction_code** | **str** | Transaction code; Mandatory for US shipments | [optional] 
**transaction_description** | **str** | Transaction description; Mandatory for US shipments | [optional] 
**content** | [**list[RequestContent]**](RequestContent.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

