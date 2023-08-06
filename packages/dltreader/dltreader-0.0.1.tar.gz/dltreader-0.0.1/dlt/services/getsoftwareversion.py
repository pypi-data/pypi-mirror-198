from .base import BaseService


class DltGetSoftwareVersionRequest(BaseService):
    """
    DLT get software version request
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        return obj


class DltGetSoftwareVersionResponse(BaseService):
    """
    DLT get software version response
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.result = data

        return obj
