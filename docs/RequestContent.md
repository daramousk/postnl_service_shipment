# RequestContent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of goods | [default to 'Powdered milk']
**ean** | **str** | A unique code for a product. Together with HS number this is mandatory for product code 4992. | [optional] 
**product_url** | **str** | Webshop URL of the product which is being shipped. Mandatory for product code 4992 | [optional] 
**quantity** | **str** | Quantity of items in description | [default to '2']
**weight** | **str** | Net weight of goods in gram(gr) | [default to '2600']
**value** | **str** | Commercial (customs) value of goods. | [default to '20.00']
**hs_tariff_nr** | **str** | First 6 numbers of Harmonized System Code | [optional] [default to '100878']
**country_of_origin** | **str** | Origin country code | [optional] [default to 'NL']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

