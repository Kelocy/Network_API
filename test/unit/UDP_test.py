import unittest
import threading
import time
from src.server.UDP_server import MyUDPServer
from src.client.UDP_client import MyUDPClient


# API_3
class UDPTest(unittest.TestCase):
    def test_udp(self):
        HOST, PORT = "localhost", 9910
        server = MyUDPServer(HOST, PORT)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()

        time.sleep(1)

        client = MyUDPClient(HOST, PORT)
        data = "Hello World!"
        return_data = client.start_udp(data)
        self.assertEqual(data, return_data)
        server.close()


if __name__ == "__main__":
    unittest.main()
