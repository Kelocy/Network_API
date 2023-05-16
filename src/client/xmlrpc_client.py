import xmlrpc.client


class XmlrpcClient:
    def __init__(self, HOST, PORT) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.url = "http://{}:{}".format(self.HOST, self.PORT)

    def start(self, x, y):
        with xmlrpc.client.ServerProxy(self.url) as proxy:
            while True:
                try:
                    # x, y = input(
                    #     "Enter two numbers separated by space: ").split()
                    result = proxy.add_numbers(x, y)
                    print(result)
                    return result
                except:
                    raise ValueError("Invalid Numbers")
