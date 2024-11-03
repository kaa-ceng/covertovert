import scapy

# Implement your ICMP sender here

from scapy.all import *

# ICMP packet with ttl 1, destination "172.18.0.3"
packet = IP(dst="172.18.0.3", ttl=1)/ICMP()

send(packet)
