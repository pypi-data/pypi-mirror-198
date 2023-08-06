# [Python Low-Level Network Utils](https://gitlab.com/debemdeboas/python-low-level-network-utils)

<div align="center">
    <img src="https://gitlab.com/debemdeboas/python-low-level-network-utils/-/raw/main/doc/img/wireshark-hello-world.png" />
</div>

PyLLNU implements the following protocols:

- Ethernet
- ICMP
- IPv4
- IPv6
- TCP
- UDP
- DHCP

This package allows developers to interact more easily with
raw sockets.
You can create IPv4 and IPv6 headers and packets and even build your own protocols.

Raw sockets operate on [OSI layer 2](https://osi-model.com/network-layer/), the Data Link Layer. This layer is also known as the layer in which the Ethernet protocol operates.
