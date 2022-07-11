# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4580
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


class LusidValidationProblemDetails(object):
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
        'name': 'str',
        'error_details': 'list[dict(str, str)]',
        'code': 'int',
        'errors': 'dict(str, list[str])',
        'type': 'str',
        'title': 'str',
        'status': 'int',
        'detail': 'str',
        'instance': 'str',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'error_details': 'errorDetails',
        'code': 'code',
        'errors': 'errors',
        'type': 'type',
        'title': 'title',
        'status': 'status',
        'detail': 'detail',
        'instance': 'instance',
        'extensions': 'extensions'
    }

    required_map = {
        'name': 'required',
        'error_details': 'optional',
        'code': 'required',
        'errors': 'optional',
        'type': 'optional',
        'title': 'optional',
        'status': 'optional',
        'detail': 'optional',
        'instance': 'optional',
        'extensions': 'optional'
    }

    def __init__(self, name=None, error_details=None, code=None, errors=None, type=None, title=None, status=None, detail=None, instance=None, extensions=None, local_vars_configuration=None):  # noqa: E501
        """LusidValidationProblemDetails - a model defined in OpenAPI"
        
        :param name:  The name of the error (required)
        :type name: str
        :param error_details:  Any additional informational information available about the nature and detail of the problem
        :type error_details: list[dict(str, str)]
        :param code:  Get the error code of the response (required)
        :type code: int
        :param errors: 
        :type errors: dict(str, list[str])
        :param type: 
        :type type: str
        :param title: 
        :type title: str
        :param status: 
        :type status: int
        :param detail: 
        :type detail: str
        :param instance: 
        :type instance: str
        :param extensions: 
        :type extensions: dict(str, object)

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._error_details = None
        self._code = None
        self._errors = None
        self._type = None
        self._title = None
        self._status = None
        self._detail = None
        self._instance = None
        self._extensions = None
        self.discriminator = None

        self.name = name
        self.error_details = error_details
        self.code = code
        self.errors = errors
        self.type = type
        self.title = title
        self.status = status
        self.detail = detail
        self.instance = instance
        self.extensions = extensions

    @property
    def name(self):
        """Gets the name of this LusidValidationProblemDetails.  # noqa: E501

        The name of the error  # noqa: E501

        :return: The name of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LusidValidationProblemDetails.

        The name of the error  # noqa: E501

        :param name: The name of this LusidValidationProblemDetails.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def error_details(self):
        """Gets the error_details of this LusidValidationProblemDetails.  # noqa: E501

        Any additional informational information available about the nature and detail of the problem  # noqa: E501

        :return: The error_details of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this LusidValidationProblemDetails.

        Any additional informational information available about the nature and detail of the problem  # noqa: E501

        :param error_details: The error_details of this LusidValidationProblemDetails.  # noqa: E501
        :type error_details: list[dict(str, str)]
        """

        self._error_details = error_details

    @property
    def code(self):
        """Gets the code of this LusidValidationProblemDetails.  # noqa: E501

        Get the error code of the response  # noqa: E501

        :return: The code of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LusidValidationProblemDetails.

        Get the error code of the response  # noqa: E501

        :param code: The code of this LusidValidationProblemDetails.  # noqa: E501
        :type code: int
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def errors(self):
        """Gets the errors of this LusidValidationProblemDetails.  # noqa: E501


        :return: The errors of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this LusidValidationProblemDetails.


        :param errors: The errors of this LusidValidationProblemDetails.  # noqa: E501
        :type errors: dict(str, list[str])
        """

        self._errors = errors

    @property
    def type(self):
        """Gets the type of this LusidValidationProblemDetails.  # noqa: E501


        :return: The type of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LusidValidationProblemDetails.


        :param type: The type of this LusidValidationProblemDetails.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this LusidValidationProblemDetails.  # noqa: E501


        :return: The title of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LusidValidationProblemDetails.


        :param title: The title of this LusidValidationProblemDetails.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this LusidValidationProblemDetails.  # noqa: E501


        :return: The status of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LusidValidationProblemDetails.


        :param status: The status of this LusidValidationProblemDetails.  # noqa: E501
        :type status: int
        """

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this LusidValidationProblemDetails.  # noqa: E501


        :return: The detail of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this LusidValidationProblemDetails.


        :param detail: The detail of this LusidValidationProblemDetails.  # noqa: E501
        :type detail: str
        """

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this LusidValidationProblemDetails.  # noqa: E501


        :return: The instance of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this LusidValidationProblemDetails.


        :param instance: The instance of this LusidValidationProblemDetails.  # noqa: E501
        :type instance: str
        """

        self._instance = instance

    @property
    def extensions(self):
        """Gets the extensions of this LusidValidationProblemDetails.  # noqa: E501


        :return: The extensions of this LusidValidationProblemDetails.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this LusidValidationProblemDetails.


        :param extensions: The extensions of this LusidValidationProblemDetails.  # noqa: E501
        :type extensions: dict(str, object)
        """

        self._extensions = extensions

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
        if not isinstance(other, LusidValidationProblemDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LusidValidationProblemDetails):
            return True

        return self.to_dict() != other.to_dict()
