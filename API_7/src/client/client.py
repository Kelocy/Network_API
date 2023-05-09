import socket
import ssl


class Client:
    def __init__(self, HOST, PORT, cert):
        self.HOST = HOST
        self.PORT = PORT
        self.cert = cert

    def start(self, msg):
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations(self.cert)

        with socket.create_connection((self.HOST, self.PORT)) as sock:
            with context.wrap_socket(sock, server_hostname=self.HOST) as ssock:
                ssock.sendall(msg.encode())
                data = ssock.recv(1024)
                print("Receive data from server: ", data.decode())

        return data.decode()
