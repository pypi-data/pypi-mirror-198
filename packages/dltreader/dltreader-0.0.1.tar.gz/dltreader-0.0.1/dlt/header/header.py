from typing import BinaryIO

from .extendedheader import DltExtendedHeader
from .standardheader import DltStandardHeader
from .storageheader import DltStorageHeader


class DltHeader:
    """
    combines the standard header with the extended header
    """
    def __init__(self):
        self.standard: DltStandardHeader = None
        self.extended: DltExtendedHeader = None

    @classmethod
    def create_from(
        cls: "DltHeader",
        f: BinaryIO,
        msbf: bool
    ) -> "DltHeader":
        """
        create DLT header instance from file

        :param cls: DLT header class
        :type cls: DltHeader
        :param f: binary file that is read
        :type f: BinaryIO
        :param msbf: if True, big endian is used
        :type msbf: bool
        :return: DLT header instance
        :rtype: DltHeader
        """
        # create DLT header instance
        obj = cls()

        # get standard header including type and length of payload
        obj.standard = DltStandardHeader.create_from(f=f, msbf=msbf)

        if obj.standard.has_ueh():
            # has extended header
            obj.extended = DltExtendedHeader.create_from(f=f, msbf=msbf)

        return obj

    def header_size(self) -> int:
        """
        size of all headers combined

        :return: combined header size
        :rtype: int
        """
        return (
            self.standard.size() +
            (self.extended.size() if self.standard.has_ueh() else 0)
        )

    def payload_size(self) -> int:
        """
        payload size

        :return: payload size
        :rtype: int
        """
        return self.standard.len - self.header_size()

    def __repr__(self) -> str:
        """
        string representation of the DLT header

        :return: string representation of the DLT header
        :rtype: str
        """
        return str(self.__dict__)
