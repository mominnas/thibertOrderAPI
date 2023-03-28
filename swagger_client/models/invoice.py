# coding: utf-8

"""
    TAPI

     

    OpenAPI spec version: V1 DEVELOPMENT
    
      
"""

import pprint
import re  # noqa: F401

import six

class Invoice(object):
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
        'document_id': 'str',
        'document_type': 'str',
        'original_order_id': 'str',
        'currency_id': 'str',
        'prices_incl_tax': 'float',
        'status': 'str',
        'sales_person_id': 'str',
        'sales_person_name': 'str',
        'contact_id': 'str',
        'contact_name': 'str',
        'tax_percent': 'float',
        'tax_amount': 'float',
        'invoice_discount': 'float',
        'subtotal': 'float',
        'total_excl_tax': 'float',
        'total_incl_tax': 'float',
        'order_date': 'str',
        'posting_date': 'str',
        'document_date': 'str',
        'due_date': 'str',
        'shipment_date': 'str',
        'payment_terms_code': 'str',
        'payment_method_name': 'str',
        'payment_status': 'str',
        'payment_transaction_id': 'str',
        'location_code': 'str',
        'shipping_method_code': 'str',
        'customer_id': 'str',
        'reference_no': 'str',
        'shop_account_email': 'str',
        'outstanding_amount': 'float',
        'shipping_method_name': 'str',
        'order_lines_count': 'int',
        'sell_to_address': 'Address',
        'bill_to_address': 'Address',
        'ship_to_address': 'Address',
        'sales_lines': 'list[Salesline]',
        'tax_lines': 'list[Taxline]'
    }

    attribute_map = {
        'document_id': 'documentId',
        'document_type': 'documentType',
        'original_order_id': 'originalOrderId',
        'currency_id': 'currencyId',
        'prices_incl_tax': 'pricesInclTax',
        'status': 'status',
        'sales_person_id': 'salesPersonId',
        'sales_person_name': 'salesPersonName',
        'contact_id': 'contactId',
        'contact_name': 'contactName',
        'tax_percent': 'taxPercent',
        'tax_amount': 'taxAmount',
        'invoice_discount': 'invoiceDiscount',
        'subtotal': 'subtotal',
        'total_excl_tax': 'totalExclTax',
        'total_incl_tax': 'totalInclTax',
        'order_date': 'orderDate',
        'posting_date': 'postingDate',
        'document_date': 'documentDate',
        'due_date': 'dueDate',
        'shipment_date': 'shipmentDate',
        'payment_terms_code': 'paymentTermsCode',
        'payment_method_name': 'paymentMethodName',
        'payment_status': 'paymentStatus',
        'payment_transaction_id': 'paymentTransactionId',
        'location_code': 'locationCode',
        'shipping_method_code': 'shippingMethodCode',
        'customer_id': 'customerId',
        'reference_no': 'referenceNo',
        'shop_account_email': 'shopAccountEmail',
        'outstanding_amount': 'outstandingAmount',
        'shipping_method_name': 'shippingMethodName',
        'order_lines_count': 'orderLinesCount',
        'sell_to_address': 'sellToAddress',
        'bill_to_address': 'billToAddress',
        'ship_to_address': 'shipToAddress',
        'sales_lines': 'salesLines',
        'tax_lines': 'taxLines'
    }

    def __init__(self, document_id=None, document_type=None, original_order_id=None, currency_id=None, prices_incl_tax=None, status=None, sales_person_id=None, sales_person_name=None, contact_id=None, contact_name=None, tax_percent=None, tax_amount=None, invoice_discount=None, subtotal=None, total_excl_tax=None, total_incl_tax=None, order_date=None, posting_date=None, document_date=None, due_date=None, shipment_date=None, payment_terms_code=None, payment_method_name=None, payment_status=None, payment_transaction_id=None, location_code=None, shipping_method_code=None, customer_id=None, reference_no=None, shop_account_email=None, outstanding_amount=None, shipping_method_name=None, order_lines_count=None, sell_to_address=None, bill_to_address=None, ship_to_address=None, sales_lines=None, tax_lines=None):  # noqa: E501
        """Invoice - a model defined in Swagger"""  # noqa: E501
        self._document_id = None
        self._document_type = None
        self._original_order_id = None
        self._currency_id = None
        self._prices_incl_tax = None
        self._status = None
        self._sales_person_id = None
        self._sales_person_name = None
        self._contact_id = None
        self._contact_name = None
        self._tax_percent = None
        self._tax_amount = None
        self._invoice_discount = None
        self._subtotal = None
        self._total_excl_tax = None
        self._total_incl_tax = None
        self._order_date = None
        self._posting_date = None
        self._document_date = None
        self._due_date = None
        self._shipment_date = None
        self._payment_terms_code = None
        self._payment_method_name = None
        self._payment_status = None
        self._payment_transaction_id = None
        self._location_code = None
        self._shipping_method_code = None
        self._customer_id = None
        self._reference_no = None
        self._shop_account_email = None
        self._outstanding_amount = None
        self._shipping_method_name = None
        self._order_lines_count = None
        self._sell_to_address = None
        self._bill_to_address = None
        self._ship_to_address = None
        self._sales_lines = None
        self._tax_lines = None
        self.discriminator = None
        if document_id is not None:
            self.document_id = document_id
        if document_type is not None:
            self.document_type = document_type
        if original_order_id is not None:
            self.original_order_id = original_order_id
        if currency_id is not None:
            self.currency_id = currency_id
        if prices_incl_tax is not None:
            self.prices_incl_tax = prices_incl_tax
        if status is not None:
            self.status = status
        if sales_person_id is not None:
            self.sales_person_id = sales_person_id
        if sales_person_name is not None:
            self.sales_person_name = sales_person_name
        if contact_id is not None:
            self.contact_id = contact_id
        if contact_name is not None:
            self.contact_name = contact_name
        if tax_percent is not None:
            self.tax_percent = tax_percent
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if invoice_discount is not None:
            self.invoice_discount = invoice_discount
        if subtotal is not None:
            self.subtotal = subtotal
        if total_excl_tax is not None:
            self.total_excl_tax = total_excl_tax
        if total_incl_tax is not None:
            self.total_incl_tax = total_incl_tax
        if order_date is not None:
            self.order_date = order_date
        if posting_date is not None:
            self.posting_date = posting_date
        if document_date is not None:
            self.document_date = document_date
        if due_date is not None:
            self.due_date = due_date
        if shipment_date is not None:
            self.shipment_date = shipment_date
        if payment_terms_code is not None:
            self.payment_terms_code = payment_terms_code
        if payment_method_name is not None:
            self.payment_method_name = payment_method_name
        if payment_status is not None:
            self.payment_status = payment_status
        if payment_transaction_id is not None:
            self.payment_transaction_id = payment_transaction_id
        if location_code is not None:
            self.location_code = location_code
        if shipping_method_code is not None:
            self.shipping_method_code = shipping_method_code
        if customer_id is not None:
            self.customer_id = customer_id
        if reference_no is not None:
            self.reference_no = reference_no
        if shop_account_email is not None:
            self.shop_account_email = shop_account_email
        if outstanding_amount is not None:
            self.outstanding_amount = outstanding_amount
        if shipping_method_name is not None:
            self.shipping_method_name = shipping_method_name
        if order_lines_count is not None:
            self.order_lines_count = order_lines_count
        if sell_to_address is not None:
            self.sell_to_address = sell_to_address
        if bill_to_address is not None:
            self.bill_to_address = bill_to_address
        if ship_to_address is not None:
            self.ship_to_address = ship_to_address
        if sales_lines is not None:
            self.sales_lines = sales_lines
        if tax_lines is not None:
            self.tax_lines = tax_lines

    @property
    def document_id(self):
        """Gets the document_id of this Invoice.  # noqa: E501


        :return: The document_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Invoice.


        :param document_id: The document_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_type(self):
        """Gets the document_type of this Invoice.  # noqa: E501


        :return: The document_type of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this Invoice.


        :param document_type: The document_type of this Invoice.  # noqa: E501
        :type: str
        """

        self._document_type = document_type

    @property
    def original_order_id(self):
        """Gets the original_order_id of this Invoice.  # noqa: E501


        :return: The original_order_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._original_order_id

    @original_order_id.setter
    def original_order_id(self, original_order_id):
        """Sets the original_order_id of this Invoice.


        :param original_order_id: The original_order_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._original_order_id = original_order_id

    @property
    def currency_id(self):
        """Gets the currency_id of this Invoice.  # noqa: E501


        :return: The currency_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this Invoice.


        :param currency_id: The currency_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._currency_id = currency_id

    @property
    def prices_incl_tax(self):
        """Gets the prices_incl_tax of this Invoice.  # noqa: E501


        :return: The prices_incl_tax of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._prices_incl_tax

    @prices_incl_tax.setter
    def prices_incl_tax(self, prices_incl_tax):
        """Sets the prices_incl_tax of this Invoice.


        :param prices_incl_tax: The prices_incl_tax of this Invoice.  # noqa: E501
        :type: float
        """

        self._prices_incl_tax = prices_incl_tax

    @property
    def status(self):
        """Gets the status of this Invoice.  # noqa: E501


        :return: The status of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.


        :param status: The status of this Invoice.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def sales_person_id(self):
        """Gets the sales_person_id of this Invoice.  # noqa: E501


        :return: The sales_person_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._sales_person_id

    @sales_person_id.setter
    def sales_person_id(self, sales_person_id):
        """Sets the sales_person_id of this Invoice.


        :param sales_person_id: The sales_person_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._sales_person_id = sales_person_id

    @property
    def sales_person_name(self):
        """Gets the sales_person_name of this Invoice.  # noqa: E501


        :return: The sales_person_name of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._sales_person_name

    @sales_person_name.setter
    def sales_person_name(self, sales_person_name):
        """Sets the sales_person_name of this Invoice.


        :param sales_person_name: The sales_person_name of this Invoice.  # noqa: E501
        :type: str
        """

        self._sales_person_name = sales_person_name

    @property
    def contact_id(self):
        """Gets the contact_id of this Invoice.  # noqa: E501


        :return: The contact_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this Invoice.


        :param contact_id: The contact_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def contact_name(self):
        """Gets the contact_name of this Invoice.  # noqa: E501


        :return: The contact_name of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this Invoice.


        :param contact_name: The contact_name of this Invoice.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def tax_percent(self):
        """Gets the tax_percent of this Invoice.  # noqa: E501


        :return: The tax_percent of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._tax_percent

    @tax_percent.setter
    def tax_percent(self, tax_percent):
        """Sets the tax_percent of this Invoice.


        :param tax_percent: The tax_percent of this Invoice.  # noqa: E501
        :type: float
        """

        self._tax_percent = tax_percent

    @property
    def tax_amount(self):
        """Gets the tax_amount of this Invoice.  # noqa: E501


        :return: The tax_amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this Invoice.


        :param tax_amount: The tax_amount of this Invoice.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def invoice_discount(self):
        """Gets the invoice_discount of this Invoice.  # noqa: E501


        :return: The invoice_discount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._invoice_discount

    @invoice_discount.setter
    def invoice_discount(self, invoice_discount):
        """Sets the invoice_discount of this Invoice.


        :param invoice_discount: The invoice_discount of this Invoice.  # noqa: E501
        :type: float
        """

        self._invoice_discount = invoice_discount

    @property
    def subtotal(self):
        """Gets the subtotal of this Invoice.  # noqa: E501


        :return: The subtotal of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this Invoice.


        :param subtotal: The subtotal of this Invoice.  # noqa: E501
        :type: float
        """

        self._subtotal = subtotal

    @property
    def total_excl_tax(self):
        """Gets the total_excl_tax of this Invoice.  # noqa: E501


        :return: The total_excl_tax of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._total_excl_tax

    @total_excl_tax.setter
    def total_excl_tax(self, total_excl_tax):
        """Sets the total_excl_tax of this Invoice.


        :param total_excl_tax: The total_excl_tax of this Invoice.  # noqa: E501
        :type: float
        """

        self._total_excl_tax = total_excl_tax

    @property
    def total_incl_tax(self):
        """Gets the total_incl_tax of this Invoice.  # noqa: E501


        :return: The total_incl_tax of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._total_incl_tax

    @total_incl_tax.setter
    def total_incl_tax(self, total_incl_tax):
        """Sets the total_incl_tax of this Invoice.


        :param total_incl_tax: The total_incl_tax of this Invoice.  # noqa: E501
        :type: float
        """

        self._total_incl_tax = total_incl_tax

    @property
    def order_date(self):
        """Gets the order_date of this Invoice.  # noqa: E501


        :return: The order_date of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this Invoice.


        :param order_date: The order_date of this Invoice.  # noqa: E501
        :type: str
        """

        self._order_date = order_date

    @property
    def posting_date(self):
        """Gets the posting_date of this Invoice.  # noqa: E501


        :return: The posting_date of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._posting_date

    @posting_date.setter
    def posting_date(self, posting_date):
        """Sets the posting_date of this Invoice.


        :param posting_date: The posting_date of this Invoice.  # noqa: E501
        :type: str
        """

        self._posting_date = posting_date

    @property
    def document_date(self):
        """Gets the document_date of this Invoice.  # noqa: E501


        :return: The document_date of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._document_date

    @document_date.setter
    def document_date(self, document_date):
        """Sets the document_date of this Invoice.


        :param document_date: The document_date of this Invoice.  # noqa: E501
        :type: str
        """

        self._document_date = document_date

    @property
    def due_date(self):
        """Gets the due_date of this Invoice.  # noqa: E501


        :return: The due_date of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this Invoice.


        :param due_date: The due_date of this Invoice.  # noqa: E501
        :type: str
        """

        self._due_date = due_date

    @property
    def shipment_date(self):
        """Gets the shipment_date of this Invoice.  # noqa: E501


        :return: The shipment_date of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._shipment_date

    @shipment_date.setter
    def shipment_date(self, shipment_date):
        """Sets the shipment_date of this Invoice.


        :param shipment_date: The shipment_date of this Invoice.  # noqa: E501
        :type: str
        """

        self._shipment_date = shipment_date

    @property
    def payment_terms_code(self):
        """Gets the payment_terms_code of this Invoice.  # noqa: E501


        :return: The payment_terms_code of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._payment_terms_code

    @payment_terms_code.setter
    def payment_terms_code(self, payment_terms_code):
        """Sets the payment_terms_code of this Invoice.


        :param payment_terms_code: The payment_terms_code of this Invoice.  # noqa: E501
        :type: str
        """

        self._payment_terms_code = payment_terms_code

    @property
    def payment_method_name(self):
        """Gets the payment_method_name of this Invoice.  # noqa: E501


        :return: The payment_method_name of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_name

    @payment_method_name.setter
    def payment_method_name(self, payment_method_name):
        """Sets the payment_method_name of this Invoice.


        :param payment_method_name: The payment_method_name of this Invoice.  # noqa: E501
        :type: str
        """

        self._payment_method_name = payment_method_name

    @property
    def payment_status(self):
        """Gets the payment_status of this Invoice.  # noqa: E501


        :return: The payment_status of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """Sets the payment_status of this Invoice.


        :param payment_status: The payment_status of this Invoice.  # noqa: E501
        :type: str
        """

        self._payment_status = payment_status

    @property
    def payment_transaction_id(self):
        """Gets the payment_transaction_id of this Invoice.  # noqa: E501


        :return: The payment_transaction_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._payment_transaction_id

    @payment_transaction_id.setter
    def payment_transaction_id(self, payment_transaction_id):
        """Sets the payment_transaction_id of this Invoice.


        :param payment_transaction_id: The payment_transaction_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._payment_transaction_id = payment_transaction_id

    @property
    def location_code(self):
        """Gets the location_code of this Invoice.  # noqa: E501


        :return: The location_code of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._location_code

    @location_code.setter
    def location_code(self, location_code):
        """Sets the location_code of this Invoice.


        :param location_code: The location_code of this Invoice.  # noqa: E501
        :type: str
        """

        self._location_code = location_code

    @property
    def shipping_method_code(self):
        """Gets the shipping_method_code of this Invoice.  # noqa: E501


        :return: The shipping_method_code of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._shipping_method_code

    @shipping_method_code.setter
    def shipping_method_code(self, shipping_method_code):
        """Sets the shipping_method_code of this Invoice.


        :param shipping_method_code: The shipping_method_code of this Invoice.  # noqa: E501
        :type: str
        """

        self._shipping_method_code = shipping_method_code

    @property
    def customer_id(self):
        """Gets the customer_id of this Invoice.  # noqa: E501


        :return: The customer_id of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Invoice.


        :param customer_id: The customer_id of this Invoice.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def reference_no(self):
        """Gets the reference_no of this Invoice.  # noqa: E501


        :return: The reference_no of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._reference_no

    @reference_no.setter
    def reference_no(self, reference_no):
        """Sets the reference_no of this Invoice.


        :param reference_no: The reference_no of this Invoice.  # noqa: E501
        :type: str
        """

        self._reference_no = reference_no

    @property
    def shop_account_email(self):
        """Gets the shop_account_email of this Invoice.  # noqa: E501


        :return: The shop_account_email of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._shop_account_email

    @shop_account_email.setter
    def shop_account_email(self, shop_account_email):
        """Sets the shop_account_email of this Invoice.


        :param shop_account_email: The shop_account_email of this Invoice.  # noqa: E501
        :type: str
        """

        self._shop_account_email = shop_account_email

    @property
    def outstanding_amount(self):
        """Gets the outstanding_amount of this Invoice.  # noqa: E501


        :return: The outstanding_amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._outstanding_amount

    @outstanding_amount.setter
    def outstanding_amount(self, outstanding_amount):
        """Sets the outstanding_amount of this Invoice.


        :param outstanding_amount: The outstanding_amount of this Invoice.  # noqa: E501
        :type: float
        """

        self._outstanding_amount = outstanding_amount

    @property
    def shipping_method_name(self):
        """Gets the shipping_method_name of this Invoice.  # noqa: E501


        :return: The shipping_method_name of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._shipping_method_name

    @shipping_method_name.setter
    def shipping_method_name(self, shipping_method_name):
        """Sets the shipping_method_name of this Invoice.


        :param shipping_method_name: The shipping_method_name of this Invoice.  # noqa: E501
        :type: str
        """

        self._shipping_method_name = shipping_method_name

    @property
    def order_lines_count(self):
        """Gets the order_lines_count of this Invoice.  # noqa: E501


        :return: The order_lines_count of this Invoice.  # noqa: E501
        :rtype: int
        """
        return self._order_lines_count

    @order_lines_count.setter
    def order_lines_count(self, order_lines_count):
        """Sets the order_lines_count of this Invoice.


        :param order_lines_count: The order_lines_count of this Invoice.  # noqa: E501
        :type: int
        """

        self._order_lines_count = order_lines_count

    @property
    def sell_to_address(self):
        """Gets the sell_to_address of this Invoice.  # noqa: E501


        :return: The sell_to_address of this Invoice.  # noqa: E501
        :rtype: Address
        """
        return self._sell_to_address

    @sell_to_address.setter
    def sell_to_address(self, sell_to_address):
        """Sets the sell_to_address of this Invoice.


        :param sell_to_address: The sell_to_address of this Invoice.  # noqa: E501
        :type: Address
        """

        self._sell_to_address = sell_to_address

    @property
    def bill_to_address(self):
        """Gets the bill_to_address of this Invoice.  # noqa: E501


        :return: The bill_to_address of this Invoice.  # noqa: E501
        :rtype: Address
        """
        return self._bill_to_address

    @bill_to_address.setter
    def bill_to_address(self, bill_to_address):
        """Sets the bill_to_address of this Invoice.


        :param bill_to_address: The bill_to_address of this Invoice.  # noqa: E501
        :type: Address
        """

        self._bill_to_address = bill_to_address

    @property
    def ship_to_address(self):
        """Gets the ship_to_address of this Invoice.  # noqa: E501


        :return: The ship_to_address of this Invoice.  # noqa: E501
        :rtype: Address
        """
        return self._ship_to_address

    @ship_to_address.setter
    def ship_to_address(self, ship_to_address):
        """Sets the ship_to_address of this Invoice.


        :param ship_to_address: The ship_to_address of this Invoice.  # noqa: E501
        :type: Address
        """

        self._ship_to_address = ship_to_address

    @property
    def sales_lines(self):
        """Gets the sales_lines of this Invoice.  # noqa: E501


        :return: The sales_lines of this Invoice.  # noqa: E501
        :rtype: list[Salesline]
        """
        return self._sales_lines

    @sales_lines.setter
    def sales_lines(self, sales_lines):
        """Sets the sales_lines of this Invoice.


        :param sales_lines: The sales_lines of this Invoice.  # noqa: E501
        :type: list[Salesline]
        """

        self._sales_lines = sales_lines

    @property
    def tax_lines(self):
        """Gets the tax_lines of this Invoice.  # noqa: E501


        :return: The tax_lines of this Invoice.  # noqa: E501
        :rtype: list[Taxline]
        """
        return self._tax_lines

    @tax_lines.setter
    def tax_lines(self, tax_lines):
        """Sets the tax_lines of this Invoice.


        :param tax_lines: The tax_lines of this Invoice.  # noqa: E501
        :type: list[Taxline]
        """

        self._tax_lines = tax_lines

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
        if issubclass(Invoice, dict):
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
        if not isinstance(other, Invoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
