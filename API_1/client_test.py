"""Test client function
"""
import unittest
from src.client import Client

class ClientTest(unittest.TestCase):
    """Two test functions test the client class
    """

    def setUp(self):
        """Setup a client with url
        """
        url = "https://jsonplaceholder.typicode.com/posts"
        self.client = Client(url)

    def test_function_get(self):
        """Get function will pull data from the url
        """
        data = self.client.get()
        print(data)


    def test_function_post(self):
        """Post function will send data to url and receive the response
        """
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        return_data = self.client.post(data_post)
        data_post.update({"id": 101})
        self.assertEqual(return_data, data_post)
        print(data_post)


if __name__ == "__main__":
    unittest.main()
