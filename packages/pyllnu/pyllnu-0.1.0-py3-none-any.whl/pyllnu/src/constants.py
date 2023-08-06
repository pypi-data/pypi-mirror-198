
from enum import Enum
from ipaddress import IPv4Address

################################################################################
# ETHERNET CONSTANTS
################################################################################

ETH_DEFAULT_NET_IFACE = 'eth0'

ETH_FRAME_SIZE = 1518
ETH_P_ALL = 3
ETH_HEADER_FMT = '!6B6BH'
ETH_MAC_BROADCAST = 'FF:FF:FF:FF:FF:FF'


################################################################################
# IPV4 CONSTANTS
################################################################################

IPV4_LOCALHOST = IPv4Address('127.0.0.1')
IPV4_BROADCAST = IPv4Address('255.255.255.255')

IPV4_PACKET_TYPE = 0x0800


################################################################################
# IPV6 CONSTANTS
################################################################################

IPV6_PACKET_TYPE = 0x86DD

IPV6_HEADER_VERSION = 0x6  # 1 nibble
IPV6_HEADER_TRAFFIC_CLASS = 0x0  # 8 bits
IPV6_HEADER_FLOW_LABEL = 0x0  # 20 bits
IPV6_HEADER_NEXT_HEADER = 0x6  # 8 bits
IPV6_HEADER_HOP_LIMIT = 0xff  # 8 bits


################################################################################
# TCP CONSTANTS
################################################################################

TCP_PROTOCOL = 6


################################################################################
# UDP CONSTANTS
################################################################################

UDP_PROTOCOL = 17


################################################################################
# DHCP CONSTANTS
################################################################################

# PORTS
DHCP_SERVER_PORT = 67
DHCP_CLIENT_PORT = 68

# BOOTP MESSAGE OP ID
DHCP_BOOTREQUEST = 1
DHCP_BOOTREPLY   = 2

# OPTIONS
DHCP_OPTION_SUBNET_MASK       = 1
DHCP_OPTION_ROUTER            = 3
DHCP_OPTION_DNS               = 6
DHCP_OPTION_HOST_NAME         = 12
DHCP_OPTION_BROADCAST_ADDRESS = 28
DHCP_OPTION_REQUESTED_ADDRESS = 50
DHCP_OPTION_LEASE_TIME        = 51
DHCP_OPTION_MESSAGE_TYPE      = 53
DHCP_OPTION_SERVER_IDENTIFIER = 54
DHCP_OPTION_RENEWAL_TIME      = 58
DHCP_OPTION_REBINDING_TIME    = 59

# `DHCP_OPTION_MESSAGE_TYPE` TYPES
DHCP_DISCOVER = 1
DHCP_OFFER    = 2
DHCP_REQUEST  = 3
DHCP_DECLINE  = 4
DHCP_ACK      = 5
DHCP_NACK     = 6
DHCP_RELEASE  = 7

# FIELD LENGTHS
DHCP_MAX_CHADDR_LENGTH           = 16
DHCP_MAX_SNAME_LENGTH            = 64
DHCP_MAX_FILE_LENGTH             = 128
DHCP_ETHERNET_HARDWARE_ADDRESS        = 1  #/* used in htype field of dhcp packet */
DHCP_ETHERNET_HARDWARE_ADDRESS_LENGTH = 6  #/* length of Ethernet hardware addresses */

# MISC DEFINITIONS
DHCP_INFINITE_TIME = 0xffffffff
DHCP_BROADCAST_FLAG = 32768


################################################################################
# ICMP CONSTANTS
################################################################################

ICMP_PROTOCOL = 1


################################################################################
# ARP CONSTANTS
################################################################################

ARP_PACKET_TYPE = 0x0806


################################################################################
# DNS CONSTANTS
################################################################################

DNS_PORT = 53


################################################################################
# HTTP CONSTANTS
################################################################################

HTTP_PORT = 80
HTTPS_PORT = 443


################################################################################
# PACKET TYPE CONSTANTS
################################################################################

class ETHPacketType(Enum):
    IPV4 = IPV4_PACKET_TYPE
    IPV6 = IPV6_PACKET_TYPE
    ARP  = ARP_PACKET_TYPE


class IPProtocolType(Enum):
    TCP  = TCP_PROTOCOL
    UDP  = UDP_PROTOCOL
    ICMP = ICMP_PROTOCOL


class ApplicationPortType(Enum):
    SSH = 22
    DNS = 53
    DHCP_SERVER = 67
    DHCP_CLIENT = 68
    HTTP = 80
    HTTPS = 443
