
from ctypes import (BigEndianStructure, c_ubyte, c_uint, memmove, pointer,
                    sizeof)
from ipaddress import IPv6Address

from src.pyllnu.constants import *
from src.pyllnu.struct_ancestor import StructAncestor


class IPv6PseudoHeader(BigEndianStructure):
    """
    Represents a pseudo-header to be used when calculating the definitive
    header's checksum. This structure uses IPv6 (128-bit) addresses.
    
    This header contains only a few fields from the original header.
    """
    _fields_ = [
        ('src_ip',      c_ubyte * 16),
        ('dst_ip',      c_ubyte * 16),
        ('len',         c_uint, 16),
        ('zero',        c_uint, 24),
        ('next_header', c_ubyte, 8)
    ]
    

class IPv6Header(StructAncestor):
    """
    RFC8200. Represents an IPv6 packet header.

    ```
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |Version| Traffic Class |           Flow Label                  |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |         Payload Length        |  Next Header  |   Hop Limit   |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                                                               |
    +                                                               +
    |                                                               |
    +                         Source Address                        +
    |                                                               |
    +                                                               +
    |                                                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                                                               |
    +                                                               +
    |                                                               |
    +                      Destination Address                      +
    |                                                               |
    +                                                               +
    |                                                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    ```
    """
    _fields_ = [
        ('version',             c_uint, 4),
        ('traffic_class',       c_uint, 8),
        ('flow_label',          c_uint, 20),
        ('payload_length',      c_uint, 16),
        ('next_header',         c_uint, 8),
        ('hop_limit',           c_uint, 8),
        ('source_address',      c_ubyte * 16),
        ('destination_address', c_ubyte * 16),
    ]

    @staticmethod
    def create(src_ipv6: str | IPv6Address, dst_ipv6: str | IPv6Address, len: int, next_header: int, flow_label: int = 0) -> 'IPv6Header':
        if isinstance(src_ipv6, str):
            src_addr = IPv6Address(src_ipv6).packed
        else:
            src_addr = src_ipv6.packed

        if isinstance(dst_ipv6, str):
            dst_addr = IPv6Address(dst_ipv6).packed
        else:
            dst_addr = dst_ipv6.packed

        header                     = IPv6Header()
        header.version             = IPV6_HEADER_VERSION
        header.traffic_class       = IPV6_HEADER_TRAFFIC_CLASS
        header.flow_label          = flow_label
        header.payload_length      = len
        header.next_header         = next_header
        header.hop_limit           = IPV6_HEADER_HOP_LIMIT
        header.source_address      = (c_ubyte * 16)(*list(src_addr))
        header.destination_address = (c_ubyte * 16)(*list(dst_addr))
        return header

    @staticmethod
    def from_buffer(buf: bytes) -> 'IPv6Header':
        header = IPv6Header()
        memmove(pointer(header), buf, sizeof(header))
        return header


def ipv6_to_int(ip: str | IPv6Address) -> int:
    if isinstance(ip, str):
        ip = IPv6Address(ip)
    return int(ip)


def ipv6_to_bytes(ip: str | IPv6Address) -> bytes:
    if isinstance(ip, str):
        ip = IPv6Address(ip)
    return ipv6_to_int(ip).to_bytes(16, 'big')
