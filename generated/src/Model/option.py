# coding: utf-8

"""
    Adobe Target Delivery API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Option(object):
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
    """
    openapi_types = {
        'type': 'OptionType',
        'content': 'OneOfstringobjectarray',
        'event_token': 'str',
        'response_tokens': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'type',
        'content': 'content',
        'event_token': 'eventToken',
        'response_tokens': 'responseTokens'
    }

    def __init__(self, type=None, content=None, event_token=None, response_tokens=None):  # noqa: E501
        """Option - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._content = None
        self._event_token = None
        self._response_tokens = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if content is not None:
            self.content = content
        if event_token is not None:
            self.event_token = event_token
        if response_tokens is not None:
            self.response_tokens = response_tokens

    @property
    def type(self):
        """Gets the type of this Option.  # noqa: E501


        :return: The type of this Option.  # noqa: E501
        :rtype: OptionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Option.


        :param type: The type of this Option.  # noqa: E501
        :type: OptionType
        """

        self._type = type

    @property
    def content(self):
        """Gets the content of this Option.  # noqa: E501

        Content that should be applied/displayed/replaced etc, based on the option type. Content can be one of:   * html   * redirect link   * link for a dynamic offer   * raw json   * one or more actions (json - from offers with templates and visual offers) Actions format is specific for delivery API.   # noqa: E501

        :return: The content of this Option.  # noqa: E501
        :rtype: OneOfstringobjectarray
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Option.

        Content that should be applied/displayed/replaced etc, based on the option type. Content can be one of:   * html   * redirect link   * link for a dynamic offer   * raw json   * one or more actions (json - from offers with templates and visual offers) Actions format is specific for delivery API.   # noqa: E501

        :param content: The content of this Option.  # noqa: E501
        :type: OneOfstringobjectarray
        """

        self._content = content

    @property
    def event_token(self):
        """Gets the event_token of this Option.  # noqa: E501

        Will be present only in response of a prefetch request. After the content is displayed the event token should be sent via notifications to the edge server so that visit/visitor/impression events could be logged.   # noqa: E501

        :return: The event_token of this Option.  # noqa: E501
        :rtype: str
        """
        return self._event_token

    @event_token.setter
    def event_token(self, event_token):
        """Sets the event_token of this Option.

        Will be present only in response of a prefetch request. After the content is displayed the event token should be sent via notifications to the edge server so that visit/visitor/impression events could be logged.   # noqa: E501

        :param event_token: The event_token of this Option.  # noqa: E501
        :type: str
        """

        self._event_token = event_token

    @property
    def response_tokens(self):
        """Gets the response_tokens of this Option.  # noqa: E501

        List of the response tokens and their values for the given option. Response tokens can be defined via the /v1/responsetokens API. The values for the tokens are computed for every option returned by a activity and represented as a dictionary:   * Key - the response token name.   * Value - the response token value. The value is usually a string, but it can be a list of string in case of   'category affinity' response token.   # noqa: E501

        :return: The response_tokens of this Option.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._response_tokens

    @response_tokens.setter
    def response_tokens(self, response_tokens):
        """Sets the response_tokens of this Option.

        List of the response tokens and their values for the given option. Response tokens can be defined via the /v1/responsetokens API. The values for the tokens are computed for every option returned by a activity and represented as a dictionary:   * Key - the response token name.   * Value - the response token value. The value is usually a string, but it can be a list of string in case of   'category affinity' response token.   # noqa: E501

        :param response_tokens: The response_tokens of this Option.  # noqa: E501
        :type: dict(str, object)
        """

        self._response_tokens = response_tokens

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Option):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
