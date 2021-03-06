# postnl-service-shipment
Generates a Base64 label

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2_2
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import postnl_service_shipment 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import postnl_service_shipment
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import postnl_service_shipment
from postnl_service_shipment.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = postnl_service_shipment.DefaultApi(postnl_service_shipment.ApiClient(configuration))
body = postnl_service_shipment.Request() # Request | 
apikey = 'apikey_example' # str | Authenticate using your API key
confirm = true # bool | true or false; whether or not to confirm the shipments. Default value true. (optional) (default to true)

try:
    api_response = api_instance.shipment_v22_label_post(body, apikey, confirm=confirm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->shipment_v22_label_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api-sandbox.postnl.nl*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**shipment_v22_label_post**](docs/DefaultApi.md#shipment_v22_label_post) | **POST** /shipment/v2_2/label | 

## Documentation For Models

 - [Error](docs/Error.md)
 - [ErrorErrors](docs/ErrorErrors.md)
 - [Request](docs/Request.md)
 - [RequestAddresses](docs/RequestAddresses.md)
 - [RequestAmounts](docs/RequestAmounts.md)
 - [RequestContacts](docs/RequestContacts.md)
 - [RequestContent](docs/RequestContent.md)
 - [RequestCustomer](docs/RequestCustomer.md)
 - [RequestCustomerAddress](docs/RequestCustomerAddress.md)
 - [RequestCustoms](docs/RequestCustoms.md)
 - [RequestDimension](docs/RequestDimension.md)
 - [RequestExtraFields](docs/RequestExtraFields.md)
 - [RequestGroups](docs/RequestGroups.md)
 - [RequestHazardousMaterial](docs/RequestHazardousMaterial.md)
 - [RequestMessage](docs/RequestMessage.md)
 - [RequestProductOptions](docs/RequestProductOptions.md)
 - [RequestShipments](docs/RequestShipments.md)
 - [Response](docs/Response.md)
 - [ResponseLabels](docs/ResponseLabels.md)
 - [ResponseMergedLabels](docs/ResponseMergedLabels.md)
 - [ResponseResponseShipments](docs/ResponseResponseShipments.md)
 - [ResponseWarnings](docs/ResponseWarnings.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author


