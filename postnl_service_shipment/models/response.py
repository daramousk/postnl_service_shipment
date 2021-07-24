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

class Response(object):
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
        'merged_labels': 'list[ResponseMergedLabels]',
        'response_shipments': 'list[ResponseResponseShipments]'
    }

    attribute_map = {
        'merged_labels': 'MergedLabels',
        'response_shipments': 'ResponseShipments'
    }

    def __init__(self, merged_labels=None, response_shipments=None):  # noqa: E501
        """Response - a model defined in Swagger"""  # noqa: E501
        self._merged_labels = None
        self._response_shipments = None
        self.discriminator = None
        if merged_labels is not None:
            self.merged_labels = merged_labels
        if response_shipments is not None:
            self.response_shipments = response_shipments

    @property
    def merged_labels(self):
        """Gets the merged_labels of this Response.  # noqa: E501


        :return: The merged_labels of this Response.  # noqa: E501
        :rtype: list[ResponseMergedLabels]
        """
        return self._merged_labels

    @merged_labels.setter
    def merged_labels(self, merged_labels):
        """Sets the merged_labels of this Response.


        :param merged_labels: The merged_labels of this Response.  # noqa: E501
        :type: list[ResponseMergedLabels]
        """

        self._merged_labels = merged_labels

    @property
    def response_shipments(self):
        """Gets the response_shipments of this Response.  # noqa: E501


        :return: The response_shipments of this Response.  # noqa: E501
        :rtype: list[ResponseResponseShipments]
        """
        return self._response_shipments

    @response_shipments.setter
    def response_shipments(self, response_shipments):
        """Sets the response_shipments of this Response.


        :param response_shipments: The response_shipments of this Response.  # noqa: E501
        :type: list[ResponseResponseShipments]
        """

        self._response_shipments = response_shipments

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
        if issubclass(Response, dict):
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
        if not isinstance(other, Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other