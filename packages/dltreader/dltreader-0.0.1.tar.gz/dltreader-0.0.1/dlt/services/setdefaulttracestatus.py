from .base import BaseService
from ..constants import TraceStatusType


class DltSetDefaultTraceStatusRequest(BaseService):
    """
    DLT set default trace status request
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.new_trace_status = TraceStatusType(data[0])

        return obj


class DltSetDefaultTraceStatusResponse(BaseService):
    """
    DLT set default trace status response
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.result = data

        return obj
