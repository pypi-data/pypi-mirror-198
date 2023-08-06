from ctypes import sizeof
from typing import Any

from src.pyllnu.constants import ETHPacketType, IPProtocolType
from src.pyllnu.eth import unpack_eth_header
from src.pyllnu.exceptions import UnknownProtocolError
from src.pyllnu.ipv4 import IPv4Header
from src.pyllnu.ipv6 import IPv6Header
from src.pyllnu.tcp import TCPHeader
from src.pyllnu.udp import UDPHeader
from src.pyllnu.util import get_application_layer_protocol_from_port, get_other_key


def parse_buffer(buf: bytes):
    mac_src, mac_dst, packet_type = unpack_eth_header(buf[:14])

    match packet_type:
        case ETHPacketType.IPV4.value:
            parsed = parse_ipv4_buffer(buf[14:])
        case ETHPacketType.IPV6.value:
            parsed = parse_ipv6_buffer(buf[14:])
        case ETHPacketType.ARP.value:
            raise NotImplementedError('ARP Protocol hasn\'t been implemented yet.')
        case _:
            raise UnknownProtocolError

    return {
        'eth': {
            'mac source': mac_src,
            'mac destination': mac_dst,
            'packet type': packet_type
        },
        'next': parsed
    }


def parse_ipv4_buffer(buf: bytes) -> dict[str, Any]:
    hdr = IPv4Header.from_buffer(buf)

    match hdr.protocol:
        case IPProtocolType.TCP.value:
            parsed = parse_tcp_buffer(buf[sizeof(hdr):])
        case IPProtocolType.UDP.value:
            parsed = parse_udp_buffer(buf[sizeof(hdr):])
        case IPProtocolType.ICMP.value:
            parsed = parse_icmp_buffer(buf[sizeof(hdr):])
        case _:
            parsed = {}

    return {
        'ipv4': hdr.get_properties(),
        'next': parsed
    }


def parse_ipv6_buffer(buf: bytes) -> dict[str, Any]:
    hdr = IPv6Header.from_buffer(buf)

    match hdr.protocol:
        case IPProtocolType.TCP.value:
            parsed = parse_tcp_buffer(buf[sizeof(hdr):])
        case IPProtocolType.UDP.value:
            parsed = parse_udp_buffer(buf[sizeof(hdr):])
        case IPProtocolType.ICMP.value:
            parsed = parse_icmpv6_buffer(buf[sizeof(hdr):])
        case _:
            parsed = {}

    return {
        'ipv6': hdr.get_properties(),
        'next': parsed
    }


def parse_ip_buffer(buf: bytes, hdr: IPv4Header | IPv6Header) -> dict[str, Any]:
    match hdr.protocol:
        case IPProtocolType.TCP.value:
            parsed = parse_tcp_buffer(buf[sizeof(hdr):])
        case IPProtocolType.UDP.value:
            parsed = parse_udp_buffer(buf[sizeof(hdr):])
        case IPProtocolType.ICMP.value:
            parsed = parse_icmp_buffer(buf[sizeof(hdr):])
        case _:
            parsed = {}

    match hdr:
        case IPv4Header():
            type_key = 'ipv4'
        case IPv6Header():
            type_key = 'ipv6'

    return {
        type_key: hdr.get_properties(),
        'next': parsed
    }


def parse_tcp_buffer(buf: bytes) -> dict[str, Any]:
    hdr = TCPHeader.from_buffer(buf)
    return {
        'tcp': hdr.get_properties(),
        'next': {
            get_application_layer_protocol_from_port(hdr.dst_port): buf[sizeof(hdr):]
        }
    }


def parse_udp_buffer(buf: bytes) -> dict[str, Any]:
    hdr = UDPHeader.from_buffer(buf)
    return {
        'udp': hdr.get_properties(),
        'next': {
            get_application_layer_protocol_from_port(hdr.dst_port): buf[sizeof(hdr):]
        }
    }


def parse_icmp_buffer(buf: bytes) -> dict[str, Any]:
    raise NotImplementedError('ICMP support coming soon')


def parse_icmpv6_buffer(buf: bytes) -> dict[str, Any]:
    raise NotImplementedError('ICMP support coming soon')


def get_protocols(parsed_buf: dict[str, Any]) -> list[str]:
    aux_dict = parsed_buf
    res = [get_other_key(parsed_buf)]
    while 'next' in aux_dict:
        aux_dict = aux_dict['next']
        
        if not aux_dict:
            break
        
        res.append(get_other_key(aux_dict))
    return res
