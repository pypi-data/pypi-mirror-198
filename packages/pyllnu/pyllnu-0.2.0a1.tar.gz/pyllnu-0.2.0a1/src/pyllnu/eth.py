
import ctypes
import socket
import struct
from ipaddress import IPv4Address, IPv6Address, ip_address
from typing import NewType

from src.pyllnu import util
from src.pyllnu.constants import *

ETHHeader = NewType('Header', bytes)


def create_and_bind_socket(iface: str, port: int = 0) -> socket.SocketType:
    s = create_socket()
    s.bind((iface, port))
    return s


def create_socket() -> socket.SocketType:
    return socket.socket(
        socket.AF_PACKET,
        socket.SOCK_RAW,
        socket.htons(ETH_P_ALL)
    )


def mac_str_to_int_list(mac: str) -> list[int]:
    return [int(m, 16) for m in mac.split(':')]


def mac_to_byte_array(mac: list[int] | str) -> ctypes.Array:
    if isinstance(mac, str):
        mac = mac_str_to_int_list(mac)
    return (ctypes.c_ubyte * 16)(*mac)


def get_mac_data(iface: str) -> tuple[list[int], str]:
    return util.get_mac_data()


def pack_eth_header(src: list[int], dst: list[int], packet_type: int) -> ETHHeader:
    return ETHHeader(struct.pack(ETH_HEADER_FMT, *dst, *src, packet_type))


def unpack_eth_header(buf: bytes) -> tuple[str, str, int]:
    if len(buf) > 14:
        buf = ETHHeader(buf[:14])
    data = struct.unpack(ETH_HEADER_FMT, buf)
    dst = ':'.join(f'{hex(b)[2:].upper():>02}' for b in data[:6])
    src = ':'.join(f'{hex(b)[2:].upper():>02}' for b in data[6:12])
    packet_type = int(data[12:14][0])
    return src, dst, packet_type


def get_default_gateway_mac(gateway: IPv4Address | IPv6Address) -> str:
    with open('/proc/net/arp') as f:
        f.readline()
        for line in f:
            fields = line.split()
            try:
                if ip_address(fields[0]) == gateway:
                    return fields[3]
            except ValueError:
                continue
    raise ValueError('Could not get MAC for default gateway')
