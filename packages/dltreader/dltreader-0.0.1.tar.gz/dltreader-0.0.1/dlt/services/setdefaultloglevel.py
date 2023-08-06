from .base import BaseService
from ..constants import DltLogLevelType


class DltSetDefaultLogLevelRequest(BaseService):
    """
    DLT set default log level request
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.new_log_level = DltLogLevelType(data[0])

        return obj


class DltSetDefaultLogLevelResponse(BaseService):
    """
    DLT set default log level response
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.result = data

        return obj
