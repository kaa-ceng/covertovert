import scapy

# Implement your ICMP receiver here

from scapy.all import sniff, ICMP, IP 

def receiver(packet):
    # packet has an ICMP layer and its ttl value is 1
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        packet.show() 

sniff(filter="icmp", prn=receiver)

