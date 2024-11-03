import scapy

# Implement your ICMP sender here

from scapy.all import *

# ICMP packet with ttl 1
packet = IP(dst="receiver", ttl=1)/ICMP()

send(packet)
