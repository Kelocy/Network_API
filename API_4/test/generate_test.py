from src.IPGenerator import IPGenerator
import sys
sys.path.append("..")

cidr_network_ipv4 = "123.45.67.89/27"
cidr_network_ipv6 = "2001:db8::/64"

Add_ipv4 = IPGenerator(cidr_network=cidr_network_ipv4)
Add_ipv6 = IPGenerator(cidr_network=cidr_network_ipv6)

Add_ipv4.print_ip()
Add_ipv6.print_ip()
