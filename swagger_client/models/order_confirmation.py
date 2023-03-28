# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class OrderConfirmation(object):
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
        'order_number': 'str',
        'creation_date': 'datetime'
    }

    attribute_map = {
        'order_number': 'orderNumber',
        'creation_date': 'creationDate'
    }

    def __init__(self, order_number=None, creation_date=None):  # noqa: E501
        """OrderConfirmation - a model defined in Swagger"""  # noqa: E501
        self._order_number = None
        self._creation_date = None
        self.discriminator = None
        if order_number is not None:
            self.order_number = order_number
        if creation_date is not None:
            self.creation_date = creation_date

    @property
    def order_number(self):
        """Gets the order_number of this OrderConfirmation.  # noqa: E501

        Internal identifier for the order.  # noqa: E501

        :return: The order_number of this OrderConfirmation.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this OrderConfirmation.

        Internal identifier for the order.  # noqa: E501

        :param order_number: The order_number of this OrderConfirmation.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def creation_date(self):
        """Gets the creation_date of this OrderConfirmation.  # noqa: E501

        Date when the order was processed.  # noqa: E501

        :return: The creation_date of this OrderConfirmation.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this OrderConfirmation.

        Date when the order was processed.  # noqa: E501

        :param creation_date: The creation_date of this OrderConfirmation.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

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
        if issubclass(OrderConfirmation, dict):
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
        if not isinstance(other, OrderConfirmation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
