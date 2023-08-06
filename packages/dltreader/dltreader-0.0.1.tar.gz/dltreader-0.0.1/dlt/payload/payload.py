from typing import BinaryIO

from .payloadnonverbose import DltPayloadNonVerbose
from .payloadverbose import DltPayloadVerbose
from dlt.header.header import DltHeader
from dlt.constants import DltPayloadType


class DltPayload:
    """
    payload class
    """
    @classmethod
    def create_from(
        cls: "DltPayload",
        f: BinaryIO,
        header: DltHeader
    ) -> "DltPayload":
        """
        create DLT payload from file

        :param cls: DLT payload class
        :type cls: DltPayload
        :param f: binary file that is read
        :type f: BinaryIO
        :param header: DLT header
        :type header: DltHeader
        :return: DLT payload
        :rtype: DltPayload
        """
        # create DLT payload instance
        obj = cls()

        if (header.extended is None) or (header.extended.verb is False):
            # non-verbose payload, i.e., without meta information
            obj.mode = DltPayloadType.NON_VERBOSE
            obj.payload = DltPayloadNonVerbose.create_from(f, header)

        else:
            # verbose payload, i.e., with meta information
            obj.mode = DltPayloadType.VERBOSE
            obj.payload = DltPayloadVerbose.create_from(f, header)

        return obj

    def __repr__(self) -> str:
        """
        string representation of the DLT payload

        :return: string representation of the DLT payload
        :rtype: str
        """
        return str(self.payload)
