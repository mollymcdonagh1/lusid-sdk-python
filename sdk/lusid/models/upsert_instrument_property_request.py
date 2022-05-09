# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4309
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


class UpsertInstrumentPropertyRequest(object):
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
        'identifier_type': 'str',
        'identifier': 'str',
        'properties': 'list[ModelProperty]'
    }

    attribute_map = {
        'identifier_type': 'identifierType',
        'identifier': 'identifier',
        'properties': 'properties'
    }

    required_map = {
        'identifier_type': 'required',
        'identifier': 'required',
        'properties': 'optional'
    }

    def __init__(self, identifier_type=None, identifier=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """UpsertInstrumentPropertyRequest - a model defined in OpenAPI"
        
        :param identifier_type:  The unique identifier type to search for the instrument, for example 'Figi'. (required)
        :type identifier_type: str
        :param identifier:  A value of that type to identify the instrument to upsert properties for, for example 'BBG000BLNNV0'. (required)
        :type identifier: str
        :param properties:  A set of instrument properties and associated values to store for the instrument. Each property must be from the 'Instrument' domain.
        :type properties: list[lusid.ModelProperty]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._identifier_type = None
        self._identifier = None
        self._properties = None
        self.discriminator = None

        self.identifier_type = identifier_type
        self.identifier = identifier
        self.properties = properties

    @property
    def identifier_type(self):
        """Gets the identifier_type of this UpsertInstrumentPropertyRequest.  # noqa: E501

        The unique identifier type to search for the instrument, for example 'Figi'.  # noqa: E501

        :return: The identifier_type of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier_type

    @identifier_type.setter
    def identifier_type(self, identifier_type):
        """Sets the identifier_type of this UpsertInstrumentPropertyRequest.

        The unique identifier type to search for the instrument, for example 'Figi'.  # noqa: E501

        :param identifier_type: The identifier_type of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :type identifier_type: str
        """
        if self.local_vars_configuration.client_side_validation and identifier_type is None:  # noqa: E501
            raise ValueError("Invalid value for `identifier_type`, must not be `None`")  # noqa: E501

        self._identifier_type = identifier_type

    @property
    def identifier(self):
        """Gets the identifier of this UpsertInstrumentPropertyRequest.  # noqa: E501

        A value of that type to identify the instrument to upsert properties for, for example 'BBG000BLNNV0'.  # noqa: E501

        :return: The identifier of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this UpsertInstrumentPropertyRequest.

        A value of that type to identify the instrument to upsert properties for, for example 'BBG000BLNNV0'.  # noqa: E501

        :param identifier: The identifier of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :type identifier: str
        """
        if self.local_vars_configuration.client_side_validation and identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def properties(self):
        """Gets the properties of this UpsertInstrumentPropertyRequest.  # noqa: E501

        A set of instrument properties and associated values to store for the instrument. Each property must be from the 'Instrument' domain.  # noqa: E501

        :return: The properties of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :rtype: list[lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpsertInstrumentPropertyRequest.

        A set of instrument properties and associated values to store for the instrument. Each property must be from the 'Instrument' domain.  # noqa: E501

        :param properties: The properties of this UpsertInstrumentPropertyRequest.  # noqa: E501
        :type properties: list[lusid.ModelProperty]
        """

        self._properties = properties

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
        if not isinstance(other, UpsertInstrumentPropertyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertInstrumentPropertyRequest):
            return True

        return self.to_dict() != other.to_dict()
