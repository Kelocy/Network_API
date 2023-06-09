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


class MyTCPServer:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def start(self):
        print("Server is listening...")
        with TCPServer((self.HOST, self.PORT), MyTCPHandler) as server:
            self.server = server
            server.serve_forever()

    def close(self):
        self.server.shutdown()
