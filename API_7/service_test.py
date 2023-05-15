"""Test client function
"""
import unittest
import threading
from src.server.server import Server
from src.client.client import Client
import time


class ServiceTest(unittest.TestCase):
    def test_run(self):
        HOST, PORT = "localhost", 9999
        cert_server, key_server = 'src/server/cert.pem', 'src/server/key.pem'
        server = Server(HOST, PORT, cert_server, key_server)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()

        time.sleep(1)

        cert_client = 'src/client/cert.pem'
        client = Client(HOST, PORT, cert_client)
        data = "Hello World!"

        response = client.start(data)
        self.assertEquals(data, response)


if __name__ == "__main__":
    unittest.main()
