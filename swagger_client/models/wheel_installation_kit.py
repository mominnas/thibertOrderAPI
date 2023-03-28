# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class WheelInstallationKit(object):
    """ 

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
        'thibert_part_number': 'str',
        'part': 'Part'
    }

    attribute_map = {
        'thibert_part_number': 'thibertPartNumber',
        'part': 'part'
    }

    def __init__(self, thibert_part_number=None, part=None):  # noqa: E501
        """WheelInstallationKit - a model defined in Swagger"""  # noqa: E501
        self._thibert_part_number = None
        self._part = None
        self.discriminator = None
        if thibert_part_number is not None:
            self.thibert_part_number = thibert_part_number
        if part is not None:
            self.part = part

    @property
    def thibert_part_number(self):
        """Gets the thibert_part_number of this WheelInstallationKit.  # noqa: E501

        Thibert part number associated with this part.  # noqa: E501

        :return: The thibert_part_number of this WheelInstallationKit.  # noqa: E501
        :rtype: str
        """
        return self._thibert_part_number

    @thibert_part_number.setter
    def thibert_part_number(self, thibert_part_number):
        """Sets the thibert_part_number of this WheelInstallationKit.

        Thibert part number associated with this part.  # noqa: E501

        :param thibert_part_number: The thibert_part_number of this WheelInstallationKit.  # noqa: E501
        :type: str
        """

        self._thibert_part_number = thibert_part_number

    @property
    def part(self):
        """Gets the part of this WheelInstallationKit.  # noqa: E501


        :return: The part of this WheelInstallationKit.  # noqa: E501
        :rtype: Part
        """
        return self._part

    @part.setter
    def part(self, part):
        """Sets the part of this WheelInstallationKit.


        :param part: The part of this WheelInstallationKit.  # noqa: E501
        :type: Part
        """

        self._part = part

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
        if issubclass(WheelInstallationKit, dict):
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
        if not isinstance(other, WheelInstallationKit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
