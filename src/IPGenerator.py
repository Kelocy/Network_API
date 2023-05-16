import ipaddress


class IPGenerator():
    def __init__(self, cidr_network):
        try:
            self.network = ipaddress.ip_network(cidr_network, strict=False)
        except ValueError:
            raise ValueError("Invalid IP Address")
        self.ip_version = "ipv4" if self.network.version == 4 else "ipv6"
        self.ip_address = [str(ip) for ip in self.network]

    def ip_list(self):
        return self.ip_address

    def print_ip(self):
        for ip in self.ip_address:
            print(ip)
