"""Test module for matrix_log_handler
"""

import logging
import unittest
from unittest.mock import patch, MagicMock

from matrix_log_handler import MatrixLogHandler

class MatrixLogHandlerTestCase(unittest.TestCase):
    """Test case for MatrixLogHandler
    """

    def test_logging(self):
        """Test if logs actually go to Matrix
        """

        handler = MatrixLogHandler('https://example.com', '!test:example.com', token='test_token')
        logger = logging.Logger('test')
        logger.addHandler(handler)

        mocked_response = MagicMock()
        mocked_response.status_code = 200

        with patch('matrix_client.api.requests.request', return_value=mocked_response) as mocked:
            logger.error('Test Message')

        mocked.assert_called_once()

if __name__ == '__main__':
    unittest.main()
