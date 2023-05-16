import unittest
import threading
import time
from src.server.ssl_server import SslServer
from src.client.ssl_client import SslClient
import os


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


if __name__ == "__main__":
    unittest.main()
