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
        self.client = Client()

    def test_function_get(self):
        """Get function will pull data from the url
        """
        url = "https://jsonplaceholder.typicode.com/posts"
        return_data = self.client.get(url)
        self.assertIsNotNone(return_data)
        print(return_data)

    def test_function_post(self):
        """Post function will send data to url and receive the response
        """
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        url = "https://jsonplaceholder.typicode.com/posts"
        return_response = self.client.post(url, data_post)
        return_data = self.client.get(return_response)
        data_post.update({"id": 101})
        self.assertEqual(return_data, data_post)
        print(return_data)


if __name__ == "__main__":
    unittest.main()
