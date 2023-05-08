from urllib.request import urlopen, Request
import urllib.error as ERROR
import json


class Client:
    """Get data from the url, post data to the url and get response.
    """
    def __init__(self, url) -> None:
        self.url = url

    def get(self):
        """Download data from the url, print on the command
        line and save as a file.
        """
        try:
            with urlopen(self.url) as response:
                data = response.read().decode("utf-8")
                data_json = json.loads(data)
                with open('message_json.txt', mode='wt', encoding='utf-8') as f:
                    f.write(json.dumps(data_json))
                return data_json
        except ERROR.HTTPError as e:
            print("HTTP Error: The URL is not the HTTP")
        except ERROR.URLError as e:
            print("URL Error: Cannot connect to the server")

    def post(self, data):
        """Post data to the URL and get the response.
        """
        data = json.dumps(data).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        request = Request(self.url, data=data, headers=headers)
        
        try:
            with urlopen(request) as response:
                result = response.read().decode("utf-8")
                result_json = json.loads(result)
                with open('result_json.txt', mode='wt', encoding='utf-8') as f:
                    f.write(json.dumps(result_json))
                return result_json
        except ERROR.HTTPError as e:
            print("HTTP Error: The URL is not the HTTP")
        except ERROR.URLError as e:
            print("URL Error: Cannot connect to the server")

