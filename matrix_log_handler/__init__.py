"""Log handler to send log messages to a Matrix room
"""

import logging

from matrix_client.api import MatrixHttpApi


class MatrixLogHandler(logging.Handler):
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
