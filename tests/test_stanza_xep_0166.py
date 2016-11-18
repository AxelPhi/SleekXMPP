import unittest

from sleekxmpp import Iq
from sleekxmpp.plugins.xep_0166.stanza import Jingle, Content, Reason
from sleekxmpp.plugins.xep_0166.stanza.reasons import reason_elements
from sleekxmpp.test import SleekTest
from sleekxmpp.xmlstream import register_stanza_plugin


class TestJingleStanzas(SleekTest):

    def setUp(self):
        register_stanza_plugin(Iq, Jingle)
        register_stanza_plugin(Jingle, Content)
        register_stanza_plugin(Jingle, Reason)
        for reason_element in reason_elements:
            register_stanza_plugin(Reason, reason_element)

    def test_reason_stanza(self):
        """Test of a session termination"""
        iq = self.Iq()
        iq['type'] = 'set'
        iq['from'] = 'romeo@montague.lit/orchard'
        iq['to'] = 'juliet@capulet.lit/balcony'
        iq['id'] = 'zid615d9'

        iq['jingle']['action'] = 'session-terminate'
        iq['jingle']['initiator'] = 'romeo@montague.lit/orchard'
        iq['jingle']['sid'] = 'a73sjjvkla37jfea'

        iq['jingle']['reason']['failed-transport'] = True
        iq['jingle']['reason']['text'] = 'Could not create connection to transport'

        self.check(iq, """
        <iq from="romeo@montague.lit/orchard"
            id="zid615d9"
            to="juliet@capulet.lit/balcony"
            type="set">
            <jingle xmlns="urn:xmpp:jingle:1"
                  action="session-terminate"
                  initiator="romeo@montague.lit/orchard"
                  sid="a73sjjvkla37jfea">
                <reason>
                  <failed-transport/>
                  <text>Could not create connection to transport</text>
                </reason>
            </jingle>
        </iq>
        """)

    def test_content_stanza(self):
        """Testing build of a session initiation"""
        iq = self.Iq()
        iq['type'] = 'set'
        iq['from'] = 'romeo@montague.lit/orchard'
        iq['to'] = 'juliet@capulet.lit/balcony'
        iq['id'] = 'zid615d9'

        iq['jingle']['action'] = 'session-initiate'
        iq['jingle']['initiator'] = 'romeo@montague.lit/orchard'
        iq['jingle']['sid'] = 'a73sjjvkla37jfea'

        iq['jingle']['content']['creator'] = 'initiator'
        iq['jingle']['content']['name'] = 'this-is-a-stub'


        self.check(iq, """
        <iq from="romeo@montague.lit/orchard"
            id="zid615d9"
            to="juliet@capulet.lit/balcony"
            type="set">
            <jingle xmlns="urn:xmpp:jingle:1"
                action="session-initiate"
                initiator="romeo@montague.lit/orchard"
                sid="a73sjjvkla37jfea">
            <content
                creator="initiator"
                name="this-is-a-stub" />
            </jingle>
        </iq>
        """)

suite = unittest.TestLoader().loadTestsFromTestCase(TestJingleStanzas)
