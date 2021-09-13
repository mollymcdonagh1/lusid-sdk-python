# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3478
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


class ModelProperty(object):
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
        'key': 'str',
        'value': 'PropertyValue',
        'effective_from': 'datetime',
        'effective_until': 'datetime'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'effective_from': 'effectiveFrom',
        'effective_until': 'effectiveUntil'
    }

    required_map = {
        'key': 'required',
        'value': 'optional',
        'effective_from': 'optional',
        'effective_until': 'optional'
    }

    def __init__(self, key=None, value=None, effective_from=None, effective_until=None, local_vars_configuration=None):  # noqa: E501
        """ModelProperty - a model defined in OpenAPI"
        
        :param key:  The key of the property. This takes the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or 'Transaction/strategy/quantsignal'. (required)
        :type key: str
        :param value: 
        :type value: lusid.PropertyValue
        :param effective_from:  The effective datetime from which the property is valid.
        :type effective_from: datetime
        :param effective_until:  The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveFrom' datetime of the property.
        :type effective_until: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._value = None
        self._effective_from = None
        self._effective_until = None
        self.discriminator = None

        self.key = key
        if value is not None:
            self.value = value
        self.effective_from = effective_from
        self.effective_until = effective_until

    @property
    def key(self):
        """Gets the key of this ModelProperty.  # noqa: E501

        The key of the property. This takes the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or 'Transaction/strategy/quantsignal'.  # noqa: E501

        :return: The key of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ModelProperty.

        The key of the property. This takes the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or 'Transaction/strategy/quantsignal'.  # noqa: E501

        :param key: The key of this ModelProperty.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this ModelProperty.  # noqa: E501


        :return: The value of this ModelProperty.  # noqa: E501
        :rtype: lusid.PropertyValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ModelProperty.


        :param value: The value of this ModelProperty.  # noqa: E501
        :type value: lusid.PropertyValue
        """

        self._value = value

    @property
    def effective_from(self):
        """Gets the effective_from of this ModelProperty.  # noqa: E501

        The effective datetime from which the property is valid.  # noqa: E501

        :return: The effective_from of this ModelProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_from

    @effective_from.setter
    def effective_from(self, effective_from):
        """Sets the effective_from of this ModelProperty.

        The effective datetime from which the property is valid.  # noqa: E501

        :param effective_from: The effective_from of this ModelProperty.  # noqa: E501
        :type effective_from: datetime
        """

        self._effective_from = effective_from

    @property
    def effective_until(self):
        """Gets the effective_until of this ModelProperty.  # noqa: E501

        The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveFrom' datetime of the property.  # noqa: E501

        :return: The effective_until of this ModelProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_until

    @effective_until.setter
    def effective_until(self, effective_until):
        """Sets the effective_until of this ModelProperty.

        The effective datetime until which the property is valid. If not supplied this will be valid indefinitely, or until the next 'effectiveFrom' datetime of the property.  # noqa: E501

        :param effective_until: The effective_until of this ModelProperty.  # noqa: E501
        :type effective_until: datetime
        """

        self._effective_until = effective_until

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
        if not isinstance(other, ModelProperty):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelProperty):
            return True

        return self.to_dict() != other.to_dict()
