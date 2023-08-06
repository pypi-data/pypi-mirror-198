from .base import BaseService
from ..constants import StatusType


class DltSetMessageFilteringRequest(BaseService):
    """
    DLT set message filtering request
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.new_status = StatusType(data[0])

        return obj


class DltSetMessageFilteringResponse(BaseService):
    """
    DLT set message filtering response
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.result = data

        return obj
