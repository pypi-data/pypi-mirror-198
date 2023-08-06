from .base import BaseService


class DltStoreConfigurationRequest(BaseService):
    """
    DLT store configuration request
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        return obj


class DltStoreConfigurationResponse(BaseService):
    """
    DLT store configuration response
    """
    @classmethod
    def create_from(cls, data):
        obj = cls()

        obj.result = data

        return obj
