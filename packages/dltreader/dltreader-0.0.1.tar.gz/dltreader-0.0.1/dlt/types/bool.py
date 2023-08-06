from typing import BinaryIO

from dlt.payloadargument import DltPayloadArgument
from .base import DltPayloadArgumentBaseType


class DltPayloadArgumentBoolType(DltPayloadArgumentBaseType):
    @classmethod
    def create_from(
        cls,
        f: BinaryIO,
        payload_arg: DltPayloadArgument,
        msbf: bool
    ):
        obj = cls(payload_arg, msbf)

        # get name
        obj.name = obj._get_name(f)

        # get bool value
        obj.value = obj.tr.read_bool(f)

        return obj

    def _get_name(self, f: BinaryIO):
        """
        get name
        """
        name = "undefined"
        if self.payload_arg.vari is True:
            # get name and unit
            name_len = self.tr.read_uint16(f)
            name = self.tr.read_string(f, name_len).decode("ascii")

        return name
