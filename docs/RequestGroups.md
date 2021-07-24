# RequestGroups

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_type** | **str** | Group sort that determines the type of group that is indicated. This is a code. Possible values: 01 &#x3D; Collection request 03 &#x3D; Multiple parcels in one shipment (multicolli) 04 &#x3D; Single parcel in one shipment | [default to '04']
**group_sequence** | **str** | Sequence number of the collo within the complete shipment (e.g. collo 2 of 4) Mandatory for multicollo shipments | [default to '1']
**group_count** | **str** | Total number of colli in the shipment (in case of multicolli shipments) Mandatory for multicollo shipments | [default to '1']
**main_barcode** | **str** | Main barcode for the shipment (in case of multicolli shipments) Mandatory for multicollo shipments | [default to '3SABCD7239264']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

