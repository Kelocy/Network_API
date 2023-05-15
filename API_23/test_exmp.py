import threading
from src.server import ServerTCP, ServerUDP
from src.client import Client
import time


def main1():
    HOST, PORT = "localhost", 9990
    server = ServerTCP(HOST, PORT)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # 等待一段时间，确保服务器已经启动
    time.sleep(1)

    # 运行客户端
    client = Client(HOST, PORT)
    data = "Hello World!"
    client.start_tcp(data)


def test_tcp():
    HOST, PORT = "localhost", 9999
    server = ServerTCP(HOST, PORT)
    server_once = server.start_once()
    server_thread = threading.Thread(target=server_once.serve_forever)
    server_thread.start()

    time.sleep(1)

    client = Client(HOST, PORT)
    data = "Hello World!"
    response = client.start_tcp(data)
    print(response)

    server_once.shutdown()


def main2():
    HOST, PORT = "localhost", 9800
    server = ServerUDP(HOST, PORT)
    server_thread = threading.Thread(target=server.start)
    server_thread.start()

    # 等待一段时间，确保服务器已经启动
    time.sleep(1)

    # 运行客户端
    client = Client(HOST, PORT)
    data = "Hello World!"
    client.start_udp(data)


def test_udp():
    HOST, PORT = "localhost", 9989
    server = ServerUDP(HOST, PORT)
    server_once = server.start_once()
    server_thread = threading.Thread(target=server_once.serve_forever)
    server_thread.start()

    time.sleep(1)

    client = Client(HOST, PORT)
    data = "Hello World!"
    response = client.start_udp(data)

    server_once.shutdown()


if __name__ == "__main__":
    # main()
    test_udp()
