from socketserver import TCPServer, UDPServer, BaseRequestHandler
import time
import socket


class BaseHandler(BaseRequestHandler):
    # Docs: https://docs.python.org/3/library/socketserver.html

    def handle(self):
        # The handle() method receives and decodes the message
        # from client and send back successful massage of receving data encoded.

        print("Client is connected!")
        last_activity = time.time()
        while True:
            # recv(1024) specifies the maximum amount of data in each call.
            data = self.request.recv(1024).decode()
            print(data)
            self.request.sendall(f"[Received: {data}]".encode())
            last_activity = time.time()

            if time.time() - last_activity > 10:
                print("Client inactive for 30 seconds. Closing connection")
                self.request.shutdown(socket.SHUT_RDWR)
                self.request.close()
                break


class ServerTCP:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def start(self):
        print("Server is listening...")
        with TCPServer((self.HOST, self.PORT), BaseHandler) as server:
            server.serve_forever()

class ServerUDP:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def start(self):
        print("Server is listening...")
        with UDPServer((self.HOST, self.PORT), BaseHandler) as server:
            server.serve_forever()

