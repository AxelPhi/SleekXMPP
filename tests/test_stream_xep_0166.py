import logging
import time

import unittest

from sleekxmpp.plugins.xep_0166.jingle import JingleSession
from sleekxmpp.test import SleekTest


class TestJingleSession(SleekTest):
    """
    Test using the XEP-0166 plugin.
    """

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(level=logging.DEBUG)

    def setUp(self):
        self.stream_start(mode='client', plugins=['xep_0166'])

    def tearDown(self):
        self.stream_close()

    def testAcceptSession(self):
        self.xmpp['xep_0166']._sessions['a73sjjvkla37jfea'] = JingleSession('a73sjjvkla37jfea0',
                                                                              'romeo@montague.lit/orchard',
                                                                              'juliet@capulet.lit/balcony')

        self.recv("""
                <iq from='juliet@capulet.lit/balcony'
                    id='rc61n59s'
                    to='romeo@montague.lit/orchard'
                    type='set'>
                  <jingle xmlns='urn:xmpp:jingle:1'
                          action='session-accept'
                          responder='juliet@capulet.lit/balcony'
                          sid='a73sjjvkla37jfea'>
                    <content creator='initiator' name='this-is-a-stub'>
                      <description xmlns='urn:xmpp:jingle:apps:stub:0'/>
                      <transport xmlns='urn:xmpp:jingle:transports:stub:0'/>
                    </content>
                  </jingle>
                </iq>
                """)

        time.sleep(.5)

        self.send("""
                <iq to='juliet@capulet.lit/balcony'
                    id='rc61n59s'
                    type='result'>
                </iq>
                """)

    def testInitiateSession(self):
        self.recv("""
        <iq to='juliet@capulet.lit/balcony'
            from='romeo@montague.lit/orchard'
            id='zid615d9'
            type='set'>
            <jingle xmlns='urn:xmpp:jingle:1'
                action='session-initiate'
                initiator='romeo@montague.lit/orchard'
                sid='a73sjjvkla37jfea'>
                <content creator='initiator' name='this-is-a-stub'>
                    <description xmlns='urn:xmpp:jingle:apps:stub:0'/>
                    <transport xmlns='urn:xmpp:jingle:transports:stub:0'/>
                 </content>
            </jingle>
        </iq>
        """)

        time.sleep(.5)

        self.send("""
        <iq to='romeo@montague.lit/orchard'
            id='zid615d9'
            type='result'>
        </iq>
        """)


suite = unittest.TestLoader().loadTestsFromTestCase(TestJingleSession)
