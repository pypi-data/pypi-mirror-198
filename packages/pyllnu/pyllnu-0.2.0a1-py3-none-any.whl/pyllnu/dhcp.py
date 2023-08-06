
from ctypes import (POINTER, BigEndianStructure, c_char, c_ubyte, c_uint8,
                    c_uint16, c_uint32, cast, memmove, pointer, sizeof)
from enum import Enum, auto
from ipaddress import IPv4Address
from typing import Any

from src.pyllnu.constants import *
from src.pyllnu.exceptions import *
from src.pyllnu.ipv4 import ip_to_int


# DHCP EXCHANGE STATUS
# This Enum represents an IP's status on the IP allocation pool.
# If the IP has been offered to a client but not taken, it'S
# marked as offered. If it's taken, it's marked as taken.
# Otherwise, it's marked as free.
class DHCPIPStatus(Enum):
    FREE    = auto()
    OFFERED = auto()
    TAKEN   = auto()


# DHCP MESSAGE BIG-ENDIAN STRUCT
class DHCPMessage(BigEndianStructure):
    _fields_ = [
        ('op',      c_uint8),  # 1 for client, 2 for server
        ('htype',   c_uint8),  # Ethernet: 1
        ('hlen',    c_uint8),  # MAC len: 6
        ('hops',    c_uint8),  # 0
        ('xid',     c_uint32), # Random from 0x0 to 0xffffffff
        ('secs',    c_uint16), # 0
        ('flags',   c_uint16), # 0: Unicast, 1: Broadcast
        ('ciaddr',  c_uint32), # Client's IP address
        ('yiaddr',  c_uint32), # Client's IP address as set by the server
        ('siaddr',  c_uint32), # Next server's IP address
        ('giaddr',  c_uint32), # Relay agent's IP address
        ('chaddr',  c_ubyte * DHCP_MAX_CHADDR_LENGTH), # Client's MAC address
        ('sname',   c_ubyte * DHCP_MAX_SNAME_LENGTH),  # Next server's name
        ('file',    c_ubyte * DHCP_MAX_FILE_LENGTH),   # Name of the file for the client to request from the next server
    ]

    @staticmethod
    def options_to_bytes(options: list[tuple[int, Any]]) -> bytes:
        # CREATE BUFFER
        buf = bytes()

        # MAGIC COOKIE
        buf += (c_ubyte * 4)(99, 130, 83, 99)

        # AUTOMATIC PADDING
        options.append((0, ...))

        for op_code, args in options:
            if op_code == 0:
                while (len(buf)+1) % 16 != 0:
                    buf += c_ubyte(0)
            elif op_code == DHCP_OPTION_MESSAGE_TYPE:
                buf += c_ubyte(op_code)
                buf += c_ubyte(1)
                buf += c_ubyte(args)
            elif op_code == DHCP_OPTION_DNS:
                dns_servers: list[int] = [int(IPv4Address(dns_server)) for dns_server in args]
                buf += c_ubyte(op_code)
                buf += c_ubyte(len(dns_servers) * 4)
                for dns in dns_servers:
                    buf += dns.to_bytes(4, 'big')
            elif op_code == DHCP_OPTION_REQUESTED_ADDRESS or \
                 op_code == DHCP_OPTION_SUBNET_MASK or \
                 op_code == DHCP_OPTION_SERVER_IDENTIFIER:
                buf += c_ubyte(op_code)
                buf += c_ubyte(4)
                buf += int(IPv4Address(args)).to_bytes(4, 'big')
            elif op_code == DHCP_OPTION_ROUTER:
                if not isinstance(args, list):
                    args = [args]
                elif isinstance(args, str):
                    args = [IPv4Address(args)]
                routers: list[int] = [int(IPv4Address(router)) for router in args]
                buf += c_ubyte(DHCP_OPTION_ROUTER)
                buf += c_ubyte(len(routers) * 4)
                for router in routers:
                    buf += router.to_bytes(4, 'big')
            elif op_code == DHCP_OPTION_LEASE_TIME or \
                 op_code == DHCP_OPTION_RENEWAL_TIME or \
                 op_code == DHCP_OPTION_REBINDING_TIME:
                buf += c_ubyte(op_code)
                buf += c_ubyte(4)
                buf += args.to_bytes(4, 'big')

        # 'END' OPTION
        buf += c_ubyte(0xff)

        return buf

    @staticmethod
    def bytes_to_options(buf: bytes) -> dict:
        # IGNORE MAGIC COOKIE (FIRST 4 BYTES)
        nstart = 4
        opts = {}
        while True:
            op_code = cast(buf[nstart:], POINTER(c_ubyte))[0] #type:ignore
            nstart += sizeof(c_ubyte) * 2

            if nstart >= len(buf):
                raise DHCPError('Corrupt message')
            elif op_code == 0:
                continue
            elif op_code == 0xff:
                break
            elif op_code == DHCP_OPTION_MESSAGE_TYPE:
                # Ignore len
                msg_type = cast(buf[nstart:], POINTER(c_ubyte))[0]
                nstart += sizeof(c_ubyte)
                opts[op_code] = msg_type
            elif op_code == DHCP_OPTION_DNS:
                dns = []
                _len = cast(buf[nstart:], POINTER(c_ubyte))[0]
                for i in range(0, _len, sizeof(c_uint32)):
                    if i + sizeof(c_uint32) >= _len:
                        break
                    dns.append(IPv4Address(buf[nstart:nstart+sizeof(c_uint32)][:]))
                    nstart += sizeof(c_uint32)
                opts[op_code] = dns
            elif op_code == DHCP_OPTION_REQUESTED_ADDRESS or \
                 op_code == DHCP_OPTION_SUBNET_MASK or \
                 op_code == DHCP_OPTION_SERVER_IDENTIFIER or \
                 op_code == DHCP_OPTION_ROUTER:
                opts[op_code] = IPv4Address(buf[nstart:nstart+sizeof(c_uint32)][:])
                nstart += sizeof(c_uint32)
            elif op_code == DHCP_OPTION_LEASE_TIME or \
                 op_code == DHCP_OPTION_RENEWAL_TIME or \
                 op_code == DHCP_OPTION_REBINDING_TIME:
                opts[op_code] = int.from_bytes(buf[nstart:nstart+sizeof(c_uint32)], 'big')
                nstart += sizeof(c_uint32)
            elif op_code == DHCP_OPTION_HOST_NAME:
                _len = cast(buf[nstart-1:], POINTER(c_ubyte))[0]
                hostname = cast(buf[nstart:], POINTER(c_char))[:_len]
                nstart += _len
                opts[op_code] = hostname.decode('utf-8')
            else:
                print(f'[DHCP] WARN: RECEIVED UNKNOWN OPCODE {op_code}')
                nstart += cast(buf[nstart-1:], POINTER(c_ubyte))[0]
        return opts


    @staticmethod
    def unpack_msg(buf: bytes) -> tuple['DHCPMessage', dict]:
        msg = buf[:sizeof(DHCPMessage)]
        opts = buf[sizeof(DHCPMessage):]
        hdr = DHCPMessage()
        memmove(pointer(hdr), msg, sizeof(hdr))
        return hdr, DHCPMessage.bytes_to_options(opts)


