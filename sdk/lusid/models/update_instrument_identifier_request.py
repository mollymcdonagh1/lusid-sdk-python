# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3749
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


class UpdateInstrumentIdentifierRequest(object):
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
        'type': 'str',
        'value': 'str',
        'effective_at': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'effective_at': 'effectiveAt'
    }

    required_map = {
        'type': 'required',
        'value': 'optional',
        'effective_at': 'optional'
    }

    def __init__(self, type=None, value=None, effective_at=None, local_vars_configuration=None):  # noqa: E501
        """UpdateInstrumentIdentifierRequest - a model defined in OpenAPI"
        
        :param type:  The allowable instrument identifier to update, insert or remove e.g. 'Figi'. (required)
        :type type: str
        :param value:  The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument.
        :type value: str
        :param effective_at:  The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified.
        :type effective_at: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._value = None
        self._effective_at = None
        self.discriminator = None

        self.type = type
        self.value = value
        self.effective_at = effective_at

    @property
    def type(self):
        """Gets the type of this UpdateInstrumentIdentifierRequest.  # noqa: E501

        The allowable instrument identifier to update, insert or remove e.g. 'Figi'.  # noqa: E501

        :return: The type of this UpdateInstrumentIdentifierRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateInstrumentIdentifierRequest.

        The allowable instrument identifier to update, insert or remove e.g. 'Figi'.  # noqa: E501

        :param type: The type of this UpdateInstrumentIdentifierRequest.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this UpdateInstrumentIdentifierRequest.  # noqa: E501

        The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument.  # noqa: E501

        :return: The value of this UpdateInstrumentIdentifierRequest.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateInstrumentIdentifierRequest.

        The new value of the allowable instrument identifier. If unspecified the identifier will be removed from the instrument.  # noqa: E501

        :param value: The value of this UpdateInstrumentIdentifierRequest.  # noqa: E501
        :type value: str
        """

        self._value = value

    @property
    def effective_at(self):
        """Gets the effective_at of this UpdateInstrumentIdentifierRequest.  # noqa: E501

        The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified.  # noqa: E501

        :return: The effective_at of this UpdateInstrumentIdentifierRequest.  # noqa: E501
        :rtype: str
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this UpdateInstrumentIdentifierRequest.

        The effective datetime from which the identifier should be updated, inserted or removed. Defaults to the current LUSID system datetime if not specified.  # noqa: E501

        :param effective_at: The effective_at of this UpdateInstrumentIdentifierRequest.  # noqa: E501
        :type effective_at: str
        """

        self._effective_at = effective_at

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
        if not isinstance(other, UpdateInstrumentIdentifierRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateInstrumentIdentifierRequest):
            return True

        return self.to_dict() != other.to_dict()
