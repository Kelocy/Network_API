from src.client import Client

HOST, PORT = 'localhost', 8000
client = Client(HOST, PORT)
client.start()
