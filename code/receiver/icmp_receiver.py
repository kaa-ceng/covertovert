import scapy

# Implement your ICMP receiver here



from scapy.all import sniff, ICMP, IP 

# Define a function to handle incoming packets
def handle_packet(packet):
    # Check if the packet has an ICMP layer and its TTL value is 1
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        packet.show()  # Display detailed information about the packet

# Listen for ICMP packets on all interfaces
sniff(filter="icmp", prn=handle_packet)

