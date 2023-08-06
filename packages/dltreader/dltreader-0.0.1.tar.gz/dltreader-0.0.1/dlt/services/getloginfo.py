from .base import BaseService


class DltGetLogInfoRequest(BaseService):
    """
    DLT get log info request
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        raise Exception("Not Implemented yet")

        return obj


class DltGetLogInfoResponse(BaseService):
    """
    DLT get log info response
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.result = data

        return obj
