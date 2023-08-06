from enum import auto

from .base import StringAutoEnum


class ENVEnum(StringAutoEnum):
    """Environment settings variations"""

    LOCAL = auto()
    TESTING = auto()
    DEV = auto()
    PROD = auto()
