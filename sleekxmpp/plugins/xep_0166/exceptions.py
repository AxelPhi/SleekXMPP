class JingleException(Exception):
    def __init__(self, session_id, condition, error_class='jingleError'):
        super(JingleException, self).__init__()
        self.session_id = session_id
        self.condition = condition
        self.error_class = error_class


class UnknownSession(JingleException):
    def __init__(self, session_id):
        super(UnknownSession, self).__init__(session_id, 'unknown-session')


class OutOfOrder(JingleException):
    def __init__(self, session_id):
        super(OutOfOrder, self).__init__(session_id, 'out-of-order')


class DuplicateSession(JingleException):
    def __init__(self, session_id):
        super(DuplicateSession, self).__init__(session_id, 'conflict', 'error')
