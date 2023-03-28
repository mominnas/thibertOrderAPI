# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class FilterTags(object):
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
        'tag_name': 'str',
        'tag_order': 'str',
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'tag_name': 'tagName',
        'tag_order': 'tagOrder',
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, tag_name=None, tag_order=None, name=None, value=None):  # noqa: E501
        """FilterTags - a model defined in Swagger"""  # noqa: E501
        self._tag_name = None
        self._tag_order = None
        self._name = None
        self._value = None
        self.discriminator = None
        if tag_name is not None:
            self.tag_name = tag_name
        if tag_order is not None:
            self.tag_order = tag_order
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def tag_name(self):
        """Gets the tag_name of this FilterTags.  # noqa: E501


        :return: The tag_name of this FilterTags.  # noqa: E501
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this FilterTags.


        :param tag_name: The tag_name of this FilterTags.  # noqa: E501
        :type: str
        """

        self._tag_name = tag_name

    @property
    def tag_order(self):
        """Gets the tag_order of this FilterTags.  # noqa: E501


        :return: The tag_order of this FilterTags.  # noqa: E501
        :rtype: str
        """
        return self._tag_order

    @tag_order.setter
    def tag_order(self, tag_order):
        """Sets the tag_order of this FilterTags.


        :param tag_order: The tag_order of this FilterTags.  # noqa: E501
        :type: str
        """

        self._tag_order = tag_order

    @property
    def name(self):
        """Gets the name of this FilterTags.  # noqa: E501


        :return: The name of this FilterTags.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilterTags.


        :param name: The name of this FilterTags.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this FilterTags.  # noqa: E501


        :return: The value of this FilterTags.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this FilterTags.


        :param value: The value of this FilterTags.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(FilterTags, dict):
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
        if not isinstance(other, FilterTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
