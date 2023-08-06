
from ctypes import c_ubyte, c_uint16, memmove, pointer, sizeof
from ipaddress import IPv4Address, IPv6Address, ip_address

from src.pyllnu.constants import UDP_PROTOCOL
from src.pyllnu.exceptions import *
from src.pyllnu.ipv4 import IPv4PseudoHeader
from src.pyllnu.ipv6 import IPv6PseudoHeader
from src.pyllnu.struct_ancestor import StructAncestor
from src.pyllnu.util import calc_buf_checksum


class UDPHeader(StructAncestor):
    """
    RFC768. UDP packet header.
    ```
     0      7 8     15 16    23 24    31
    +--------+--------+--------+--------+
    |     Source      |   Destination   |
    |      Port       |      Port       |
    +--------+--------+--------+--------+
    |                 |                 |
    |     Length      |    Checksum     |
    +--------+--------+--------+--------+
    ```
    """

    _fields_ = [
        ('src_port', c_uint16),
        ('dst_port', c_uint16),
        ('len',      c_uint16),
        ('checksum', c_uint16)
    ]

    @staticmethod
    def create_and_add_ports(src_port, dst_port) -> 'UDPHeader':
        header = UDPHeader()
        header.src_port = src_port
        header.dst_port = dst_port
        return header

    @staticmethod
    def create(src_port: int, dst_port: int, payload_size: int, chksum: int = 0) -> 'UDPHeader':
        header = UDPHeader()
        header.src_port = src_port
        header.dst_port = dst_port
        header.len = payload_size + sizeof(UDPHeader)
        header.checksum = chksum
        return header

    @staticmethod
    def from_buffer(buf: bytes) -> 'UDPHeader':
        hdr = UDPHeader()
        memmove(pointer(hdr), buf, sizeof(hdr))
        return hdr

    @staticmethod
    def calc_checksum_static(udp_header: 'UDPHeader', ip_info: tuple[str, str], data: bytes) -> int:
        src = ip_address(ip_info[0])
        dst = ip_address(ip_info[1])

        if isinstance(src, IPv4Address) and isinstance(dst, IPv4Address):
            checksum_header = IPv4PseudoHeader()
            checksum_header.src_ip = (c_ubyte * 4)(*list(src.packed))
            checksum_header.dst_ip = (c_ubyte * 4)(*list(dst.packed))
        elif isinstance(src, IPv6Address) and isinstance(dst, IPv6Address):
            checksum_header = IPv6PseudoHeader()
            checksum_header.src_ip = (c_ubyte * 16)(*list(src.packed))
            checksum_header.dst_ip = (c_ubyte * 16)(*list(dst.packed))
        else:
            raise InvalidIPError()

        checksum_header.len = sizeof(udp_header) + len(data)
        checksum_header.zero = 0
        checksum_header.next_header = UDP_PROTOCOL

        return calc_buf_checksum(bytes(checksum_header) + bytes(udp_header) + data)

    def calc_checksum(self, ip_info: tuple[str, str], data: bytes):
        self.checksum = self.calc_checksum_static(self, ip_info, data)
