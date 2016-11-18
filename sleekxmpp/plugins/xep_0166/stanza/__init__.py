from sleekxmpp.stanza import Error
from sleekxmpp.xmlstream import ElementBase, ET, register_stanza_plugin


class Jingle(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'jingle'
    plugin_attrib = name
    interfaces = (('action', 'initiator',
                   'responder', 'sid'))


class Content(ElementBase):
    namespace = 'urn:xmpp:jingle:1'
    name = 'content'
    plugin_attrib = name
    interfaces = (('creator', 'disposition',
                   'name', 'senders'))


class Reason(ElementBase):
    namespace = ''
    name = 'reason'
    plugin_attrib = name
    interfaces = (('text',))
    sub_interfaces = (('text',))


class JingleErrorCondition(ElementBase):
    plugin_attrib = 'jingle-error-condition'
    interfaces = set(('condition'))
    plugin_attrib_map = {}
    plugin_tag_map = {}
    conditions = set(('out-of-order', 'tie-break', 'unknown-session', 'unsupported-info'))
    condition_ns = 'urn:xmpp:jingle:1'

    def setup(self, xml=None):
        self.xml = ET.Element('')

    def get_condition(self):
        """Return the condition element's name."""
        for child in self.parent().xml:
            if "{%s}" % self.condition_ns in child.tag:
                cond = child.tag.split('}', 1)[-1]
                if cond in self.conditions:
                    return cond
        return ''

    def set_condition(self, value):
        """
        Set the tag name of the condition element.

        Arguments:
           value -- The tag name of the condition element.
        """
        if value in self.conditions:
            del self['condition']
            cond = ET.Element("{%s}%s" % (self.condition_ns, value))
            self.parent().xml.append(cond)
        return self

    def del_condition(self):
        """Remove the condition element."""
        for child in self.parent().xml:
            if "{%s}" % self.condition_ns in child.tag:
                tag = child.tag.split('}', 1)[-1]
                if tag in self.conditions:
                    self.parent().xml.remove(child)
        return self


