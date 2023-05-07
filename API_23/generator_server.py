from src.server import ServerTCP, ServerUDP

HOST, PORT = "localhost", 9999
MODEL = "TCP"   # "UDP"
if MODEL == "TCP":
    server = ServerTCP(HOST, PORT)
    server.start()
elif MODEL == "UDP":
    server = ServerUDP(HOST, PORT)
    server.start()
else:
    print("Invalid Model")
