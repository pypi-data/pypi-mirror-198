from .base import BaseService


class DltGetDefaultLogLevelRequest(BaseService):
    """
    DLT get default log level request
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        return obj


class DltGetDefaultLogLevelResponse(BaseService):
    """
    DLT get default log level response
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.result = data[0]
        obj.log_level = data[1]

        return obj
