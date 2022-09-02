# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4752
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


class ContractForDifferenceAllOf(object):
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
        'start_date': 'datetime',
        'maturity_date': 'datetime',
        'code': 'str',
        'contract_size': 'float',
        'pay_ccy': 'str',
        'reference_rate': 'float',
        'type': 'str',
        'underlying_ccy': 'str',
        'underlying_identifier': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'code': 'code',
        'contract_size': 'contractSize',
        'pay_ccy': 'payCcy',
        'reference_rate': 'referenceRate',
        'type': 'type',
        'underlying_ccy': 'underlyingCcy',
        'underlying_identifier': 'underlyingIdentifier',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'start_date': 'required',
        'maturity_date': 'optional',
        'code': 'required',
        'contract_size': 'required',
        'pay_ccy': 'required',
        'reference_rate': 'optional',
        'type': 'required',
        'underlying_ccy': 'required',
        'underlying_identifier': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, start_date=None, maturity_date=None, code=None, contract_size=None, pay_ccy=None, reference_rate=None, type=None, underlying_ccy=None, underlying_identifier=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """ContractForDifferenceAllOf - a model defined in OpenAPI"
        
        :param start_date:  The start date of the CFD. (required)
        :type start_date: datetime
        :param maturity_date:  The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set.
        :type maturity_date: datetime
        :param code:  The code of the underlying. (required)
        :type code: str
        :param contract_size:  The size of the CFD contract, this should represent the total number of stocks that the CFD represents. (required)
        :type contract_size: float
        :param pay_ccy:  The currency that this CFD pays out, this can be different to the UnderlyingCcy. (required)
        :type pay_ccy: str
        :param reference_rate:  The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0.
        :type reference_rate: float
        :param type:  The type of CFD.    Supported string (enumeration) values are: [Cash, Futures]. (required)
        :type type: str
        :param underlying_ccy:  The currency of the underlying (required)
        :type underlying_ccy: str
        :param underlying_identifier:  external market codes and identifiers for the CFD, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode]. (required)
        :type underlying_identifier: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date = None
        self._maturity_date = None
        self._code = None
        self._contract_size = None
        self._pay_ccy = None
        self._reference_rate = None
        self._type = None
        self._underlying_ccy = None
        self._underlying_identifier = None
        self._instrument_type = None
        self.discriminator = None

        self.start_date = start_date
        if maturity_date is not None:
            self.maturity_date = maturity_date
        self.code = code
        self.contract_size = contract_size
        self.pay_ccy = pay_ccy
        if reference_rate is not None:
            self.reference_rate = reference_rate
        self.type = type
        self.underlying_ccy = underlying_ccy
        self.underlying_identifier = underlying_identifier
        self.instrument_type = instrument_type

    @property
    def start_date(self):
        """Gets the start_date of this ContractForDifferenceAllOf.  # noqa: E501

        The start date of the CFD.  # noqa: E501

        :return: The start_date of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ContractForDifferenceAllOf.

        The start date of the CFD.  # noqa: E501

        :param start_date: The start_date of this ContractForDifferenceAllOf.  # noqa: E501
        :type start_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this ContractForDifferenceAllOf.  # noqa: E501

        The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set.  # noqa: E501

        :return: The maturity_date of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this ContractForDifferenceAllOf.

        The maturity date for the CFD. If CFDType is Futures, this should be set to be the maturity date of the underlying  future. If CFDType is Cash, this should not be set.  # noqa: E501

        :param maturity_date: The maturity_date of this ContractForDifferenceAllOf.  # noqa: E501
        :type maturity_date: datetime
        """

        self._maturity_date = maturity_date

    @property
    def code(self):
        """Gets the code of this ContractForDifferenceAllOf.  # noqa: E501

        The code of the underlying.  # noqa: E501

        :return: The code of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ContractForDifferenceAllOf.

        The code of the underlying.  # noqa: E501

        :param code: The code of this ContractForDifferenceAllOf.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def contract_size(self):
        """Gets the contract_size of this ContractForDifferenceAllOf.  # noqa: E501

        The size of the CFD contract, this should represent the total number of stocks that the CFD represents.  # noqa: E501

        :return: The contract_size of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: float
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this ContractForDifferenceAllOf.

        The size of the CFD contract, this should represent the total number of stocks that the CFD represents.  # noqa: E501

        :param contract_size: The contract_size of this ContractForDifferenceAllOf.  # noqa: E501
        :type contract_size: float
        """
        if self.local_vars_configuration.client_side_validation and contract_size is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_size`, must not be `None`")  # noqa: E501

        self._contract_size = contract_size

    @property
    def pay_ccy(self):
        """Gets the pay_ccy of this ContractForDifferenceAllOf.  # noqa: E501

        The currency that this CFD pays out, this can be different to the UnderlyingCcy.  # noqa: E501

        :return: The pay_ccy of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._pay_ccy

    @pay_ccy.setter
    def pay_ccy(self, pay_ccy):
        """Sets the pay_ccy of this ContractForDifferenceAllOf.

        The currency that this CFD pays out, this can be different to the UnderlyingCcy.  # noqa: E501

        :param pay_ccy: The pay_ccy of this ContractForDifferenceAllOf.  # noqa: E501
        :type pay_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and pay_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `pay_ccy`, must not be `None`")  # noqa: E501

        self._pay_ccy = pay_ccy

    @property
    def reference_rate(self):
        """Gets the reference_rate of this ContractForDifferenceAllOf.  # noqa: E501

        The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0.  # noqa: E501

        :return: The reference_rate of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: float
        """
        return self._reference_rate

    @reference_rate.setter
    def reference_rate(self, reference_rate):
        """Sets the reference_rate of this ContractForDifferenceAllOf.

        The reference rate of the CFD, this can be set to 0 but not negative values.  This field is optional, if not set it will default to 0.  # noqa: E501

        :param reference_rate: The reference_rate of this ContractForDifferenceAllOf.  # noqa: E501
        :type reference_rate: float
        """

        self._reference_rate = reference_rate

    @property
    def type(self):
        """Gets the type of this ContractForDifferenceAllOf.  # noqa: E501

        The type of CFD.    Supported string (enumeration) values are: [Cash, Futures].  # noqa: E501

        :return: The type of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContractForDifferenceAllOf.

        The type of CFD.    Supported string (enumeration) values are: [Cash, Futures].  # noqa: E501

        :param type: The type of this ContractForDifferenceAllOf.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def underlying_ccy(self):
        """Gets the underlying_ccy of this ContractForDifferenceAllOf.  # noqa: E501

        The currency of the underlying  # noqa: E501

        :return: The underlying_ccy of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._underlying_ccy

    @underlying_ccy.setter
    def underlying_ccy(self, underlying_ccy):
        """Sets the underlying_ccy of this ContractForDifferenceAllOf.

        The currency of the underlying  # noqa: E501

        :param underlying_ccy: The underlying_ccy of this ContractForDifferenceAllOf.  # noqa: E501
        :type underlying_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and underlying_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `underlying_ccy`, must not be `None`")  # noqa: E501

        self._underlying_ccy = underlying_ccy

    @property
    def underlying_identifier(self):
        """Gets the underlying_identifier of this ContractForDifferenceAllOf.  # noqa: E501

        external market codes and identifiers for the CFD, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  # noqa: E501

        :return: The underlying_identifier of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._underlying_identifier

    @underlying_identifier.setter
    def underlying_identifier(self, underlying_identifier):
        """Sets the underlying_identifier of this ContractForDifferenceAllOf.

        external market codes and identifiers for the CFD, e.g. RIC.    Supported string (enumeration) values are: [LusidInstrumentId, Isin, Sedol, Cusip, ClientInternal, Figi, RIC, QuotePermId, REDCode, BBGId, ICECode].  # noqa: E501

        :param underlying_identifier: The underlying_identifier of this ContractForDifferenceAllOf.  # noqa: E501
        :type underlying_identifier: str
        """
        if self.local_vars_configuration.client_side_validation and underlying_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `underlying_identifier`, must not be `None`")  # noqa: E501

        self._underlying_identifier = underlying_identifier

    @property
    def instrument_type(self):
        """Gets the instrument_type of this ContractForDifferenceAllOf.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond  # noqa: E501

        :return: The instrument_type of this ContractForDifferenceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this ContractForDifferenceAllOf.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption, ReferenceInstrument, ComplexBond, InflationLinkedBond  # noqa: E501

        :param instrument_type: The instrument_type of this ContractForDifferenceAllOf.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption", "ReferenceInstrument", "ComplexBond", "InflationLinkedBond"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, ContractForDifferenceAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContractForDifferenceAllOf):
            return True

        return self.to_dict() != other.to_dict()
