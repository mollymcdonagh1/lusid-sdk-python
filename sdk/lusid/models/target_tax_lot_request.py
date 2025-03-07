# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5045
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class TargetTaxLotRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'units': 'float',
        'cost': 'CurrencyAndAmount',
        'portfolio_cost': 'float',
        'price': 'float',
        'purchase_date': 'datetime',
        'settlement_date': 'datetime'
    }

    attribute_map = {
        'units': 'units',
        'cost': 'cost',
        'portfolio_cost': 'portfolioCost',
        'price': 'price',
        'purchase_date': 'purchaseDate',
        'settlement_date': 'settlementDate'
    }

    required_map = {
        'units': 'required',
        'cost': 'optional',
        'portfolio_cost': 'optional',
        'price': 'optional',
        'purchase_date': 'optional',
        'settlement_date': 'optional'
    }

    def __init__(self, units=None, cost=None, portfolio_cost=None, price=None, purchase_date=None, settlement_date=None, local_vars_configuration=None):  # noqa: E501
        """TargetTaxLotRequest - a model defined in OpenAPI"
        
        :param units:  The number of units of the instrument in this tax-lot. (required)
        :type units: float
        :param cost: 
        :type cost: lusid.CurrencyAndAmount
        :param portfolio_cost:  The total cost of the tax-lot in the transaction portfolio's base currency.
        :type portfolio_cost: float
        :param price:  The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots.
        :type price: float
        :param purchase_date:  The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots.
        :type purchase_date: datetime
        :param settlement_date:  The settlement date of the tax-lot's opening transaction.
        :type settlement_date: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._units = None
        self._cost = None
        self._portfolio_cost = None
        self._price = None
        self._purchase_date = None
        self._settlement_date = None
        self.discriminator = None

        self.units = units
        if cost is not None:
            self.cost = cost
        self.portfolio_cost = portfolio_cost
        self.price = price
        self.purchase_date = purchase_date
        self.settlement_date = settlement_date

    @property
    def units(self):
        """Gets the units of this TargetTaxLotRequest.  # noqa: E501

        The number of units of the instrument in this tax-lot.  # noqa: E501

        :return: The units of this TargetTaxLotRequest.  # noqa: E501
        :rtype: float
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this TargetTaxLotRequest.

        The number of units of the instrument in this tax-lot.  # noqa: E501

        :param units: The units of this TargetTaxLotRequest.  # noqa: E501
        :type units: float
        """
        if self.local_vars_configuration.client_side_validation and units is None:  # noqa: E501
            raise ValueError("Invalid value for `units`, must not be `None`")  # noqa: E501

        self._units = units

    @property
    def cost(self):
        """Gets the cost of this TargetTaxLotRequest.  # noqa: E501


        :return: The cost of this TargetTaxLotRequest.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this TargetTaxLotRequest.


        :param cost: The cost of this TargetTaxLotRequest.  # noqa: E501
        :type cost: lusid.CurrencyAndAmount
        """

        self._cost = cost

    @property
    def portfolio_cost(self):
        """Gets the portfolio_cost of this TargetTaxLotRequest.  # noqa: E501

        The total cost of the tax-lot in the transaction portfolio's base currency.  # noqa: E501

        :return: The portfolio_cost of this TargetTaxLotRequest.  # noqa: E501
        :rtype: float
        """
        return self._portfolio_cost

    @portfolio_cost.setter
    def portfolio_cost(self, portfolio_cost):
        """Sets the portfolio_cost of this TargetTaxLotRequest.

        The total cost of the tax-lot in the transaction portfolio's base currency.  # noqa: E501

        :param portfolio_cost: The portfolio_cost of this TargetTaxLotRequest.  # noqa: E501
        :type portfolio_cost: float
        """

        self._portfolio_cost = portfolio_cost

    @property
    def price(self):
        """Gets the price of this TargetTaxLotRequest.  # noqa: E501

        The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots.  # noqa: E501

        :return: The price of this TargetTaxLotRequest.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this TargetTaxLotRequest.

        The purchase price of each unit of the instrument held in this tax-lot. This forms part of the unique key required for multiple tax-lots.  # noqa: E501

        :param price: The price of this TargetTaxLotRequest.  # noqa: E501
        :type price: float
        """

        self._price = price

    @property
    def purchase_date(self):
        """Gets the purchase_date of this TargetTaxLotRequest.  # noqa: E501

        The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots.  # noqa: E501

        :return: The purchase_date of this TargetTaxLotRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, purchase_date):
        """Sets the purchase_date of this TargetTaxLotRequest.

        The purchase date of this tax-lot. This forms part of the unique key required for multiple tax-lots.  # noqa: E501

        :param purchase_date: The purchase_date of this TargetTaxLotRequest.  # noqa: E501
        :type purchase_date: datetime
        """

        self._purchase_date = purchase_date

    @property
    def settlement_date(self):
        """Gets the settlement_date of this TargetTaxLotRequest.  # noqa: E501

        The settlement date of the tax-lot's opening transaction.  # noqa: E501

        :return: The settlement_date of this TargetTaxLotRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this TargetTaxLotRequest.

        The settlement date of the tax-lot's opening transaction.  # noqa: E501

        :param settlement_date: The settlement_date of this TargetTaxLotRequest.  # noqa: E501
        :type settlement_date: datetime
        """

        self._settlement_date = settlement_date

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TargetTaxLotRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TargetTaxLotRequest):
            return True

        return self.to_dict() != other.to_dict()
