from typing import BinaryIO
import logging

from .exceptions import PacketException
from .header import DltHeader
from .payload import DltPayload


# prepare logger
log = logging.getLogger(__name__)


class DltPacket:
    """
    packet
    """
    @property
    def len(self) -> int:
        """
        returns the length based on standard header
        if not available -1 is returned

        :return: length of the packet
        :rtype: int
        """
        if (self.header is None) or (self.header.standard is None):
            return -1

        return self.header.standard.len

    @classmethod
    def create_from(
        cls: "DltPacket",
        f: BinaryIO,
        msbf: bool
    ) -> "DltPacket":
        """
        create packet instance from file

        :param cls: packet class
        :type cls: Packet
        :param f: binary file that is read
        :type f: BinaryIO
        :param msbf: if True, big endian is used
        :type msbf: bool
        :return: packet instance
        :rtype: Packet
        """
        # create packet instance
        obj = cls()

        # get header
        obj.header = DltHeader.create_from(f, msbf=msbf)
        if obj.header is None:
            # invalid packet header
            raise PacketException("Invalid packet header!")

        if obj.header.standard is None:
            # failed to read standard header
            raise PacketException("Fail to read standard header!")

        log.debug(
            f"header_size={obj.header.header_size()}, "
            f"payload_size={obj.header.payload_size()}"
        )

        if obj.header.payload_size() > 0:
            # get payload
            obj.payload = DltPayload.create_from(
                f, obj.header
            )

        else:
            # not payload
            obj.payload = None

        log.debug(
            f"payload={obj.payload}"
        )

        return obj

    def __repr__(self) -> str:
        """
        string representation of packet

        :return: string representation of packet
        :rtype: str
        """
        return (
            f"{self.header.standard}\n{self.header.extended}\n"
            f"{self.payload}"
        )
