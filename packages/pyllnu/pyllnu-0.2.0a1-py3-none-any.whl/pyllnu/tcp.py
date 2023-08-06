
import math
from ctypes import c_ubyte, c_uint16, c_uint32, memmove, pointer, sizeof
from dataclasses import dataclass
from ipaddress import IPv4Address, IPv6Address
from random import randint

from src.pyllnu.exceptions import *
from src.pyllnu.ipv4 import IPv4PseudoHeader
from src.pyllnu.ipv6 import IPv6PseudoHeader
from src.pyllnu.struct_ancestor import StructAncestor
from src.pyllnu.util import calc_buf_checksum


@dataclass
class TCPHeaderFlags:
    """
    Utility struct that represents the TCP header flags.
    """
    non: bool = False
    cwr: bool = False
    ecn: bool = False
    urg: bool = False
    ack: bool = False
    psh: bool = False
    rst: bool = False
    syn: bool = False
    fin: bool = False

    @staticmethod
    def from_header(header: 'TCPHeader') -> 'TCPHeaderFlags':
        return TCPHeaderFlags(
            non=bool(header.non),
            cwr=bool(header.cwr),
            ecn=bool(header.ecn),
            urg=bool(header.urg),
            ack=bool(header.ack),
            psh=bool(header.psh),
            rst=bool(header.rst),
            syn=bool(header.syn),
            fin=bool(header.fin),
        )


class TCPHeader(StructAncestor):
    """
    RFC793. Represents a TCP header.

    ```
     0                   1                   2                   3
     0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |          Source Port          |       Destination Port        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                        Sequence Number                        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Acknowledgment Number                      |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |  Data |           |U|A|P|R|S|F|                               |
    | Offset| Reserved  |R|C|S|S|Y|I|            Window             |
    |       |           |G|K|H|T|N|N|                               |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |           Checksum            |         Urgent Pointer        |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                    Options                    |    Padding    |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |                             data                              |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    ```

    Control Bits:  6 bits (from left to right):
    URG:  Urgent Pointer field significant
    ACK:  Acknowledgment field significant
    PSH:  Push Function
    RST:  Reset the connection
    SYN:  Synchronize sequence numbers
    FIN:  No more data from sender
    """
    _fields_ = [
        ('src_port',       c_uint16),
        ('dst_port',       c_uint16),
        ('seq_num',        c_uint32),
        ('ack_num',        c_uint32),
        ('offset',         c_uint16, 4),
        ('reserved',       c_uint16, 3),
        ('non',            c_uint16, 1),
        ('cwr',            c_uint16, 1),
        ('ecn',            c_uint16, 1),
        ('urg',            c_uint16, 1),
        ('ack',            c_uint16, 1),
        ('psh',            c_uint16, 1),
        ('rst',            c_uint16, 1),
        ('syn',            c_uint16, 1),
        ('fin',            c_uint16, 1),
        ('window',         c_uint16),
        ('checksum',       c_uint16),
        ('urgent_pointer', c_uint16),
    ]

    @staticmethod
    def create(ip_info: tuple[IPv4Address | IPv6Address, IPv4Address | IPv6Address],
               src_port: int,
               dst_port: int,
               opts: bytes,
               data: bytes = b'',
               seq_num: int = 0,
               tcp_flags: TCPHeaderFlags = TCPHeaderFlags(),
               window: int = 0xFFC4,
               urg_p: int = 0) -> 'TCPHeader':
        header = TCPHeader()
        header.src_port = src_port
        header.dst_port = dst_port
        header.seq_num = seq_num
        header.ack_num = 0
        header.offset = 5 + (math.ceil(len(opts) / 4))
        header.reserved = 0
        header.non = c_uint16(tcp_flags.non)
        header.cwr = c_uint16(tcp_flags.cwr)
        header.ecn = c_uint16(tcp_flags.ecn)
        header.urg = c_uint16(tcp_flags.urg)
        header.ack = c_uint16(tcp_flags.ack)
        header.psh = c_uint16(tcp_flags.psh)
        header.rst = c_uint16(tcp_flags.rst)
        header.syn = c_uint16(tcp_flags.syn)
        header.fin = c_uint16(tcp_flags.fin)
        header.window = window
        header.urgent_pointer = urg_p
        header.calc_checksum(ip_info, opts, data)

        return header

    @staticmethod
    def from_buffer(buf: bytes) -> 'TCPHeader':
        header = TCPHeader()
        memmove(pointer(header), buf, sizeof(header))
        return header

    @staticmethod
    def calc_checksum_static(tcp_header: 'TCPHeader', ip_info: tuple[IPv4Address | IPv6Address, IPv4Address | IPv6Address], opts: bytes, data: bytes) -> int:
        src = ip_info[0]
        dst = ip_info[1]

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

        checksum_header.len = sizeof(tcp_header) + len(opts) + len(data)
        checksum_header.zero = 0
        checksum_header.next_header = 6

        return calc_buf_checksum(bytes(checksum_header) + bytes(tcp_header) + opts + data)

    def calc_checksum(self, ip_info: tuple[IPv4Address | IPv6Address, IPv4Address | IPv6Address], opts: bytes, data: bytes):
        self.checksum = self.calc_checksum_static(self, ip_info, opts, data)

    def read_data_from_buffer(self, buf: bytes) -> bytes:
        return buf[self.offset*4:]

    def get_flags(self) -> TCPHeaderFlags:
        return TCPHeaderFlags.from_header(self)


def unpack_tcp_header(buf: bytes) -> tuple[int, int, dict[str, bool], int, int, bytes]:
    header = TCPHeader.from_buffer(buf)
    src = header.src_port
    dst = header.dst_port

    flags = {}
    flags['urg'] = bool(header.urg)
    flags['ack'] = bool(header.ack)
    flags['psh'] = bool(header.psh)
    flags['rst'] = bool(header.rst)
    flags['syn'] = bool(header.syn)
    flags['fin'] = bool(header.fin)

    data = buf[header.offset*4:]
    return src, dst, flags, int(header.seq_num), int(header.checksum), data


def create_isn() -> int:
    return randint(0x0, 0xFFFF_FFFF)
