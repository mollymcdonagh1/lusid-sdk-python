# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4097
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


class ValuationSchedule(object):
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
        'effective_from': 'str',
        'effective_at': 'str',
        'tenor': 'str',
        'roll_convention': 'str',
        'holiday_calendars': 'list[str]',
        'valuation_date_times': 'list[str]'
    }

    attribute_map = {
        'effective_from': 'effectiveFrom',
        'effective_at': 'effectiveAt',
        'tenor': 'tenor',
        'roll_convention': 'rollConvention',
        'holiday_calendars': 'holidayCalendars',
        'valuation_date_times': 'valuationDateTimes'
    }

    required_map = {
        'effective_from': 'optional',
        'effective_at': 'required',
        'tenor': 'optional',
        'roll_convention': 'optional',
        'holiday_calendars': 'optional',
        'valuation_date_times': 'optional'
    }

    def __init__(self, effective_from=None, effective_at=None, tenor=None, roll_convention=None, holiday_calendars=None, valuation_date_times=None, local_vars_configuration=None):  # noqa: E501
        """ValuationSchedule - a model defined in OpenAPI"
        
        :param effective_from:  If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each business day in the given range.
        :type effective_from: str
        :param effective_at:  The market data time, i.e. the time to run the valuation request effective of. (required)
        :type effective_at: str
        :param tenor:  Tenor, e.g \"1D\", \"1M\" to be used in generating the date schedule when effectiveFrom and effectiveAt are both given and are not the same.
        :type tenor: str
        :param roll_convention:  When Tenor is given and is not equal to \"1D\", there may be cases where \"date + tenor\" land on non-business days around month end.  In that case, the RollConvention, e.g. modified following \"MF\" would be applied to determine the next GBD.
        :type roll_convention: str
        :param holiday_calendars:  The holiday calendar(s) that should be used in determining the date schedule.  Holiday calendar(s) are supplied by their names, for example, \"CoppClarke\".   Note that when the calendars are not available (e.g. when the user has insufficient permissions),   a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored.
        :type holiday_calendars: list[str]
        :param valuation_date_times:  If given, this is the exact set of dates on which to perform a valuation. This will replace/override all other specified values if given.
        :type valuation_date_times: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._effective_from = None
        self._effective_at = None
        self._tenor = None
        self._roll_convention = None
        self._holiday_calendars = None
        self._valuation_date_times = None
        self.discriminator = None

        self.effective_from = effective_from
        self.effective_at = effective_at
        self.tenor = tenor
        self.roll_convention = roll_convention
        self.holiday_calendars = holiday_calendars
        self.valuation_date_times = valuation_date_times

    @property
    def effective_from(self):
        """Gets the effective_from of this ValuationSchedule.  # noqa: E501

        If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each business day in the given range.  # noqa: E501

        :return: The effective_from of this ValuationSchedule.  # noqa: E501
        :rtype: str
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this ValuationSchedule.

        If present, the EffectiveFrom and EffectiveAt dates are interpreted as a range of dates for which to perform a valuation.  In this case, valuation is calculated for the portfolio(s) for each business day in the given range.  # noqa: E501

        :param effective_from: The effective_from of this ValuationSchedule.  # noqa: E501
        :type effective_from: str
        """

        self._effective_from = effective_from

    @property
    def effective_at(self):
        """Gets the effective_at of this ValuationSchedule.  # noqa: E501

        The market data time, i.e. the time to run the valuation request effective of.  # noqa: E501

        :return: The effective_at of this ValuationSchedule.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this ValuationSchedule.

        The market data time, i.e. the time to run the valuation request effective of.  # noqa: E501

        :param effective_at: The effective_at of this ValuationSchedule.  # noqa: E501
        :type effective_at: str
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def tenor(self):
        """Gets the tenor of this ValuationSchedule.  # noqa: E501

        Tenor, e.g \"1D\", \"1M\" to be used in generating the date schedule when effectiveFrom and effectiveAt are both given and are not the same.  # noqa: E501

        :return: The tenor of this ValuationSchedule.  # noqa: E501
        :rtype: str
        """
        return self._tenor

    @tenor.setter
    def tenor(self, tenor):
        """Sets the tenor of this ValuationSchedule.

        Tenor, e.g \"1D\", \"1M\" to be used in generating the date schedule when effectiveFrom and effectiveAt are both given and are not the same.  # noqa: E501

        :param tenor: The tenor of this ValuationSchedule.  # noqa: E501
        :type tenor: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tenor is not None and len(tenor) > 16):
            raise ValueError("Invalid value for `tenor`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenor is not None and len(tenor) < 0):
            raise ValueError("Invalid value for `tenor`, length must be greater than or equal to `0`")  # noqa: E501

        self._tenor = tenor

    @property
    def roll_convention(self):
        """Gets the roll_convention of this ValuationSchedule.  # noqa: E501

        When Tenor is given and is not equal to \"1D\", there may be cases where \"date + tenor\" land on non-business days around month end.  In that case, the RollConvention, e.g. modified following \"MF\" would be applied to determine the next GBD.  # noqa: E501

        :return: The roll_convention of this ValuationSchedule.  # noqa: E501
        :rtype: str
        """
        return self._roll_convention

    @roll_convention.setter
    def roll_convention(self, roll_convention):
        """Sets the roll_convention of this ValuationSchedule.

        When Tenor is given and is not equal to \"1D\", there may be cases where \"date + tenor\" land on non-business days around month end.  In that case, the RollConvention, e.g. modified following \"MF\" would be applied to determine the next GBD.  # noqa: E501

        :param roll_convention: The roll_convention of this ValuationSchedule.  # noqa: E501
        :type roll_convention: str
        """
        if (self.local_vars_configuration.client_side_validation and
                roll_convention is not None and len(roll_convention) > 16):
            raise ValueError("Invalid value for `roll_convention`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                roll_convention is not None and len(roll_convention) < 0):
            raise ValueError("Invalid value for `roll_convention`, length must be greater than or equal to `0`")  # noqa: E501

        self._roll_convention = roll_convention

    @property
    def holiday_calendars(self):
        """Gets the holiday_calendars of this ValuationSchedule.  # noqa: E501

        The holiday calendar(s) that should be used in determining the date schedule.  Holiday calendar(s) are supplied by their names, for example, \"CoppClarke\".   Note that when the calendars are not available (e.g. when the user has insufficient permissions),   a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored.  # noqa: E501

        :return: The holiday_calendars of this ValuationSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._holiday_calendars

    @holiday_calendars.setter
    def holiday_calendars(self, holiday_calendars):
        """Sets the holiday_calendars of this ValuationSchedule.

        The holiday calendar(s) that should be used in determining the date schedule.  Holiday calendar(s) are supplied by their names, for example, \"CoppClarke\".   Note that when the calendars are not available (e.g. when the user has insufficient permissions),   a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored.  # noqa: E501

        :param holiday_calendars: The holiday_calendars of this ValuationSchedule.  # noqa: E501
        :type holiday_calendars: list[str]
        """

        self._holiday_calendars = holiday_calendars

    @property
    def valuation_date_times(self):
        """Gets the valuation_date_times of this ValuationSchedule.  # noqa: E501

        If given, this is the exact set of dates on which to perform a valuation. This will replace/override all other specified values if given.  # noqa: E501

        :return: The valuation_date_times of this ValuationSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._valuation_date_times

    @valuation_date_times.setter
    def valuation_date_times(self, valuation_date_times):
        """Sets the valuation_date_times of this ValuationSchedule.

        If given, this is the exact set of dates on which to perform a valuation. This will replace/override all other specified values if given.  # noqa: E501

        :param valuation_date_times: The valuation_date_times of this ValuationSchedule.  # noqa: E501
        :type valuation_date_times: list[str]
        """

        self._valuation_date_times = valuation_date_times

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
        if not isinstance(other, ValuationSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValuationSchedule):
            return True

        return self.to_dict() != other.to_dict()
