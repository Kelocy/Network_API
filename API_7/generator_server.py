from src.server.server import Server

HOST, PORT = "localhost", 9999
cert, key = 'src/server/cert.pem', 'src/server/key.pem'
server = Server(HOST, PORT, cert, key)
server.start()
