# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class PartsFilters(object):
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
        'filter_lines': 'list[FilterLine]'
    }

    attribute_map = {
        'filter_lines': 'filterLines'
    }

    def __init__(self, filter_lines=None):  # noqa: E501
        """PartsFilters - a model defined in Swagger"""  # noqa: E501
        self._filter_lines = None
        self.discriminator = None
        if filter_lines is not None:
            self.filter_lines = filter_lines

    @property
    def filter_lines(self):
        """Gets the filter_lines of this PartsFilters.  # noqa: E501


        :return: The filter_lines of this PartsFilters.  # noqa: E501
        :rtype: list[FilterLine]
        """
        return self._filter_lines

    @filter_lines.setter
    def filter_lines(self, filter_lines):
        """Sets the filter_lines of this PartsFilters.


        :param filter_lines: The filter_lines of this PartsFilters.  # noqa: E501
        :type: list[FilterLine]
        """

        self._filter_lines = filter_lines

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
        if issubclass(PartsFilters, dict):
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
        if not isinstance(other, PartsFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
