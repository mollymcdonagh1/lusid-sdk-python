# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4245
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


class CreatePortfolioGroupRequest(object):
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
        'code': 'str',
        'created': 'datetime',
        'values': 'list[ResourceId]',
        'sub_groups': 'list[ResourceId]',
        'properties': 'dict(str, ModelProperty)',
        'display_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'code': 'code',
        'created': 'created',
        'values': 'values',
        'sub_groups': 'subGroups',
        'properties': 'properties',
        'display_name': 'displayName',
        'description': 'description'
    }

    required_map = {
        'code': 'required',
        'created': 'optional',
        'values': 'optional',
        'sub_groups': 'optional',
        'properties': 'optional',
        'display_name': 'required',
        'description': 'optional'
    }

    def __init__(self, code=None, created=None, values=None, sub_groups=None, properties=None, display_name=None, description=None, local_vars_configuration=None):  # noqa: E501
        """CreatePortfolioGroupRequest - a model defined in OpenAPI"
        
        :param code:  The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group. (required)
        :type code: str
        :param created:  The effective datetime at which the portfolio group was created. Defaults to the current LUSID system datetime if not specified.
        :type created: datetime
        :param values:  The resource identifiers of the portfolios to be contained within the portfolio group.
        :type values: list[lusid.ResourceId]
        :param sub_groups:  The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups.
        :type sub_groups: list[lusid.ResourceId]
        :param properties:  A set of unique group properties to add to the portfolio group. Each property must be from the 'PortfolioGroup' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'PortfolioGroup/Manager/Id'. These properties must be pre-defined.
        :type properties: dict[str, lusid.ModelProperty]
        :param display_name:  The name of the portfolio group. (required)
        :type display_name: str
        :param description:  A long form description of the portfolio group.
        :type description: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._created = None
        self._values = None
        self._sub_groups = None
        self._properties = None
        self._display_name = None
        self._description = None
        self.discriminator = None

        self.code = code
        self.created = created
        self.values = values
        self.sub_groups = sub_groups
        self.properties = properties
        self.display_name = display_name
        self.description = description

    @property
    def code(self):
        """Gets the code of this CreatePortfolioGroupRequest.  # noqa: E501

        The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group.  # noqa: E501

        :return: The code of this CreatePortfolioGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreatePortfolioGroupRequest.

        The code that the portfolio group will be created with. Together with the scope this uniquely identifies the portfolio group.  # noqa: E501

        :param code: The code of this CreatePortfolioGroupRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def created(self):
        """Gets the created of this CreatePortfolioGroupRequest.  # noqa: E501

        The effective datetime at which the portfolio group was created. Defaults to the current LUSID system datetime if not specified.  # noqa: E501

        :return: The created of this CreatePortfolioGroupRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CreatePortfolioGroupRequest.

        The effective datetime at which the portfolio group was created. Defaults to the current LUSID system datetime if not specified.  # noqa: E501

        :param created: The created of this CreatePortfolioGroupRequest.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def values(self):
        """Gets the values of this CreatePortfolioGroupRequest.  # noqa: E501

        The resource identifiers of the portfolios to be contained within the portfolio group.  # noqa: E501

        :return: The values of this CreatePortfolioGroupRequest.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this CreatePortfolioGroupRequest.

        The resource identifiers of the portfolios to be contained within the portfolio group.  # noqa: E501

        :param values: The values of this CreatePortfolioGroupRequest.  # noqa: E501
        :type values: list[lusid.ResourceId]
        """

        self._values = values

    @property
    def sub_groups(self):
        """Gets the sub_groups of this CreatePortfolioGroupRequest.  # noqa: E501

        The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups.  # noqa: E501

        :return: The sub_groups of this CreatePortfolioGroupRequest.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._sub_groups

    @sub_groups.setter
    def sub_groups(self, sub_groups):
        """Sets the sub_groups of this CreatePortfolioGroupRequest.

        The resource identifiers of the portfolio groups to be contained within the portfolio group as sub groups.  # noqa: E501

        :param sub_groups: The sub_groups of this CreatePortfolioGroupRequest.  # noqa: E501
        :type sub_groups: list[lusid.ResourceId]
        """

        self._sub_groups = sub_groups

    @property
    def properties(self):
        """Gets the properties of this CreatePortfolioGroupRequest.  # noqa: E501

        A set of unique group properties to add to the portfolio group. Each property must be from the 'PortfolioGroup' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'PortfolioGroup/Manager/Id'. These properties must be pre-defined.  # noqa: E501

        :return: The properties of this CreatePortfolioGroupRequest.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreatePortfolioGroupRequest.

        A set of unique group properties to add to the portfolio group. Each property must be from the 'PortfolioGroup' domain and should be identified by its key which has the format {domain}/{scope}/{code}, e.g. 'PortfolioGroup/Manager/Id'. These properties must be pre-defined.  # noqa: E501

        :param properties: The properties of this CreatePortfolioGroupRequest.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def display_name(self):
        """Gets the display_name of this CreatePortfolioGroupRequest.  # noqa: E501

        The name of the portfolio group.  # noqa: E501

        :return: The display_name of this CreatePortfolioGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreatePortfolioGroupRequest.

        The name of the portfolio group.  # noqa: E501

        :param display_name: The display_name of this CreatePortfolioGroupRequest.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CreatePortfolioGroupRequest.  # noqa: E501

        A long form description of the portfolio group.  # noqa: E501

        :return: The description of this CreatePortfolioGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreatePortfolioGroupRequest.

        A long form description of the portfolio group.  # noqa: E501

        :param description: The description of this CreatePortfolioGroupRequest.  # noqa: E501
        :type description: str
        """

        self._description = description

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
        if not isinstance(other, CreatePortfolioGroupRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreatePortfolioGroupRequest):
            return True

        return self.to_dict() != other.to_dict()
