from src.client.client import Client

HOST, PORT = "localhost", 9999
cert = 'src/client/server_cert.pem'
client = Client(HOST, PORT, cert)
client.start("Hello")
