from src.client import Client

HOST, PORT = "localhost", 9999
client = Client(HOST, PORT)
client.start()
