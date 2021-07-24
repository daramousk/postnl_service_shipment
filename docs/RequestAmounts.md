# RequestAmounts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_type** | **str** | Amount type. This is a code. Possible values are: 01 &#x3D; Cash on delivery (COD) 02 &#x3D; Insured value 04 mandatory for Commercial route China. 12 mandatory for Inco terms DDP Commercial route China. | [default to '01']
**account_name** | **str** | Name of bank account owner  | [optional] 
**bic** | **str** | BIC number,optional for COD shipments (mandatory for bank account number other than originating in The Netherlands) | [optional] 
**currency** | **str** | Currency code according ISO 4217. E.g. EUR | [optional] [default to 'EUR']
**iban** | **str** | IBAN bank account number,mandatory for COD shipments. Dutch IBAN numbers are 18 characters  | [optional] 
**reference** | **str** | Personal payment reference  | [optional] 
**transaction_number** | **str** | Transaction number | [optional] 
**value** | **str** | Money value in EUR (unless value Currency is specified for another currency). Value format (N6.2): #####0.00 (2 digits behind decimal dot) Mandatory for COD and Insured products | [default to '100.00']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

