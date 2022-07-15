# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4609
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


class PortfolioDetails(object):
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
        'href': 'str',
        'origin_portfolio_id': 'ResourceId',
        'version': 'Version',
        'base_currency': 'str',
        'corporate_action_source_id': 'ResourceId',
        'sub_holding_keys': 'list[str]',
        'instrument_scopes': 'list[str]',
        'accounting_method': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'origin_portfolio_id': 'originPortfolioId',
        'version': 'version',
        'base_currency': 'baseCurrency',
        'corporate_action_source_id': 'corporateActionSourceId',
        'sub_holding_keys': 'subHoldingKeys',
        'instrument_scopes': 'instrumentScopes',
        'accounting_method': 'accountingMethod',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'origin_portfolio_id': 'required',
        'version': 'required',
        'base_currency': 'required',
        'corporate_action_source_id': 'optional',
        'sub_holding_keys': 'optional',
        'instrument_scopes': 'optional',
        'accounting_method': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, origin_portfolio_id=None, version=None, base_currency=None, corporate_action_source_id=None, sub_holding_keys=None, instrument_scopes=None, accounting_method=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PortfolioDetails - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param origin_portfolio_id:  (required)
        :type origin_portfolio_id: lusid.ResourceId
        :param version:  (required)
        :type version: lusid.Version
        :param base_currency:  The base currency of the transaction portfolio. (required)
        :type base_currency: str
        :param corporate_action_source_id: 
        :type corporate_action_source_id: lusid.ResourceId
        :param sub_holding_keys: 
        :type sub_holding_keys: list[str]
        :param instrument_scopes:  The resolution strategy used to resolve instruments of transactions/holdings upserted to the transaction portfolio.
        :type instrument_scopes: list[str]
        :param accounting_method:  . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst
        :type accounting_method: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._origin_portfolio_id = None
        self._version = None
        self._base_currency = None
        self._corporate_action_source_id = None
        self._sub_holding_keys = None
        self._instrument_scopes = None
        self._accounting_method = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.origin_portfolio_id = origin_portfolio_id
        self.version = version
        self.base_currency = base_currency
        if corporate_action_source_id is not None:
            self.corporate_action_source_id = corporate_action_source_id
        self.sub_holding_keys = sub_holding_keys
        self.instrument_scopes = instrument_scopes
        if accounting_method is not None:
            self.accounting_method = accounting_method
        self.links = links

    @property
    def href(self):
        """Gets the href of this PortfolioDetails.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this PortfolioDetails.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PortfolioDetails.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this PortfolioDetails.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def origin_portfolio_id(self):
        """Gets the origin_portfolio_id of this PortfolioDetails.  # noqa: E501


        :return: The origin_portfolio_id of this PortfolioDetails.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._origin_portfolio_id

    @origin_portfolio_id.setter
    def origin_portfolio_id(self, origin_portfolio_id):
        """Sets the origin_portfolio_id of this PortfolioDetails.


        :param origin_portfolio_id: The origin_portfolio_id of this PortfolioDetails.  # noqa: E501
        :type origin_portfolio_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and origin_portfolio_id is None:  # noqa: E501
            raise ValueError("Invalid value for `origin_portfolio_id`, must not be `None`")  # noqa: E501

        self._origin_portfolio_id = origin_portfolio_id

    @property
    def version(self):
        """Gets the version of this PortfolioDetails.  # noqa: E501


        :return: The version of this PortfolioDetails.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PortfolioDetails.


        :param version: The version of this PortfolioDetails.  # noqa: E501
        :type version: lusid.Version
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def base_currency(self):
        """Gets the base_currency of this PortfolioDetails.  # noqa: E501

        The base currency of the transaction portfolio.  # noqa: E501

        :return: The base_currency of this PortfolioDetails.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this PortfolioDetails.

        The base currency of the transaction portfolio.  # noqa: E501

        :param base_currency: The base_currency of this PortfolioDetails.  # noqa: E501
        :type base_currency: str
        """
        if self.local_vars_configuration.client_side_validation and base_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `base_currency`, must not be `None`")  # noqa: E501

        self._base_currency = base_currency

    @property
    def corporate_action_source_id(self):
        """Gets the corporate_action_source_id of this PortfolioDetails.  # noqa: E501


        :return: The corporate_action_source_id of this PortfolioDetails.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._corporate_action_source_id

    @corporate_action_source_id.setter
    def corporate_action_source_id(self, corporate_action_source_id):
        """Sets the corporate_action_source_id of this PortfolioDetails.


        :param corporate_action_source_id: The corporate_action_source_id of this PortfolioDetails.  # noqa: E501
        :type corporate_action_source_id: lusid.ResourceId
        """

        self._corporate_action_source_id = corporate_action_source_id

    @property
    def sub_holding_keys(self):
        """Gets the sub_holding_keys of this PortfolioDetails.  # noqa: E501


        :return: The sub_holding_keys of this PortfolioDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._sub_holding_keys

    @sub_holding_keys.setter
    def sub_holding_keys(self, sub_holding_keys):
        """Sets the sub_holding_keys of this PortfolioDetails.


        :param sub_holding_keys: The sub_holding_keys of this PortfolioDetails.  # noqa: E501
        :type sub_holding_keys: list[str]
        """

        self._sub_holding_keys = sub_holding_keys

    @property
    def instrument_scopes(self):
        """Gets the instrument_scopes of this PortfolioDetails.  # noqa: E501

        The resolution strategy used to resolve instruments of transactions/holdings upserted to the transaction portfolio.  # noqa: E501

        :return: The instrument_scopes of this PortfolioDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._instrument_scopes

    @instrument_scopes.setter
    def instrument_scopes(self, instrument_scopes):
        """Sets the instrument_scopes of this PortfolioDetails.

        The resolution strategy used to resolve instruments of transactions/holdings upserted to the transaction portfolio.  # noqa: E501

        :param instrument_scopes: The instrument_scopes of this PortfolioDetails.  # noqa: E501
        :type instrument_scopes: list[str]
        """

        self._instrument_scopes = instrument_scopes

    @property
    def accounting_method(self):
        """Gets the accounting_method of this PortfolioDetails.  # noqa: E501

        . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst  # noqa: E501

        :return: The accounting_method of this PortfolioDetails.  # noqa: E501
        :rtype: str
        """
        return self._accounting_method

    @accounting_method.setter
    def accounting_method(self, accounting_method):
        """Sets the accounting_method of this PortfolioDetails.

        . The available values are: Default, AverageCost, FirstInFirstOut, LastInFirstOut, HighestCostFirst, LowestCostFirst  # noqa: E501

        :param accounting_method: The accounting_method of this PortfolioDetails.  # noqa: E501
        :type accounting_method: str
        """
        allowed_values = ["Default", "AverageCost", "FirstInFirstOut", "LastInFirstOut", "HighestCostFirst", "LowestCostFirst"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and accounting_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `accounting_method` ({0}), must be one of {1}"  # noqa: E501
                .format(accounting_method, allowed_values)
            )

        self._accounting_method = accounting_method

    @property
    def links(self):
        """Gets the links of this PortfolioDetails.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this PortfolioDetails.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PortfolioDetails.

        Collection of links.  # noqa: E501

        :param links: The links of this PortfolioDetails.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, PortfolioDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortfolioDetails):
            return True

        return self.to_dict() != other.to_dict()
