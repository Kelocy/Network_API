from src.IPGenerator import IPGenerator

cidr_network_ipv4 = "123.45.67.89/27"
cidr_network_ipv6 = "2001:db8::/120"

Add_ipv4 = IPGenerator(cidr_network=cidr_network_ipv4)
Add_ipv6 = IPGenerator(cidr_network=cidr_network_ipv6)

ipv4_list = Add_ipv4.ip_list()
ipv6_list = Add_ipv6.ip_list()

with open('ipv4.txt', mode='wt') as file:
    for item in ipv4_list:
        file.write(str(item) + '\n')

with open('ipv6.txt', mode='wt') as file:
    for item in ipv6_list:
        file.write(str(item) + '\n')

Add_ipv4.print_ip()
Add_ipv6.print_ip()
