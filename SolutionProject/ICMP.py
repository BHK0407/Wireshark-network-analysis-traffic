import pyshark

capture_file = r"C:\Users\Admin\Desktop\Cybersecurity\Wireshark capture\Comprehending ICMP\icmp fragmented.cap"

capture = pyshark.FileCapture(capture_file)

total_icmp_packets = 0
fragmented_icmp_packets = 0

print("ICMP Packets Details:")
print("----------------------")

for packet in capture:
    # Check if the packet is an ICMP packet
    if "ICMP" in packet:
        total_icmp_packets += 1
        icmp_type = packet.icmp.type
        icmp_code = packet.icmp.code
        src_ip = packet.ip.src
        dst_ip = packet.ip.dst
        print(f"Packet {total_icmp_packets}:")
        print(f"    Source IP: {src_ip}")
        print(f"    Destination IP: {dst_ip}")
        print(f"    ICMP Type: {icmp_type}")
        print(f"    ICMP Code: {icmp_type}")
        # Check if the packet is fragmented
        try:
            if packet.icmp.fragment_count:
                fragmented_icmp_packets += 1
                print("    Fragmented: Yes")
        except AttributeError:
            pass
        print()
# Close the capture file
capture.close()

# Display statistics
print("Total ICMP packets: ", total_icmp_packets)
print("Fragmented ICMP packets: ", fragmented_icmp_packets)
