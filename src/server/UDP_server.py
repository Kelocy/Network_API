from socketserver import TCPServer, UDPServer, BaseRequestHandler, ThreadingMixIn
import time
import socket


class MyUDPHandler(BaseRequestHandler):
    def handle(self):
        print("Client is connected!")
        data = self.request[0].decode()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.encode(), self.client_address)


class MyUDPServer:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def start(self):
        print("Server is listening...")
        with UDPServer((self.HOST, self.PORT), MyUDPHandler) as server:
            self.server = server
            server.serve_forever()

    def close(self):
        self.server.shutdown()
