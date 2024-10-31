import scapy

# Implement your ICMP sender here


from scapy.all import IP, ICMP, send

# Set the IP address of the receiver container
receiver_ip = "172.18.0.2"  # Replace with the actual IP of the receiver container

# Create an ICMP packet with TTL value set to 1
packet = IP(dst=receiver_ip, ttl=1)/ICMP()

# Send the ICMP packet
send(packet)
print(f"ICMP packet sent to {receiver_ip} with TTL=1")

