# coding: utf-8

"""
    Labelling

    Generates a Base64 label  # noqa: E501

    OpenAPI spec version: v2_2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RequestProductOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'characteristic': 'str',
        'option': 'str'
    }

    attribute_map = {
        'characteristic': 'Characteristic',
        'option': 'Option'
    }

    def __init__(self, characteristic='118', option='006'):  # noqa: E501
        """RequestProductOptions - a model defined in Swagger"""  # noqa: E501
        self._characteristic = None
        self._option = None
        self.discriminator = None
        self.characteristic = characteristic
        self.option = option

    @property
    def characteristic(self):
        """Gets the characteristic of this RequestProductOptions.  # noqa: E501

        The characteristic of the ProductOption. Mandatory for some products, please see the Products page  # noqa: E501

        :return: The characteristic of this RequestProductOptions.  # noqa: E501
        :rtype: str
        """
        return self._characteristic

    @characteristic.setter
    def characteristic(self, characteristic):
        """Sets the characteristic of this RequestProductOptions.

        The characteristic of the ProductOption. Mandatory for some products, please see the Products page  # noqa: E501

        :param characteristic: The characteristic of this RequestProductOptions.  # noqa: E501
        :type: str
        """
        if characteristic is None:
            raise ValueError("Invalid value for `characteristic`, must not be `None`")  # noqa: E501

        self._characteristic = characteristic

    @property
    def option(self):
        """Gets the option of this RequestProductOptions.  # noqa: E501

        The product option code for this ProductOption. Mandatory for some products, please see the Products page  # noqa: E501

        :return: The option of this RequestProductOptions.  # noqa: E501
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this RequestProductOptions.

        The product option code for this ProductOption. Mandatory for some products, please see the Products page  # noqa: E501

        :param option: The option of this RequestProductOptions.  # noqa: E501
        :type: str
        """
        if option is None:
            raise ValueError("Invalid value for `option`, must not be `None`")  # noqa: E501

        self._option = option

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RequestProductOptions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestProductOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
