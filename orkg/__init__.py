import logging

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass


import sys

logger = logging.getLogger("ORKG")
logger.addHandler(logging.NullHandler())

from .client import ORKG