from sleekxmpp.xmlstream import ElementBase


class AlternativeSession(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'alternative-session'
    plugin_attrib = name
    interfaces = (('sid'),)
    sub_interfaces = (('sid'),)


class Busy(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'busy'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class Cancel(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'cancel'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class ConnectivityError(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'connectivity-error'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class Decline(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'decline'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class Expired(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'expired'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class FailedApplication(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'failed-application'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class FailedTransport(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'failed-transport'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class GeneralError(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'general-error'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class Gone(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'gone'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class IncompatibleParameters(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'incompatible-parameters'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class MediaError(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'media-error'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class SecurityError(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'security-error'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class Success(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'success'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class Timeout(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'timeout'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class UnsupportedApplications(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'unsupported-applications'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


class UnsupportedTransports(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'unsupported-transports'
    plugin_attrib = name
    interfaces = ()
    sub_interfaces = ()


reason_elements = [
    AlternativeSession, Busy, Cancel,
    ConnectivityError, Decline, Expired, FailedApplication,
    FailedTransport, GeneralError, Gone, IncompatibleParameters,
    MediaError, SecurityError, Success, Timeout,
    UnsupportedApplications, UnsupportedTransports
]
