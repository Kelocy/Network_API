from src.server import Server

HOST, PORT = 'localhost', 8000
server = Server(HOST, PORT)
server.start()
