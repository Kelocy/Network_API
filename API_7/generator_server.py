from src.server.server import Server

HOST, PORT = "localhost", 9999
cert, key = 'src/server/server_cert.pem', 'src/server/server_key.pem'
server = Server(HOST, PORT, cert, key)
server.start()
