import time
from ctypes import sizeof

from src import constants, eth, ipv4, ipv6, tcp, udp, util
import json
from src.parser import *


dst_ip = '142.251.129.206'
dst_ipv6 = '2800:3f0:4001:820::200e'
eth_iface = 'eth0'

sock = eth.create_and_bind_socket(eth_iface, 9874)
mac_src, mac_src_str = eth.get_mac_data(eth_iface)

our_ip, _ = ipv4.get_our_ip_and_net_mask(eth_iface)
default_gateway_ip = ipv4.get_default_gateway(eth_iface)
default_gateway_mac_str = eth.get_default_gateway_mac(default_gateway_ip)
default_gateway_mac = eth.mac_str_to_int_list(default_gateway_mac_str)

# payload = int(305419896).to_bytes(4, 'big')
payload = b'hello world!'

udp_hdr = udp.UDPHeader.create(9874, 9874, len(payload))

ipv4_hdr = ipv4.IPv4Header.create(our_ip,
                                  dst_ip,
                                  sizeof(udp_hdr) + len(payload),
                                  constants.UDP_PROTOCOL)

ipv6_hdr = ipv6.IPv6Header.create('::1',
                                  dst_ipv6,
                                  sizeof(udp_hdr) + len(payload),
                                  constants.UDP_PROTOCOL)

udp_hdr.calc_checksum(('::1', dst_ipv6), payload)

# ip_hdr = ipv4_hdr
ip_hdr = ipv6_hdr

# eth_hdr = eth.pack_eth_header(mac_src,
#                               default_gateway_mac,
#                               constants.IPV4_PACKET_TYPE)
eth_hdr = eth.pack_eth_header(mac_src,
                              default_gateway_mac,
                              constants.IPV6_PACKET_TYPE)

# while True:
#     print(f'Sending {len(eth_hdr + ip_hdr + udp_hdr + payload)} bytes of data')
#     sock.send(eth_hdr + ip_hdr + udp_hdr + payload)
#     time.sleep(1)

test_buffer = b'\x00\x15\x5d\xaf\x29\xf0\x00\x15\x5d\xf2\xaa\xcc\x08\x00\x45\x00' \
              b'\x00\x3c\xa4\xa8\x40\x00\x40\x06\xb3\x04\xac\x1f\xbb\xfe\x33\x69' \
              b'\x47\x88\x93\xf8\x01\xbb\x93\xb4\x87\xd4\x00\x00\x00\x00\xa0\x02' \
              b'\xfa\xf0\xf7\x70\x00\x00\x02\x04\x05\xb4\x04\x02\x08\x0a\xef\x7c' \
              b'\xd1\xd5\x00\x00\x00\x00\x01\x03\x03\x07'

sock = eth.create_socket()

while True:
    data, iface_info = sock.recvfrom(4096)
    
    eth_hdr = eth.unpack_eth_header(data)
    
    if mac_src_str not in (eth_hdr[0], eth_hdr[1]):
        continue

    try:
        buf_data = parse_buffer(data)
    except NotImplementedError:
        continue

    print(get_protocols(buf_data))

    # print(
    #     json.dumps(
    #         buf_data,
    #         indent=2,
    #         sort_keys=True,
    #         default=lambda o: f'<<non-serializable: {type(o).__qualname__}>>'
    #     )
    # )
