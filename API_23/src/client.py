import socket


class Client:
    def __init__(self, HOST, PORT):
        self.HOST = HOST
        self.PORT = PORT

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            """Send message to server by sock.
            Input "quit" to stop client.

            Args:
                socket.AF_INET: Specify IPv4 address family, 
                which is Internet Address Family.
                socket.SOCK_STREAM: Specify the socket type as TCP.
            """
            sock.connect((self.HOST, self.PORT))
            while True:
                data = input("Input data: ")
                if data == "quit":
                    break
                sock.sendall(data.encode())
                # recv(1024) specifies the maximum amount of data in each call.
                response = sock.recv(1024).decode()
                print("Server response: ", response)
