from sleekxmpp.stanza import Error
from sleekxmpp.xmlstream import ElementBase, ET, register_stanza_plugin

JINGLE_NAMESPACE = 'urn:xmpp:jingle:1'

JINGLE_ERRORS_NAMESPACE = 'urn:xmpp:jingle:errors:1'


class Jingle(ElementBase):
    namespace = JINGLE_NAMESPACE
    name = 'jingle'
    plugin_attrib = name
    interfaces = (('action', 'initiator',
                   'responder', 'sid'))


class JingleError(Error):
    plugin_attrib = 'jingleError'
    conditions = (('unknown-session', 'unsupported-info', 'tie-break', 'out-of-order'))
    condition_ns = JINGLE_ERRORS_NAMESPACE


class Content(ElementBase):
    namespace = JINGLE_NAMESPACE
    name = 'content'
    plugin_attrib = name
    interfaces = (('creator', 'disposition',
                   'name', 'senders'))


class Reason(ElementBase):
    namespace = JINGLE_NAMESPACE
    name = 'reason'
    plugin_attrib = name
    interfaces = (('text',))
    sub_interfaces = (('text',))
