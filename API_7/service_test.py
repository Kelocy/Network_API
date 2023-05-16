"""Test client function
"""
import unittest
import threading
from src.server.server import Server
from src.client.client import Client
import time
import os


class ServiceTest(unittest.TestCase):
    def test_run(self):
        HOST, PORT = "localhost", 9999
        cert_server = os.path.join(
            os.path.dirname(__file__), 'src/server/cert.pem')
        key_server = os.path.join(
            os.path.dirname(__file__), 'src/server/key.pem')
        server = Server(HOST, PORT, cert_server, key_server)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()

        time.sleep(1)

        cert_client = os.path.join(
            os.path.dirname(__file__), 'src/client/cert.pem')
        client = Client(HOST, PORT, cert_client)
        data = "Hello World!"

        response = client.start(data)
        self.assertEquals(data, response)


if __name__ == "__main__":
    unittest.main()