def allocate_ip(pool: dict[IPv4Address, DHCPIPStatus]) -> IPv4Address:
    ip = next((ip for ip, status in pool.items() if status == DHCPIPStatus.FREE), None)
    if not ip:
        raise DHCPError('No free IPs')
    return ip


def build_dhcp_answer(xid, their_ip, chaddr) -> DHCPMessage:
    answr = DHCPMessage()
    answr.op = DHCP_BOOTREPLY
    answr.htype = 1
    answr.hlen = 6
    answr.hops = 0
    answr.xid = xid
    answr.secs = 0
    answr.flags = 0
    answr.ciaddr = 0
    answr.yiaddr = ip_to_int(their_ip)
    answr.siaddr = 0
    answr.giaddr = 0
    answr.chaddr = chaddr
    answr.sname = (c_ubyte * DHCP_MAX_SNAME_LENGTH)()
    answr.file = (c_ubyte * DHCP_MAX_FILE_LENGTH)()
    return answr


def build_dhcp_answer_options(msg_type, our_ip, our_mask, default_gateway, dns_servers) -> bytes:
    return DHCPMessage.options_to_bytes([
        (DHCP_OPTION_MESSAGE_TYPE,      msg_type),
        (DHCP_OPTION_SUBNET_MASK,       our_mask),
        (DHCP_OPTION_RENEWAL_TIME,      1800),
        (DHCP_OPTION_REBINDING_TIME,    3150),
        (DHCP_OPTION_LEASE_TIME,        3600),
        (DHCP_OPTION_SERVER_IDENTIFIER, our_ip),
        (DHCP_OPTION_ROUTER,            default_gateway),
        (DHCP_OPTION_DNS,               dns_servers)
    ])


def offer(rcvd_msg: DHCPMessage, _: dict, our_ip, our_mask, default_gateway, dns_servers, their_ip) -> bytes:
    answr = build_dhcp_answer(rcvd_msg.xid, their_ip, rcvd_msg.chaddr)
    options = build_dhcp_answer_options(DHCP_OFFER, our_ip, our_mask, default_gateway, dns_servers)
    dhcp_bytes = bytes(answr) + options #type: ignore
    while len(dhcp_bytes) % 16 != 0:
        dhcp_bytes += c_ubyte(0)
    return dhcp_bytes


def ack(rcvd_msg: DHCPMessage, _: dict, our_ip, our_mask, default_gateway, dns_servers, their_ip) -> bytes:
    answr = build_dhcp_answer(rcvd_msg.xid, their_ip, rcvd_msg.chaddr)
    options = build_dhcp_answer_options(DHCP_ACK, our_ip, our_mask, default_gateway, dns_servers)
    dhcp_bytes = bytes(answr) + options #type: ignore
    while len(dhcp_bytes) % 16 != 0:
        dhcp_bytes += c_ubyte(0)
    return dhcp_bytes
