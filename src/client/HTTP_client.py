"""Client which can get data from url and post data
"""
from urllib.request import urlopen, Request
import urllib.error as ERROR

import json
from http.client import InvalidURL


class HTTPClient:
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
            print("\nHTTP Error")
            print("Error code: ", error.code)
            raise error
        except ERROR.URLError as error:
            print("\nURL Error")
            print("Error reason: ", error.reason)
            raise error
        except InvalidURL as error:
            print("\nInvalid URL Error")
            raise error
        except ValueError as error:
            print("\nValue Error")
            raise error

    def post(self, url, data):
        """Post data to the URL and get the response.
        """
        if not isinstance(data, dict):
            raise TypeError
        data = json.dumps(data).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        try:
            request = Request(url, data=data, headers=headers, method="POST")
            return request
        except ERROR.HTTPError as error:
            print("\nHTTP Error")
            print("Error code: ", error.code)
            raise error
        except ERROR.URLError as error:
            print("\nURL Error")
            print("Error reason: ", error.reason)
            raise error
        except InvalidURL as error:
            print("\nInvalid URL Error")
            raise error
        except ValueError as error:
            print("\nValue Error")
            raise error

    def put(self, url, data):
        """Put data to the URL and get the response.
        """
        if not isinstance(data, dict):
            raise TypeError
        data = json.dumps(data).encode("utf-8")
        headers = {"Content-Type": "application/json"}
        try:
            request = Request(url, data=data, headers=headers, method="PUT")
            return request
        except ERROR.HTTPError as error:
            print("\nHTTP Error")
            print("Error code: ", error.code)
            raise error
        except ERROR.URLError as error:
            print("\nURL Error")
            print("Error reason: ", error.reason)
            raise error
        except InvalidURL as error:
            print("\nInvalid URL Error")
            raise error
        except ValueError as error:
            print("\nValue Error")
            raise error

    def delete(self, url):
        try:
            request = Request(url, method="DELETE")
            return request
        except ERROR.HTTPError as error:
            print("\nHTTP Error")
            print("Error code: ", error.code)
            raise error
        except ERROR.URLError as error:
            print("\nURL Error")
            print("Error reason: ", error.reason)
            raise error
        except InvalidURL as error:
            print("\nInvalid URL Error")
            raise error
        except ValueError as error:
            print("\nValue Error")
            raise error
