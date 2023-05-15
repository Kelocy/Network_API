from socketserver import TCPServer, UDPServer, BaseRequestHandler, ThreadingMixIn
import time
import socket


class MyTCPHandler(BaseRequestHandler):
    # Docs: https://docs.python.org/3/library/socketserver.html

    def handle(self):
        # The handle() method receives and decodes the message
        # from client and send back successful massage of receving data encoded.

        print("Client is connected!")
        # last_activity = time.time()
        # while True:
        # recv(1024) specifies the maximum amount of data in each call.
        data = self.request.recv(1024).decode()
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        self.request.sendall(data.encode())
        # last_activity = time.time()

        # if time.time() - last_activity > 10:
        #     print("Client inactive for 30 seconds. Closing connection")
        #     self.request.shutdown(socket.SHUT_RDWR)
        #     self.request.close()
        #     break


class MyUDPHandler(BaseRequestHandler):
    def handle(self):
        print("Client is connected!")
        data = self.request[0].decode()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.encode(), self.client_address)


class ThreadedTCPServer(ThreadingMixIn, TCPServer):
    pass


class ThreadedUDPServer(ThreadingMixIn, UDPServer):
    pass


class ServerTCP:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def start(self):
        print("Server is listening...")
        with TCPServer((self.HOST, self.PORT), MyTCPHandler) as server:
            server.serve_forever()

    def start_once(self):
        print("Server is listening...")
        server = ThreadedTCPServer((self.HOST, self.PORT), MyTCPHandler)
        return server


class ServerUDP:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def start(self):
        print("Server is listening...")
        with UDPServer((self.HOST, self.PORT), MyUDPHandler) as server:
            server.serve_forever()

    def start_once(self):
        print("Server is listening...")
        server = ThreadedUDPServer((self.HOST, self.PORT), MyUDPHandler)
        return server
