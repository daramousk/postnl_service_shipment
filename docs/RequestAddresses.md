# RequestAddresses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_type** | **str** | Type of the address. This is a code. You can find the possible values at Guidelines | [default to '02']
**area** | **str** | Area of the address | [optional] 
**buildingname** | **str** | Building name of the address | [optional] 
**city** | **str** | City of the address | [optional] [default to 'Hoofddorp']
**company_name** | **str** | This field has a dependency with the field Name. One of both fields must be filled mandatory; using both fields is also allowed. Mandatory when AddressType is 09. | [optional] [default to 'PostNL']
**countrycode** | **str** | The ISO2 country codes | [default to 'NL']
**department** | **str** | Send to specific department of a company.  | [optional] 
**doorcode** | **str** | Door code of address. Mandatory for some international shipments. | [optional] 
**first_name** | **str** | Remark: please add FirstName and Name (lastname) of the receiver to improve the parcel tracking experience of your customer.  | [optional] [default to 'Peter']
**floor** | **str** | Send to specific floor of a company | [optional] 
**house_nr** | **str** | Mandatory for shipments to Benelux. Max. length is 5 characters (only for Benelux addresses). For Benelux addresses,this field should always be numeric. | [optional] [default to '42']
**house_nr_ext** | **str** | House number extension  | [optional] 
**name** | **str** | Last name of person. This field has a dependency with the field CompanyName. One of both fields must be filled mandatory; using both fields is also allowed. Remark: please add FirstName and Name (lastname) of the receiver to improve the parcel tracking experience of your customer.  | [optional] [default to 'de Ruiter']
**region** | **str** | Region of the address | [optional] 
**street** | **str** | This field has a dependency with the field StreetHouseNrExt. One of both fields must be filled mandatory; using both fields is also allowed.  | [optional] [default to 'Siriusdreef']
**street_house_nr_ext** | **str** | Combination of Street, HouseNr and HouseNrExt. Please see Guidelines for the explanation. | [optional] 
**zipcode** | **str** | Zipcode of the address. Mandatory for shipments to Benelux. Max length (NL) 6 characters,(BE;LU) 4 numeric characters | [optional] [default to '2132WT']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

