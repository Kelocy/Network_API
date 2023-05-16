"""Test client function
"""
import unittest
import threading
import time
from src.client.HTTP_client import HTTPClient
from src.server.TCP_server import MyTCPServer
from src.client.TCP_client import MyTCPClient
from src.server.UDP_server import MyUDPServer
from src.client.UDP_client import MyUDPClient
from src.IPGenerator import IPGenerator
from src.server.xmlrpc_server import XmlrpcServer
from src.client.xmlrpc_client import XmlrpcClient
from src.server.ssl_server import SslServer
from src.client.ssl_client import SslClient
import os


# API_1
class HTTPTest(unittest.TestCase):
    """Two test functions test the client class
    """

    def setUp(self):
        """Setup a client with url
        """
        self.client = HTTPClient()

    def test_get(self):
        """Get function will pull data from the url
        """
        url = "https://jsonplaceholder.typicode.com/posts"
        return_data = self.client.get(url)
        self.assertIsNotNone(return_data)
        # print(return_data)

    def test_post(self):
        """Post function will send data to url and receive the response
        """
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        data_expect_response = {
            "id": 101,
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!",
        }
        url = "https://jsonplaceholder.typicode.com/posts"
        return_response = self.client.post(url, data_post)
        return_data = self.client.get(return_response)
        self.assertEqual(return_data, data_expect_response)
        # print(return_data)

    def test_put(self):
        """Post function will send data to url and receive the response
        """
        data_post = {
            "id": 1,
            "name": "JOJO",
            "email": "jojo@example.com",
            "message": "My best day!"
        }
        url = "https://jsonplaceholder.typicode.com/posts/1"
        return_response = self.client.put(url, data_post)
        return_data = self.client.get(return_response)
        self.assertEqual(return_data, data_post)
        # print(return_data)

    def test_delete(self):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        return_response = self.client.delete(url)
        return_data = self.client.get(return_response)
        # print(return_data)
        self.assertEqual(return_data, {})


# API_2
class TCPTest(unittest.TestCase):
    """Two test functions test the client class
    """

    def test_tcp(self):
        HOST, PORT = "localhost", 9900
        server = MyTCPServer(HOST, PORT)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()

        time.sleep(1)

        client = MyTCPClient(HOST, PORT)
        data = "Hello World!"
        return_data = client.start_tcp(data)
        self.assertEqual(data, return_data)
        server.close()


# API_3
class UDPTest(unittest.TestCase):
    def test_udp(self):
        HOST, PORT = "localhost", 9989
        server = MyUDPServer(HOST, PORT)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()

        time.sleep(1)

        client = MyUDPClient(HOST, PORT)
        data = "Hello World!"
        return_data = client.start_udp(data)
        self.assertEqual(data, return_data)
        server.close()


# API_4
class IPGeneratorTest(unittest.TestCase):
    def test_generate_ipv4(self):
        ipv4 = "123.45.67.89/27"
        Address_ipv4 = IPGenerator(cidr_network=ipv4)
        file_path = os.path.join(os.path.dirname(__file__), './etc/ipv4.txt')

        data = file_to_list(file_path)
        self.assertEqual(data, Address_ipv4.ip_list())
        # ipv4_list = Address_ipv4.ip_list()

    def test_generate_ipv6(self):
        ipv6 = "2001:db8::/120"
        Address_ipv6 = IPGenerator(cidr_network=ipv6)
        file_path = os.path.join(os.path.dirname(__file__), './etc/ipv6.txt')

        data = file_to_list(file_path)
        self.assertEqual(data, Address_ipv6.ip_list())
        # ipv6_list = Address_ipv6.ip_list()


# API_6
class XmlrpcTest(unittest.TestCase):
    def test_run(self):
        HOST, PORT = 'localhost', 8000
        server = XmlrpcServer(HOST, PORT)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()

        time.sleep(1)

        client = XmlrpcClient(HOST, PORT)
        response = client.start(13, 45)
        self.assertEquals(58, response)
        server.close()


# API_7
class SslTest(unittest.TestCase):
    def test_run(self):
        HOST, PORT = "localhost", 9999
        cert_server = 'src/server/etc/cert.pem'
        key_server = 'src/server/etc/key.pem'
        # cert_server = os.path.join(
        #     os.path.dirname(__file__), 'src/server/etc/cert.pem')
        # key_server = os.path.join(
        #     os.path.dirname(__file__), 'src/server/etc/key.pem')
        server = SslServer(HOST, PORT, cert_server, key_server)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()

        time.sleep(1)

        cert_client = 'src/client/etc/cert.pem'
        # cert_client = os.path.join(
        #     os.path.dirname(__file__), 'src/client/etc/cert.pem')
        client = SslClient(HOST, PORT, cert_client)
        data = "Hello World!"

        response = client.start(data)
        self.assertEquals(data, response)


def file_to_list(name):     # ipv4 / ipv6
    with open(name, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines


if __name__ == "__main__":
    unittest.main()
