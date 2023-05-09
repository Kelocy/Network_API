import unittest
from src.IPGenerator import IPGenerator


class ClientTest(unittest.TestCase):
    def test_generate_ipv4(self):
        ipv4 = "123.45.67.89/27"
        Address_ipv4 = IPGenerator(cidr_network=ipv4)
        ipv4_list = Address_ipv4.ip_list()

    def test_generate_ipv6(self):
        ipv6 = "2001:db8::/120"
        Address_ipv6 = IPGenerator(cidr_network=ipv6)
        ipv6_list = Address_ipv6.ip_list()
