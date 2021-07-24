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

class ErrorErrors(object):
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
        'error': 'str',
        'code': 'str',
        'description': 'str'
    }

    attribute_map = {
        'error': 'Error',
        'code': 'Code',
        'description': 'Description'
    }

    def __init__(self, error=None, code=None, description=None):  # noqa: E501
        """ErrorErrors - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._code = None
        self._description = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if code is not None:
            self.code = code
        if description is not None:
            self.description = description

    @property
    def error(self):
        """Gets the error of this ErrorErrors.  # noqa: E501


        :return: The error of this ErrorErrors.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ErrorErrors.


        :param error: The error of this ErrorErrors.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def code(self):
        """Gets the code of this ErrorErrors.  # noqa: E501


        :return: The code of this ErrorErrors.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorErrors.


        :param code: The code of this ErrorErrors.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this ErrorErrors.  # noqa: E501


        :return: The description of this ErrorErrors.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ErrorErrors.


        :param description: The description of this ErrorErrors.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(ErrorErrors, dict):
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
        if not isinstance(other, ErrorErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
