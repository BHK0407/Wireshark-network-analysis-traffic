import pyshark
import matplotlib.pyplot as plt

def extract_icmp_info(packet):
    icmp_info = {}
    icmp_info['Type'] = int(packet.icmp.type)
    icmp_info['Code'] = int(packet.icmp.code)
    icmp_info['Source IP'] = packet.ip.src
    icmp_info['Destination IP'] = packet.ip.dst
    icmp_info['TTL'] = int(packet.ip.ttl) if 'IP' in packet else None
    return icmp_info

def print_icmp_info(icmp_info):
    print(f"    ICMP Type: {icmp_info['Type']}")
    print(f"    ICMP Code: {icmp_info['Code']}")
    print(f"    Source IP: {icmp_info['Source IP']}")
    print(f"    Destination IP: {icmp_info['Destination IP']}")
    if icmp_info['TTL'] is not None:
        print(f"    TTL: {icmp_info['TTL']}")

def main():
    capture_file = r"C:\Users\Admin\Desktop\Cybersecurity\Wireshark capture\Comprehending ICMP\traceroute_MPLS.cap"

    capture = pyshark.FileCapture(capture_file)

    icmp_packets = 0
    icmp_info_list = []

    print("ICMP Packets Details:")
    print("----------------------")
    for packet in capture:
        # Check if the packet is an ICMP packet
        if "ICMP" in packet:
            icmp_packets += 1
            # Extract ICMP-related information
            icmp_info = extract_icmp_info(packet)
            icmp_info_list.append(icmp_info)  # Append icmp_info to the list
            print(f"ICMP Packet {icmp_packets}:")
            print_icmp_info(icmp_info)
            print()

    # Close the capture file
    capture.close()

    # Calculate statistics
    icmp_types = [info['Type'] for info in icmp_info_list]
    icmp_codes = [info['Code'] for info in icmp_info_list]
    ttl_values = [info['TTL'] for info in icmp_info_list if info['TTL'] is not None]

    # Plot distribution of ICMP types
    plt.figure(figsize=(8, 6))
    plt.hist(icmp_types, bins=range(min(icmp_types), max(icmp_types) + 1), alpha=0.5)
    plt.xlabel("ICMP Type")
    plt.ylabel("Frequency")
    plt.title("Distribution of ICMP Types")
    plt.grid(True)
    plt.show()
    # Plot distribution of ICMP codes
    plt.figure(figsize=(8, 6))
    plt.hist(icmp_codes, bins=range(min(icmp_codes), max(icmp_codes) + 1), alpha=0.5)
    plt.xlabel('ICMP Code')
    plt.ylabel('Frequency')
    plt.title('Distribution of ICMP Codes')
    plt.grid(True)
    plt.show()

    # Plot distribution of TTL values
    plt.figure(figsize=(8, 6))
    plt.hist(ttl_values, bins=range(min(ttl_values), max(ttl_values) + 1), alpha=0.5)
    plt.xlabel('TTL')
    plt.ylabel('Frequency')
    plt.title('Distribution of TTL Values')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
