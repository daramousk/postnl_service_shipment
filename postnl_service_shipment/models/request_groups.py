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

class RequestGroups(object):
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
        'group_type': 'str',
        'group_sequence': 'str',
        'group_count': 'str',
        'main_barcode': 'str'
    }

    attribute_map = {
        'group_type': 'GroupType',
        'group_sequence': 'GroupSequence',
        'group_count': 'GroupCount',
        'main_barcode': 'MainBarcode'
    }

    def __init__(self, group_type='04', group_sequence='1', group_count='1', main_barcode='3SABCD7239264'):  # noqa: E501
        """RequestGroups - a model defined in Swagger"""  # noqa: E501
        self._group_type = None
        self._group_sequence = None
        self._group_count = None
        self._main_barcode = None
        self.discriminator = None
        self.group_type = group_type
        self.group_sequence = group_sequence
        self.group_count = group_count
        self.main_barcode = main_barcode

    @property
    def group_type(self):
        """Gets the group_type of this RequestGroups.  # noqa: E501

        Group sort that determines the type of group that is indicated. This is a code. Possible values: 01 = Collection request 03 = Multiple parcels in one shipment (multicolli) 04 = Single parcel in one shipment  # noqa: E501

        :return: The group_type of this RequestGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this RequestGroups.

        Group sort that determines the type of group that is indicated. This is a code. Possible values: 01 = Collection request 03 = Multiple parcels in one shipment (multicolli) 04 = Single parcel in one shipment  # noqa: E501

        :param group_type: The group_type of this RequestGroups.  # noqa: E501
        :type: str
        """
        if group_type is None:
            raise ValueError("Invalid value for `group_type`, must not be `None`")  # noqa: E501

        self._group_type = group_type

    @property
    def group_sequence(self):
        """Gets the group_sequence of this RequestGroups.  # noqa: E501

        Sequence number of the collo within the complete shipment (e.g. collo 2 of 4) Mandatory for multicollo shipments  # noqa: E501

        :return: The group_sequence of this RequestGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_sequence

    @group_sequence.setter
    def group_sequence(self, group_sequence):
        """Sets the group_sequence of this RequestGroups.

        Sequence number of the collo within the complete shipment (e.g. collo 2 of 4) Mandatory for multicollo shipments  # noqa: E501

        :param group_sequence: The group_sequence of this RequestGroups.  # noqa: E501
        :type: str
        """
        if group_sequence is None:
            raise ValueError("Invalid value for `group_sequence`, must not be `None`")  # noqa: E501

        self._group_sequence = group_sequence

    @property
    def group_count(self):
        """Gets the group_count of this RequestGroups.  # noqa: E501

        Total number of colli in the shipment (in case of multicolli shipments) Mandatory for multicollo shipments  # noqa: E501

        :return: The group_count of this RequestGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        """Sets the group_count of this RequestGroups.

        Total number of colli in the shipment (in case of multicolli shipments) Mandatory for multicollo shipments  # noqa: E501

        :param group_count: The group_count of this RequestGroups.  # noqa: E501
        :type: str
        """
        if group_count is None:
            raise ValueError("Invalid value for `group_count`, must not be `None`")  # noqa: E501

        self._group_count = group_count

    @property
    def main_barcode(self):
        """Gets the main_barcode of this RequestGroups.  # noqa: E501

        Main barcode for the shipment (in case of multicolli shipments) Mandatory for multicollo shipments  # noqa: E501

        :return: The main_barcode of this RequestGroups.  # noqa: E501
        :rtype: str
        """
        return self._main_barcode

    @main_barcode.setter
    def main_barcode(self, main_barcode):
        """Sets the main_barcode of this RequestGroups.

        Main barcode for the shipment (in case of multicolli shipments) Mandatory for multicollo shipments  # noqa: E501

        :param main_barcode: The main_barcode of this RequestGroups.  # noqa: E501
        :type: str
        """
        if main_barcode is None:
            raise ValueError("Invalid value for `main_barcode`, must not be `None`")  # noqa: E501

        self._main_barcode = main_barcode

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
        if issubclass(RequestGroups, dict):
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
        if not isinstance(other, RequestGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
