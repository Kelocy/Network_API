from src.client.client import Client

HOST, PORT = "localhost", 9999
cert = 'src/client/cert.pem'
client = Client(HOST, PORT, cert)
while True:
    message = input("Please input your message: ")
    client.start(message)
