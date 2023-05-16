import unittest
import threading
import time
from src.server.xmlrpc_server import XmlrpcServer
from src.client.xmlrpc_client import XmlrpcClient


class XmlrpcTest(unittest.TestCase):
    def test_run(self):
        HOST, PORT = 'localhost', 9920
        server = XmlrpcServer(HOST, PORT)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()

        time.sleep(1)

        client = XmlrpcClient(HOST, PORT)
        response = client.start(13, 45)
        self.assertEquals(58, response)
        server.close()


if __name__ == "__main__":
    unittest.main()
