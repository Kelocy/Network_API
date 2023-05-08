import unittest
from src.server import ServerTCP
from src.client import Client
import threading


class ClientTest(unittest.TestCase):
    def setUp(self):
        HOST, PORT = "localhost", 9999
        self.server = ServerTCP(HOST, PORT)
        server_thread = threading.Thread(target=self.server.start())
        server_thread.start()

    def test_client_start(self):
        HOST, PORT = "localhost", 9999
        client = Client(HOST, PORT)

    def test_client_host_port_start(self):
        HOST, PORT = "2749329", 432321
        client = Client(HOST, PORT)

    def test_client_msg(self):
        HOST, PORT = "localhost", 9999
        client = Client(HOST, PORT)
        data, response = client.start()
        print(data, response)


if __name__ == "__main__":
    unittest.main()
