import cgi
import json


class RESTAPI():
    def __init__(self):
        pass

    def start(self):
        self.server = cgi.FieldStorage()
        if "module" in self.server and "function" in self.server:
            module_name = self.server.getvalue("module")
            function_name = self.server.getvalue("function")
            if "args" in self.server:
                args = json.loads(self.server.getvalue("args"))
            else:
                args = []
            module = __import__(module_name)
            function = getattr(module, function_name)
            try:
                rsp = function(*args)
                print("Call result:")
                print(rsp)
            except:
                print("Call back fail")
                print("Insufficient or invalid args")
        else:
            print("Call back fail")
            print("Invalid request")
