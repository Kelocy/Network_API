"""Test client function
"""
import unittest
from src.client.HTTP_client import HTTPClient


class ServiceTest(unittest.TestCase):
    """Two test functions test the client class
    """

    def setUp(self):
        """Setup a client with url
        """
        self.client = HTTPClient()

    def test_get(self):
        """Get function will pull data from the url
        """
        url = "https://jsonplaceholder.typicode.com/posts"
        return_data = self.client.get(url)
        self.assertIsNotNone(return_data)
        # print(return_data)

    def test_post(self):
        """Post function will send data to url and receive the response
        """
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        data_expect_response = {
            "id": 101,
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!",
        }
        url = "https://jsonplaceholder.typicode.com/posts"
        return_response = self.client.post(url, data_post)
        return_data = self.client.get(return_response)
        self.assertEqual(return_data, data_expect_response)
        # print(return_data)

    def test_put(self):
        """Post function will send data to url and receive the response
        """
        data_post = {
            "id": 1,
            "name": "JOJO",
            "email": "jojo@example.com",
            "message": "My best day!"
        }
        url = "https://jsonplaceholder.typicode.com/posts/1"
        return_response = self.client.put(url, data_post)
        return_data = self.client.get(return_response)
        self.assertEqual(return_data, data_post)
        # print(return_data)

    def test_delete(self):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        return_response = self.client.delete(url)
        return_data = self.client.get(return_response)
        # print(return_data)
        self.assertEqual(return_data, {})


if __name__ == "__main__":
    unittest.main()
