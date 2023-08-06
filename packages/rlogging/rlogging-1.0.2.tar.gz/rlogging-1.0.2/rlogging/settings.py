from pathlib import Path

LOGGING_ENV = {}

try:
    from decouple import config

    LOGGING_ENV['dir'] = config('APP_LOGGING_DIR', 'logs', Path)

except ImportError:
    import os

    LOGGING_ENV['dir'] = Path(os.environ.get('APP_LOGGING_DIR', 'logs'))


LOGGING = {
    'version': 1,
    'filters': {'warning': {'()': 'rlogging.filters.WarningFilter'}},
    'formatters': {
        'text': {'()': 'rlogging.formatters.RsFormatter'},
        'elk': {'()': 'rlogging.formatters.ElkFormatter'},
    },
    'handlers': {
        'django_file': {
            'class': 'rlogging.handlers.DailyFileHandler',
            'filename': LOGGING_ENV['dir'] / 'django_file.log',
            'formatter': 'elk',
        },
        'app_file': {
            'class': 'rlogging.handlers.DailyFileHandler',
            'filename': LOGGING_ENV['dir'] / 'app_file.log',
            'formatter': 'elk',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'text',
        },
        'error': {
            'class': 'logging.StreamHandler',
            'formatter': 'text',
            'level': 'WARNING',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_file', 'error'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['app_file', 'console'],
        'level': 'INFO',
        'propagate': False,
    },
}


def aply():
    import logging

    logging.config.dictConfig(LOGGING)
