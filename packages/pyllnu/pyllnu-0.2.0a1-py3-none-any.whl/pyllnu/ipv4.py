
import random
import struct
from ctypes import (BigEndianStructure, c_ubyte, c_uint, c_uint8, c_uint16,
                    c_uint32, memmove, pointer, sizeof)
from ipaddress import IPv4Address, IPv4Network
from socket import inet_ntoa

from src.pyllnu.util import calc_buf_checksum
from src.pyllnu.exceptions import *
from src.pyllnu.struct_ancestor import StructAncestor


class IPv4PseudoHeader(BigEndianStructure):
    """
    Represents a pseudo-header to be used when calculating the definitive
    header's checksum. This structure uses IPv4 (32-bit) addresses.
    
    This header contains only a few fields from the original header.
    """
    _fields_ = [
        ('src_ip',      c_ubyte * 4),
        ('dst_ip',      c_ubyte * 4),
        ('len',         c_uint32),
        ('zero',        c_uint, 24),
        ('next_header', c_ubyte, 8)
    ]


class IPv4Header(StructAncestor):
    """
    RFC791. Represents an IPv4 packet header.

    ```
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |Version|  IHL  |Type of Service|          Total Length         |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |         Identification        |Flags|      Fragment Offset    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |  Time to Live |    Protocol   |         Header Checksum       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                       Source Address                          |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Destination Address                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Options                    |    Padding    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    ```
    """

    _fields_ = [
        ('version',  c_uint8, 4),
        ('ihl',      c_uint8, 4),
        ('tos',      c_uint8),
        ('len',      c_uint16),
        ('id',       c_uint16),
        ('flags',    c_ubyte, 3),
        ('offset',   c_uint16, 13),
        ('ttl',      c_uint8),
        ('protocol', c_uint8),
        ('checksum', c_uint16),
        ('src',      c_uint32),
        ('dst',      c_uint32),
    ]

    @staticmethod
    def calc_checksum_static(header: 'IPv4Header') -> int:
        return calc_buf_checksum(bytes(header))

    @staticmethod
    def from_buffer(buf: bytes) -> 'IPv4Header':
        header = IPv4Header()
        memmove(pointer(header), buf, sizeof(header))
        return header

    @staticmethod
    def create(src_ip: str, dst_ip: str, payload_len: int, next_header_protocol: int, header_id: int | None = None) -> 'IPv4Header':
        ipv4_hdr          = IPv4Header()
        ipv4_hdr.version  = 4
        ipv4_hdr.ihl      = 5
        ipv4_hdr.tos      = 0
        ipv4_hdr.len      = (ipv4_hdr.ihl * 4) + payload_len
        ipv4_hdr.id       = header_id or random.randint(1, 0xffff-1)
        ipv4_hdr.flags    = 0
        ipv4_hdr.offset   = 0
        ipv4_hdr.ttl      = 0xffff
        ipv4_hdr.protocol = next_header_protocol
        ipv4_hdr.checksum = 0
        ipv4_hdr.src      = int(IPv4Address(src_ip))
        ipv4_hdr.dst      = int(IPv4Address(dst_ip))
        ipv4_hdr.options  = 0
        ipv4_hdr.padding  = 0
        ipv4_hdr.calc_checksum()

        return ipv4_hdr
    
    def calc_checksum(self):
        """
        Calculates an IPv4 header's checksum in-place.

        Args:
            hdr (IPv4Header)
        """
        self.checksum = self.calc_checksum_static(self)


def get_ipv4_address_pool(ip: str | IPv4Address, mask: str | IPv4Address) -> IPv4Network:
    if isinstance(ip, str):
        ip = IPv4Address(ip)
    if isinstance(mask, str):
        mask = IPv4Address(mask)
    network = IPv4Address(
        int.from_bytes(ip.packed, 'big') & int.from_bytes(mask.packed, 'big'))
    return IPv4Network(f'{network.exploded}/{mask.exploded}')


def get_default_gateway(iface: str) -> IPv4Address:
    with open('/proc/net/route') as f:
        for line in f:
            fields = line.strip().split()
            if fields[0].lower() != iface:
                continue
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue
            return IPv4Address(inet_ntoa(struct.pack('<L', int(fields[2], 16))))
    raise GatewayNotFoundError(f'Could not find default gateway for interface {iface}')


def ip_to_int(ip: str | IPv4Address) -> int:
    if isinstance(ip, str):
        ip = IPv4Address(ip)
    return int(ip)


def ip_to_bytes(ip: str | IPv4Address) -> bytes:
    if isinstance(ip, str):
        ip = IPv4Address(ip)
    return ip_to_int(ip).to_bytes(4, 'big')
