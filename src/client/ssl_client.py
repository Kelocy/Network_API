"""Client side by using ssl to send message and get the response
"""
import socket
import ssl


class SslClient:
    """Create client side and start sending message
    """

    def __init__(self, host, port, cert):
        self.host = host
        self.port = port
        self.cert = cert

    def start(self, msg):
        """Use ssl while connecting, get response and print message
        """
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations(self.cert)

        with socket.create_connection((self.host, self.port)) as sock:
            with context.wrap_socket(sock, server_hostname=self.host) as ssock:
                ssock.sendall(msg.encode())
                data = ssock.recv(1024)
                print("Receive data from server: ", data.decode())

        return data.decode()
