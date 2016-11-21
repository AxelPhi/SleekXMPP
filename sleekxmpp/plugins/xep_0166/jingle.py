from datetime import datetime
import logging
from uuid import uuid1

from sleekxmpp import Iq
from sleekxmpp.plugins.base import BasePlugin
from sleekxmpp.plugins.xep_0166 import stanza
from sleekxmpp.plugins.xep_0166.exceptions import JingleException, UnknownSession, DuplicateSession, OutOfOrder
from sleekxmpp.plugins.xep_0166.stanza import Jingle, Content, Reason
from sleekxmpp.plugins.xep_0166.stanza import JingleError
from sleekxmpp.plugins.xep_0166.stanza.reasons import reason_elements
from sleekxmpp.xmlstream import register_stanza_plugin
from sleekxmpp.xmlstream.handler import Callback
from sleekxmpp.xmlstream.matcher import StanzaPath

log = logging.getLogger(__name__)

# Session states
PENDING = 'pending'
ACTIVE = 'active'
ENDED = 'ended'

# Jingle action constants
ACTION_SESSION_ACCEPT = 'session-accept'
ACTION_SESSION_INITIATE = 'session-initiate'
ACTION_SESSION_TERMINATE = 'session-terminate'

# Event names
EVENT_SESSION_REQUEST = 'jingle-session-request'


class JingleSession(object):
    def __init__(self, plugin, session_id, initiator, responder):
        self.plugin = plugin
        self.session_id = session_id
        self.initiator = initiator
        self.responder = responder
        self.created_at = datetime.now()
        self.last_action_at = self.created_at
        self.state = PENDING

    def accept(self):
        pass

    def accepted(self):
        if not self.state == PENDING:
            raise OutOfOrder(self.session_id)
        self.state = ACTIVE
        self.last_action_at = datetime.now()


class XEP_0166(BasePlugin):
    """
    XEP-0166: Jingle
    """

    name = 'xep_0166'
    description = 'XEP-0166: Jingle'
    dependencies = set(['xep_0020', 'xep_0030'])
    stanza = stanza

    def plugin_init(self):

        register_stanza_plugin(Iq, Jingle)
        register_stanza_plugin(Iq, JingleError)
        register_stanza_plugin(Jingle, Content)
        register_stanza_plugin(Jingle, Reason)
        for reason_element in reason_elements:
            register_stanza_plugin(Reason, reason_element)

        self.xmpp.registerHandler(
            Callback('Jingle Session Handling',
                     StanzaPath('iq/jingle'),
                     self._handle_jingle_stanza))

        self._sessions = {}
        self._content_handlers = {}
        self._transport_handlers = {}

        self._jingle_actions = {
            'content-accept': None,
            'content-add': None,
            'content-modify': None,
            'content-reject': None,
            'content-remove': None,
            'description-info': None,
            'security-info': None,
            ACTION_SESSION_ACCEPT: self._session_accept,
            'session-info': None,
            ACTION_SESSION_INITIATE: self._session_initiate,
            ACTION_SESSION_TERMINATE: self._session_terminate,
            'transport-accept': None,
            'transport-info': None,
            'transport-reject': None,
            'transport-replace': None
        }

    def plugin_end(self):
        # cleanup
        pass

    def session_bind(self, jid):
        # bind features to sessions
        pass

    def register_content_handler(self, ns, handler):
        self._content_handlers[ns] = handler

    def unregister_content_handler(self, ns, handler):
        if ns in self._content_handlers:
            del self._content_handlers[ns]

    def register_transport_handler(self, ns, handler):
        self._transport_handlers[ns] = handler

    def unregister_transport_handler(self, ns, handler):
        if ns in self._transport_handlers:
            del self._transport_handlers[ns]

    def _handle_jingle_stanza(self, iq):
        jingle = iq['jingle']
        log.debug('Incoming Jingle Stanza: {}'.format(jingle))
        action = jingle['action']
        sid = jingle['sid']
        try:
            if not action == ACTION_SESSION_INITIATE and sid not in self._sessions:
                raise UnknownSession(sid)
            if action == ACTION_SESSION_INITIATE and sid in self._sessions:
                raise DuplicateSession(sid)

            if action == ACTION_SESSION_INITIATE:
                self._jingle_actions[action](sid, iq, jingle)
            else:
                self._jingle_actions[action](self._sessions[sid], iq, jingle)

        except JingleException as exc:
            iq.reply(True)
            iq[exc.error_class].set_condition(exc.condition)
            iq.send()

    def _session_initiate(self, sid, iq, jingle):
        session = JingleSession(self, sid, jingle['initiator'], iq['to'])
        self._sessions[sid] = session
        self.xmpp.event(EVENT_SESSION_REQUEST, session)
        iq.reply(True)
        iq.set_type('result')
        iq.send()

    def _session_accept(self, session, iq, jingle):
        session.accept()
        iq.reply(True)
        iq.set_type('result')
        iq.send()

    def _session_terminate(self, session, iq, jingle):
        pass

    def _session_info(self, session, iq, jingle):
        pass

    def _content_accept(self, session, iq, jingle):
        pass

    def _content_add(self, session, iq, jingle):
        pass

    def _content_modify(self, session, iq, jingle):
        pass

    def _content_reject(self, session, iq, jingle):
        pass

    def _content_remove(self, session, iq, jingle):
        pass

    def _description_info(self, session, iq, jingle):
        pass

    def _security_info(self, session, iq, jingle):
        pass

    def _transport_info(self, session, iq, jingle):
        pass

    def _transport_reject(self, session, iq, jingle):
        pass

    def _transport_replace(self, session, iq, jingle):
        pass
