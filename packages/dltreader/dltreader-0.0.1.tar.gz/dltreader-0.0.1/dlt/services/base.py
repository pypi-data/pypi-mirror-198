from abc import ABC


class BaseService(ABC):
    """
    abstract base class from which all services are derived
    """
    @classmethod
    def create_from(cls: "BaseService", data):
        """
        override this method based on type
        """
        obj = cls(data)

        return obj

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.__dict__})"
