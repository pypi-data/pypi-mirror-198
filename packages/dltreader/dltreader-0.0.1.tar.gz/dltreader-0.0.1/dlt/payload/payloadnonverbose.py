import logging
from typing import BinaryIO

from dlt.typereader import TypeReader
from dlt.header import DltHeader
from dlt.services import DltSetDefaultTraceStatusRequest, \
    DltGetLogInfoRequest, DltSetDefaultLogLevelRequest, \
    DltStoreConfigurationRequest, DltResetToFactoryDefaultRequest, \
    DltSetMessageFilteringRequest, DltGetSoftwareVersionRequest, \
    DltGetTraceStatusRequest
from dlt.constants import ServiceId, DltMessageType, DltControlType


# prepare logger
log = logging.getLogger(__name__)


class DltPayloadNonVerbose:
    """
    non-verbose payload class
    """
    @classmethod
    def create_from(
        cls,
        f: BinaryIO,
        header: DltHeader
    ):
        obj = cls()

        # set msbf
        obj.msbf = header.standard.has_msbf()

        # enforce little endian
        tr = TypeReader(msbf=False)
        obj.message_id = tr.read_uint32(f)

        # read payload (size minus message ID)
        obj.value = f.read(header.payload_size() - 4)

        if header.extended is not None:
            if header.extended.mstp == DltMessageType.CONTROL:
                # control message
                service = ServiceId(obj.message_id)
                if header.extended.mtin == DltControlType.REQUEST:
                    # requests
                    service_msg = None
                    try:
                        service_msg = {
                            ServiceId.SET_DEFAULT_LOG_LEVEL: (
                                DltSetDefaultLogLevelRequest
                            ),
                            ServiceId.SET_DEFAULT_TRACE_STATUS: (
                                DltSetDefaultTraceStatusRequest
                            ),
                            ServiceId.GET_LOG_INFO: (
                                DltGetLogInfoRequest
                            ),
                            ServiceId.GET_DEFAULT_LOG_LEVEL: (
                                DltSetDefaultLogLevelRequest
                            ),
                            ServiceId.STORE_CONFIG: (
                                DltStoreConfigurationRequest
                            ),
                            ServiceId.RESET_TO_FACTORY_DEFAULT: (
                                DltResetToFactoryDefaultRequest
                            ),
                            ServiceId.SET_MESSAGE_FILTERING: (
                                DltSetMessageFilteringRequest
                            ),
                            ServiceId.GET_SOFTWARE_VERSION: (
                                DltGetSoftwareVersionRequest
                            ),
                            ServiceId.GET_TRACE_STATUS: (
                                DltGetTraceStatusRequest
                            ),
                            # TODO:
                            # GetLogChannelNames
                            # TraceStatus
                            # SetLogChannelAssignment
                            # SetLogChannelThreshold
                            # GetLogChannelThreshold
                            # BufferOverflowNotification
                            # CallSWCInjection
                        }[service].create_from(obj.value)

                        return service_msg

                    except KeyError:
                        if service in (
                            ServiceId.SET_COM_INTERFACE_STATUS,
                            ServiceId.SET_COM_INTERFACE_MAX_BANDWIDTH,
                            ServiceId.SET_VERBOSE_MODE,
                            ServiceId.SET_TIMING_PACKETS,
                            ServiceId.GET_LOCAL_TIME,
                            ServiceId.SET_USE_ECU_ID,
                            ServiceId.SET_USE_SESSION_ID,
                            ServiceId.SET_USE_TIMESTAMP,
                            ServiceId.SET_USE_EXTENDED_HEADER,
                            ServiceId.MESSAGE_BUFFER_OVERFLOW,
                            ServiceId.GET_COM_INTERFACE_STATUS,
                            ServiceId.GET_COM_INTERFACE_MAX_BANDWIDTH,
                            ServiceId.GET_VERBOSE_MODE_STATUS,
                            ServiceId.GET_MESSAGE_FILTERING_STATUS,
                            ServiceId.GET_USE_ECU_ID,
                            ServiceId.GET_USE_SESSION_ID,
                            ServiceId.GET_USE_TIMESTAMP,
                            ServiceId.GET_USE_EXTENDED_HEADER
                        ):
                            # deprecated services
                            log.warning(
                                f"skipping deprecated service: {service}"
                            )
                            return None

                        else:
                            log.error(f"NOT IMPLEMENTED YET: {service}")

        return obj

    def __repr__(self):
        return (
            f"<DltPayloadNonVerbose(message_id={self.message_id}, "
            f"value={self.value})>"
        )
