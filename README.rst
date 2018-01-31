matrix_log_handler
==================

.. image:: https://img.shields.io/pypi/v/matrix_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/matrix_log_handler

.. image:: https://img.shields.io/pypi/wheel/matrix_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/matrix_log_handler

.. image:: https://img.shields.io/pypi/format/matrix_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/matrix_log_handler

.. image:: https://img.shields.io/pypi/pyversions/matrix_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/matrix_log_handler

.. image:: https://img.shields.io/pypi/status/matrix_log_handler.svg?style=flat-square
    :target: https://pypi.python.org/pypi/matrix_log_handler

Python log handler that posts to a Matrix room. Posts to the Matrix API using
https://github.com/matrix-org/matrix-python-sdk.

Installation
------------

.. code-block:: bash

    pip install matrix-log-handler

Options
-------

base_url (required)
~~~~~~~~~~~~~~~~~~~

The base URL of the Matrix Homeserver to use.  Up to, but *not* including `/_matrix/client`.

room_id (required)
~~~~~~~~~~~~~~~~~~

The room ID to use, like !ppfKZfDaaAaWzLkYrw:example.org.

token
~~~~~

An access token that can be used to send messages.

username and password
~~~~~~~~~~~~~~~~~~~~~

An optional username/password to login with.  Note that it advised *not* to use these parameters, but use ``token`` instead.

fail_silent
~~~~~~~~~~~
Defaults to ``False``.

If your access token, username/password, or base URL is invalid, or for some other reason the API
call returns an error, this option will silently ignore the API error.

If you enable this setting, **make sure you have another log handler** that will also handle the
same log events, or they may be lost entirely.

Logging configuration
--------------------

This example will send log messages with the level of ERROR or above to Matrix.

.. code-block:: python

    import logging

    logging.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'matrix-error': {
                'class': 'matrix_log_handler.MatrixLogHandler',
                'level': 'ERROR',
                'base_url': 'https://matrix.example.com',
                'room_id': '!ppfKZfDaaAaWzLkYrw:example.org'
            },
            'loggers': {
                '': {
                    'handlers': ['matrix-error'],
                    'level': 'ERROR',
                    'propagate': True,
                },
            }
        }
    })

    logging.error('Hello, Matrix!')

License
-------

Apache 2.0

Matrix-Python-SDK is also under Apache 2.0.
