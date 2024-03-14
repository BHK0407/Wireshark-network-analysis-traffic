# Network Protocol Analysis with Wireshark and Python

## Objective:

The objective of this project is to analyze network protocols using Wireshark and Python scripting. Specifically, we'll focus on understanding ICMP (Internet Control Message Protocol) and IPv6 Neighbor Discovery Protocol (NDP) using captured network traffic.

## Tools Required:

- Wireshark: A network protocol analyzer.
- Python 3.x: For scripting and data analysis.
- Libraries: pyshark (a Python wrapper for Wireshark) and other necessary libraries.

## Steps:

1. Capture Network Traffic:

Use Wireshark to capture network traffic for ICMP and IPv6 NDP scenarios. Save the captures as .cap files.

2. Analyze ICMP Traffic:

- Load the icmp.fragmented.cap file into Wireshark.
- Identify ICMP packets and analyze their structure, including fragmented packets.
- Use Python with the pyshark library to extract and analyze ICMP packets programmatically.
- Display relevant statistics and information about ICMP traffic.

3. Analyze MPLS-Traceroute Traffic:

- Load the traceroute_MPLS.cap file into Wireshark.
- Analyze the traceroute packets and understand how MPLS (Multiprotocol - Label Switching) affects the routing.
- Utilize Python and pyshark to extract MPLS-related information and analyze the traceroute packets.
- Display MPLS-related statistics and insights.

4. Analyze IPv6 NDP Traffic:

- Load the IPv6_NDP.cap file into Wireshark.
- Identify IPv6 Neighbor Discovery Protocol packets and understand their purpose.
- Use Python and pyshark to extract NDP packets and analyze their contents programmatically.
- Display NDP-related statistics and insights.

5. Integration and Reporting:

- Combine the analysis from all three scenarios (ICMP, MPLS-Traceroute, and IPv6 NDP).
- Generate a comprehensive report summarizing the findings, including packet statistics, protocol behavior, and any noteworthy observations.
- Utilize Python libraries like matplotlib or seaborn to create visualizations for better understanding.
Optionally, create interactive dashboards or visualizations for deeper exploration.

## Conclusion:


In conclusion, this project offers a practical exploration of network protocol analysis through the combined use of Wireshark and Python. By dissecting actual network traffic captures, participants gain valuable insights into the intricacies of ICMP, MPLS, and IPv6 NDP protocols. This hands-on approach not only enhances understanding of network communications but also equips individuals with valuable troubleshooting skills. Through this project, participants can delve deeper into the nuances of network behavior, empowering them to make informed decisions and effectively manage network infrastructures.





