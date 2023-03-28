# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class WheelPartType(object):
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
        'wheel_part_type_id': 'str',
        'wheel_part_types': 'list[LocalizedString]'
    }

    attribute_map = {
        'wheel_part_type_id': 'wheelPartTypeID',
        'wheel_part_types': 'wheelPartTypes'
    }

    def __init__(self, wheel_part_type_id=None, wheel_part_types=None):  # noqa: E501
        """WheelPartType - a model defined in Swagger"""  # noqa: E501
        self._wheel_part_type_id = None
        self._wheel_part_types = None
        self.discriminator = None
        if wheel_part_type_id is not None:
            self.wheel_part_type_id = wheel_part_type_id
        if wheel_part_types is not None:
            self.wheel_part_types = wheel_part_types

    @property
    def wheel_part_type_id(self):
        """Gets the wheel_part_type_id of this WheelPartType.  # noqa: E501

        WheelPartTypeID used to filter result  # noqa: E501

        :return: The wheel_part_type_id of this WheelPartType.  # noqa: E501
        :rtype: str
        """
        return self._wheel_part_type_id

    @wheel_part_type_id.setter
    def wheel_part_type_id(self, wheel_part_type_id):
        """Sets the wheel_part_type_id of this WheelPartType.

        WheelPartTypeID used to filter result  # noqa: E501

        :param wheel_part_type_id: The wheel_part_type_id of this WheelPartType.  # noqa: E501
        :type: str
        """

        self._wheel_part_type_id = wheel_part_type_id

    @property
    def wheel_part_types(self):
        """Gets the wheel_part_types of this WheelPartType.  # noqa: E501

        WheelPartType Name  # noqa: E501

        :return: The wheel_part_types of this WheelPartType.  # noqa: E501
        :rtype: list[LocalizedString]
        """
        return self._wheel_part_types

    @wheel_part_types.setter
    def wheel_part_types(self, wheel_part_types):
        """Sets the wheel_part_types of this WheelPartType.

        WheelPartType Name  # noqa: E501

        :param wheel_part_types: The wheel_part_types of this WheelPartType.  # noqa: E501
        :type: list[LocalizedString]
        """

        self._wheel_part_types = wheel_part_types

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
        if issubclass(WheelPartType, dict):
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
        if not isinstance(other, WheelPartType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
