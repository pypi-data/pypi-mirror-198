from typing import BinaryIO

from dlt.constants import PayloadArgumentFlag
from dlt.payloadargument import DltPayloadArgument
from dlt.header import DltHeader
from dlt.types import DltPayloadArgumentBoolType, DltPayloadArgumentSIntType, \
    DltPayloadArgumentUIntType, DltPayloadArgumentFloaType, \
    DltPayloadArgumentArayType, DltPayloadArgumentStrgType, \
    DltPayloadArgumentRawdType, DltPayloadArgumentTraiType, \
    DltPayloadArgumentStruType


class DltPayloadVerbose:
    """
    verbose payload class
    """
    @classmethod
    def create_from(cls, f: BinaryIO, header: DltHeader):
        obj = cls()

        # set msbf
        obj.msbf = header.standard.has_msbf()

        # set number of arguments
        obj.noar = header.extended.noar

        # parse arguments
        obj.args = []

        for _ in range(obj.noar):
            arg = DltPayloadArgument.create_from(f, obj.msbf)

            # get argument type class
            arg_type = {
                PayloadArgumentFlag.BOOL: DltPayloadArgumentBoolType,
                PayloadArgumentFlag.SINT: DltPayloadArgumentSIntType,
                PayloadArgumentFlag.UINT: DltPayloadArgumentUIntType,
                PayloadArgumentFlag.FLOA: DltPayloadArgumentFloaType,
                PayloadArgumentFlag.ARAY: DltPayloadArgumentArayType,
                PayloadArgumentFlag.STRG: DltPayloadArgumentStrgType,
                PayloadArgumentFlag.RAWD: DltPayloadArgumentRawdType,
                PayloadArgumentFlag.TRAI: DltPayloadArgumentTraiType,
                PayloadArgumentFlag.STRU: DltPayloadArgumentStruType
            }[arg.type]

            # create instance of the type class
            obj.args.append(
                arg_type.create_from(f, arg, obj.msbf)
            )

        return obj

    def __repr__(self):
        return (
            "<DltPayloadVerbose(args=[{}])>".format(
                ",".join([
                    f"{arg.__class__.__name__}(value={arg.value})"
                    for arg in self.args
                ])
            )
        )
