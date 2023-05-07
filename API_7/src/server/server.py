import socket
import ssl

# context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# context.load_cert_chain(certfile='server_cert.pem', keyfile='server_key.pem')


class Server:
    def __init__(self, HOST, PORT, cert, key):
        self.HOST = HOST
        self.PORT = PORT
        self.cert = cert
        self.key = key

    def start(self):
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(certfile=self.cert, keyfile=self.key)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind((self.HOST, self.PORT))
            sock.listen(5)
            with context.wrap_socket(sock, server_side=True) as ssock:
                while True:
                    conn, addr = ssock.accept()
                    with conn:
                        data = conn.recv(1024)
                        if not data:
                            break
                        conn.sendall(data)
