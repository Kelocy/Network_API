import unittest
from src.IPGenerator import IPGenerator
import os


class ServiceTest(unittest.TestCase):
    def test_generate_ipv4(self):
        ipv4 = "123.45.67.89/27"
        Address_ipv4 = IPGenerator(cidr_network=ipv4)
        file_path = os.path.join(os.path.dirname(__file__), 'ipv4.txt')

        data = file_to_list(file_path)
        self.assertEqual(data, Address_ipv4.ip_list())
        # ipv4_list = Address_ipv4.ip_list()

    def test_generate_ipv6(self):
        ipv6 = "2001:db8::/120"
        Address_ipv6 = IPGenerator(cidr_network=ipv6)
        file_path = os.path.join(os.path.dirname(__file__), 'ipv6.txt')

        data = file_to_list(file_path)
        self.assertEqual(data, Address_ipv6.ip_list())
        # ipv6_list = Address_ipv6.ip_list()


def file_to_list(name):     # ipv4 / ipv6
    with open(name, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines


if __name__ == "__main__":
    unittest.main()
