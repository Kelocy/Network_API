import unittest
import threading
import time
from src.server.TCP_server import MyTCPServer
from src.client.TCP_client import MyTCPClient


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


if __name__ == "__main__":
    unittest.main()
