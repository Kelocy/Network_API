import socket


class MyUDPClient:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def start_udp(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.sendto(data.encode(), (self.HOST, self.PORT))
            response = str(sock.recv(1024).decode())
            print("Received: ", response)
            # print("Server response: ", response)
            return response
