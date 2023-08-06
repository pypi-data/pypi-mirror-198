from .base import BaseService


class DltGetTraceStatusRequest(BaseService):
    """
    DLT get trace status request
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        return obj


class DltGetTraceStatusResponse(BaseService):
    """
    DLT get trace status response
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.result = data[0]
        obj.trace_status = data[1]

        return obj
