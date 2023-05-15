import xmlrpc.server


class AddFunction:
    def add_numbers(self, x, y):
        try:
            x = int(x)
            y = int(y)
            return x + y
        except:
            raise ValueError("Invalid Number")


class Server:
    def __init__(self, HOST, PORT) -> None:
        self.HOST = HOST
        self.PORT = PORT

    def start(self):
        with xmlrpc.server.SimpleXMLRPCServer((self.HOST, self.PORT)) as server:
            server.register_instance(AddFunction())

            # Start the server
            print("Start the server")
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                print("\nKeyboard interrupt received, exiting.")
                server.shutdown()
