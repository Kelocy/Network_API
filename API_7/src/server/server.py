"""Server side by using ssl to receive and send message 
"""
import socket
import ssl


class Server:
    """Create server and start listening
    """
    def __init__(self, host, port, cert, key):
        self.host = host
        self.port = port
        self.cert = cert
        self.key = key

    def start(self):
        """Create sock service to listen to the port by uisng ssl certification 
        """
        print("Server is listening...")
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=self.cert, keyfile=self.key)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.host, self.port))
            sock.listen(5)
            with context.wrap_socket(sock, server_side=True) as ssock:
                try:
                    while True:
                        conn, _ = ssock.accept()
                        try:
                            data = conn.recv(1024)
                            if not data:
                                break
                            print("Receive data: ", data.decode())
                            conn.sendall(data)
                        except ssl.SSLError as SSLError:
                            raise ConnectionError(
                                "SSL Connection Error") from SSLError
                except KeyboardInterrupt:
                    print("KeyboardInterrupt error occurred")
