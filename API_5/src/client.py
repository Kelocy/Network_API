import urllib
import json


class Client:
    def __init__(self, host, port):
        self.url = "http://{}:{}".format(host, port)

    def call_remote_function(self, module_name, function_name, *args):
        data = {
            "module": module_name,
            "function": function_name,
            "args": json.dumps(args),
        }
        data_rqs = urllib.parse.urlencode(data).encode("ascii")
        rps = urllib.request.urlopen(self.url, data)
        return rps.read().decode()
