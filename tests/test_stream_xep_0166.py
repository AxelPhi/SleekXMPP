import logging
import time
import threading


import unittest
from sleekxmpp.test import SleekTest


class TestJingleSession(SleekTest):

    """
    Test using the XEP-0166 plugin.
    """

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)

    def tearDown(self):
        self.stream_close()

    def testSessionStart(self):
        self.stream_start(mode='client',
                          plugins=['xep_0166'])

        ret = self.recv("""
        <iq from='romeo@montague.lit/orchard'
            id='zid615d9'
            to='juliet@capulet.lit/balcony'
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
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestJingleSession)
