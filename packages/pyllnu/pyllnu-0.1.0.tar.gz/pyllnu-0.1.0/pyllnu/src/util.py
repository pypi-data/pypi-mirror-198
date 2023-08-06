
import socket
from ctypes import BigEndianStructure, memmove, pointer, sizeof
from ipaddress import ip_address
from typing import Any

from pyllnu.src.constants import *
from pyllnu.src.exceptions import *


def load_cls_from_buffer(_class: BigEndianStructure, buf: bytes):
    header = _class()
    memmove(pointer(header), buf, sizeof(header))
    return header


def calc_pseudo_header_checksum(ip_src: str, ip_dst: str, protocol: int, hdr_len: int) -> int:
    _ip_src = ip_address(ip_src)
    _ip_dst = ip_address(ip_dst)
    
    _sum_phdr = int(_ip_src) + int(_ip_dst) + protocol + hdr_len
    return _sum_phdr


def calc_buf_checksum(buf: bytes) -> int:
    _sum = 0 
    for i in range(0, len(buf), 2):
        a = buf[i]
        try:
            b = buf[i + 1]
        except IndexError:
            break
        _sum += a + (b << 8)
    _sum += _sum >> 16
    _sum = ~_sum & 0xffff
    _sum = socket.htons(_sum)
    return _sum


def eth_packet_type_to_str(packet_id: int) -> ETHPacketType:
    try:
        return ETHPacketType(packet_id)
    except TypeError:
        raise TypeError('Unknown packet')


def get_application_layer_protocol_from_port(dst_port: int) -> str:
    try:
        return \
            f'{ApplicationPortType(dst_port).name} ({ApplicationPortType(dst_port).value})'
    except ValueError:
        return f'Unknown destination port: {dst_port}'


def get_other_key(dict_keys: dict[str, Any], ignore_key: str = 'next') -> str:
    return list(set(dict_keys.keys()) - {ignore_key})[0]
