"""Test client function
"""
import unittest
import threading
from src.server import ServerTCP, ServerUDP
from src.client import Client
import time


class ServiceTest(unittest.TestCase):
    """Two test functions test the client class
    """

    def test_tcp(self):
        HOST, PORT = "localhost", 9900
        server = ServerTCP(HOST, PORT)
        server_once = server.start_once()
        server_thread = threading.Thread(target=server_once.serve_forever)
        server_thread.start()

        time.sleep(1)

        client = Client(HOST, PORT)
        data = "Hello World!"
        return_data = client.start_tcp(data)
        self.assertEqual(data, return_data)
        server_once.shutdown()

    def test_udp(self):
        HOST, PORT = "localhost", 9989
        server = ServerUDP(HOST, PORT)
        server_once = server.start_once()
        server_thread = threading.Thread(target=server_once.serve_forever)
        server_thread.start()

        time.sleep(1)

        client = Client(HOST, PORT)
        data = "Hello World!"
        return_data = client.start_udp(data)
        self.assertEqual(data, return_data)
        server_once.shutdown()


if __name__ == "__main__":
    unittest.main()
