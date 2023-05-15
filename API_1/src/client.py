"""Client which can get data from url and post data
"""
from urllib.request import urlopen, Request
import urllib.error as ERROR
import json


class Client:
    """Get data from the url, post data to the url and get response.
    """

    def get(self, url):
        """Download data from the url, print on the command
        line and save as a file.
        """
        try:
            with urlopen(url) as response:
                data = response.read().decode("utf-8")
                data_json = json.loads(data)
                with open('message_json.txt', mode='wt', encoding='utf-8') as file:
                    file.write(json.dumps(data_json))
                return data_json
        except ERROR.HTTPError as error:
            print("HTTP Error: The URL is not HTTP")
            print("Error code: ", error.code)
            return None
        except ERROR.URLError as error:
            print("URL Error: Cannot connect to the server")
            print("Error code: ", error)
            return None

    def post(self, url, data):
        """Post data to the URL and get the response.
        """
        data = json.dumps(data).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        request = Request(url, data=data, headers=headers, method="POST")
        return request

    def put(self, url, data):
        """Put data to the URL and get the response.
        """
        data = json.dumps(data).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        request = Request(url, data=data, headers=headers, method="PUT")
        return request

    def delete(self, url):
        request = Request(url, method="DELETE")
        return request
