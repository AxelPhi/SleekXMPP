import logging

from sleekxmpp import Iq
from sleekxmpp.plugins.base import BasePlugin
from sleekxmpp.plugins.xep_0166 import stanza
from sleekxmpp.plugins.xep_0166.exceptions import JingleException, UnkownJingleSession
from sleekxmpp.plugins.xep_0166.stanza import Jingle, Content, Reason, JingleErrorCondition
from sleekxmpp.plugins.xep_0166.stanza.errors import UnknownSession
from sleekxmpp.plugins.xep_0166.stanza.reasons import reason_elements
from sleekxmpp.stanza import Error
from sleekxmpp.xmlstream import register_stanza_plugin
from sleekxmpp.xmlstream.handler import Callback
from sleekxmpp.xmlstream.matcher import StanzaPath

log = logging.getLogger(__name__)

JINGLE_ACTIONS = {
    'content-accept': None,
    'content-add': None,
    'content-modify': None,
    'content-reject': None,
    'content-remove': None,
    'description-info': None,
    'security-info': None,
    'session-accept': None,
    'session-info': None,
    'session-initiate': None,
    'session-terminate': None,
    'transport-accept': None,
    'transport-info': None,
    'transport-reject': None,
    'transport-replace': None
}


class XEP_0166(BasePlugin):
    """
    XEP-0166: Jingle
    """

    name = 'xep_0166'
    description = 'XEP-0166: Jingle'
    dependencies = set(['xep_0020', 'xep_0030'])
    stanza = stanza

    def plugin_init(self):
        # register stanzas

        self.xmpp.registerHandler(
            Callback('Jingle Session Handling',
                     StanzaPath('iq/jingle'),
                     self._handle_jingle_stanza))

        register_stanza_plugin(Iq, Jingle)
        register_stanza_plugin(Jingle, Content)
        register_stanza_plugin(Jingle, Reason)
        for reason_element in reason_elements:
            register_stanza_plugin(Reason, reason_element)

        self._sessions = {}

    def plugin_end(self):
        # cleanup
        pass

    def session_bind(self, jid):
        # bind features to sessions
        pass

    def _handle_jingle_stanza(self, iq):
        jingle = iq['jingle']
        log.debug('Incoming Jingle Stanza: {}'.format(jingle))
        session_id = jingle['sid']
        try:
            raise UnkownJingleSession(session_id)
        except UnkownJingleSession as exc:
            iq.reply(True)
            iq['error'] = UnknownSession()

        iq.send()


