import unittest
import threading
from src.server import Server
from src.client import Client
import time


class ServiceTest(unittest.TestCase):
    def test_run(self):
        HOST, PORT = 'localhost', 8000
        server = Server(HOST, PORT)
        server_thread = threading.Thread(target=server.start)
        server_thread.start()

        time.sleep(1)

        client = Client(HOST, PORT)
        response = client.start(13, 45)
        self.assertEquals(58, response)
        server.close()


if __name__ == "__main__":
    unittest.main()
