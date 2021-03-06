# coding: utf-8

"""
    Python InsightVM API Client

    OpenAPI spec version: 3
    Contact: support@rapid7.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rapid7vmconsole.models.link import Link  # noqa: F401,E501
from rapid7vmconsole.models.operating_system import OperatingSystem  # noqa: F401,E501


class PolicyAsset(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'hostname': 'str',
        'id': 'int',
        'ip': 'str',
        'links': 'list[Link]',
        'os': 'OperatingSystem',
        'status': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'id': 'id',
        'ip': 'ip',
        'links': 'links',
        'os': 'os',
        'status': 'status'
    }

    def __init__(self, hostname=None, id=None, ip=None, links=None, os=None, status=None):  # noqa: E501
        """PolicyAsset - a model defined in Swagger"""  # noqa: E501

        self._hostname = None
        self._id = None
        self._ip = None
        self._links = None
        self._os = None
        self._status = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if links is not None:
            self.links = links
        if os is not None:
            self.os = os
        if status is not None:
            self.status = status

    @property
    def hostname(self):
        """Gets the hostname of this PolicyAsset.  # noqa: E501

        The primary host name (local or FQDN) of the asset.  # noqa: E501

        :return: The hostname of this PolicyAsset.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this PolicyAsset.

        The primary host name (local or FQDN) of the asset.  # noqa: E501

        :param hostname: The hostname of this PolicyAsset.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this PolicyAsset.  # noqa: E501

        The identifier of the asset.  # noqa: E501

        :return: The id of this PolicyAsset.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyAsset.

        The identifier of the asset.  # noqa: E501

        :param id: The id of this PolicyAsset.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ip(self):
        """Gets the ip of this PolicyAsset.  # noqa: E501

        The primary IPv4 or IPv6 address of the asset.  # noqa: E501

        :return: The ip of this PolicyAsset.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this PolicyAsset.

        The primary IPv4 or IPv6 address of the asset.  # noqa: E501

        :param ip: The ip of this PolicyAsset.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def links(self):
        """Gets the links of this PolicyAsset.  # noqa: E501

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :return: The links of this PolicyAsset.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyAsset.

        Hypermedia links to corresponding or related resources.  # noqa: E501

        :param links: The links of this PolicyAsset.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def os(self):
        """Gets the os of this PolicyAsset.  # noqa: E501

        The full description of the operating system of the asset.  # noqa: E501

        :return: The os of this PolicyAsset.  # noqa: E501
        :rtype: OperatingSystem
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this PolicyAsset.

        The full description of the operating system of the asset.  # noqa: E501

        :param os: The os of this PolicyAsset.  # noqa: E501
        :type: OperatingSystem
        """

        self._os = os

    @property
    def status(self):
        """Gets the status of this PolicyAsset.  # noqa: E501

        The overall compliance status of the asset.   # noqa: E501

        :return: The status of this PolicyAsset.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PolicyAsset.

        The overall compliance status of the asset.   # noqa: E501

        :param status: The status of this PolicyAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["PASS", "FAIL", "NOT_APPLICABLE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(PolicyAsset, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyAsset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
