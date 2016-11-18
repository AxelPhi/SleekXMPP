from sleekxmpp import ElementBase
from sleekxmpp import register_stanza_plugin
from sleekxmpp.stanza import Error

JINGLE_ERRORS_NAMESPACE = 'urn:xmpp:jingle:errors:1'


class OutOfOrder(ElementBase):
    namespace = JINGLE_ERRORS_NAMESPACE
    name = 'out-of-order'
    plugin_attrib = name


class TieBreak(ElementBase):
    namespace = JINGLE_ERRORS_NAMESPACE
    name = 'tie-break'
    plugin_attrib = name


class UnknownSession(Error):
    name = 'error-name'
    plugin_attrib = 'error-attrib'
    conditions = (('unknown-session'))
    condition_ns =  JINGLE_ERRORS_NAMESPACE

class UnsupportedInfo(ElementBase):
    namespace = JINGLE_ERRORS_NAMESPACE
    name = 'unsupported-info'
    plugin_attrib = name

#
# jingle_errors = [OutOfOrder, TieBreak, UnknownSession, UnsupportedInfo]
# for jingle_error in jingle_errors:
#     register_stanza_plugin(Error, jingle_error)
