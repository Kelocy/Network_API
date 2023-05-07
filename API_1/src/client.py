from urllib.request import urlopen, Request
import urllib.error as ERROR
import json


class Client:
    def __init__(self, url) -> None:
        self.url = url

    def get(self):
        try:
            with urlopen(self.url) as response:
                data = response.read().decode("utf-8")
                data_json = json.loads(data)
                return data_json
        except ERROR.HTTPError as e:
            print("HTTP Error: The URL is not the HTTP")
        except ERROR.URLError as e:
            print("URL Error: Cannot connect to the server")

    def post(self, data):
        data = json.dumps(data).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        request = Request(self.url, data=data, headers=headers)
        
        try:
            with urlopen(request) as response:
                result = response.read().decode("utf-8")
                result_json = json.loads(result)
                return result_json
        except ERROR.HTTPError as e:
            print("HTTP Error: The URL is not the HTTP")
        except ERROR.URLError as e:
            print("URL Error: Cannot connect to the server")

