"""
    SleekXMPP: The Sleek XMPP Library
    Copyright (C) 2012 Nathanael C. Fritz, Lance J.T. Stout
    This file is part of SleekXMPP.

    See the file LICENSE for copying permission.
"""

from sleekxmpp.plugins.base import register_plugin

from sleekxmpp.plugins.xep_0166 import stanza
from sleekxmpp.plugins.xep_0166.jingle import XEP_0166

register_plugin(XEP_0166)

xep_0166 = XEP_0166
