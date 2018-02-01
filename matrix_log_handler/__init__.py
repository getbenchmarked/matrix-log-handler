"""Log handler to send log messages to a Matrix room
"""

import logging

from matrix_client.api import MatrixHttpApi


class MatrixLogHandler(logging.Handler):
    """Log handler to send records to a Matrix room.

    :param base_url: the base URL of the Matrix homeserver to use.  This should not include the
        `_matrix/client/` part.
    :param room_id: the room ID to send the messages to.  The account must be in the room and must
        have the sufficient power level to send messages.  Note that this must be the room ID
        (!foo:bar.org), not an alias!
    :param username: a username to use for logging in if no access token was set
    :param password: a password to use for logging in if no access token was set
    :param token: a valid access token that can be used to identify the log handler to the Matrix
        homeserver.  This is the recommended way for authorization.  If not set, a
        username/password pair must be set so the handler can acquire an access token.
    :type base_url: str
    :type room_id: str
    :type username: str
    :type password: str
    :type token: str
    """

    def __init__(self, base_url, room_id,
               username=None, password=None, token=None, fail_silent=False,
               format='[%(levelname)s] [%(asctime)s] [%(name)s] - %(message)s'):
        logging.Handler.__init__(self)

        self.base_url = base_url
        self.username = username
        self.password = password
        self.room_id = room_id
        self.token = token
        self.fail_silent = fail_silent

        self.matrix = MatrixHttpApi(base_url, token=self.token)

        self.formatter = logging.Formatter(format)

    def _login(self):
        if self.username is None or self.password is None:
            raise ValueError(
                'Both username and password must be set if there is no token available!')

        response = self.matrix.login('m.login.password', user=self.username, password=self.password)

        self.token = response['access_token']

    def _make_content(self, record):
        content = {
            'msgtype': 'm.text',
            'body': self.format(record),
        }

        return content

    def emit(self, record):
        content = self._make_content(record)

        try:
            if not self.token:
                self._login()

            self.matrix.send_message_event(self.room_id, 'm.room.message', content)
        except:
            self.handleError(record)
