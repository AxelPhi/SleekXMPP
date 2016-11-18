from sleekxmpp.stanza import Error
from sleekxmpp.plugins.xep_0166.stanza.errors import UnknownSession

class JingleException(Exception):
    def __init__(self, session_id):
        super(JingleException, self).__init__(session_id)

        # error = Error()
        # error.del_condition()
        # error['type'] = self.error_type
        # error['unknown-session'] = True
        # error.set_text(self.text)
        # return error


class UnkownJingleSession(JingleException):

    # def __init__(self, session_id):
    #     super(UnkownJingleSession, self).__init__(session_id)
    #     self.session_id = session_id
    #     self.error_type = 'cancel'
    #     self.error_condition = 'unknown-session'
    #     self.text = 'Unknown jingle session: '.format(self.session_id)


    @property
    def error_stanza(self):
        return UnknownSession()
