"""Test client function
"""
import unittest
from src.client.HTTP_client import HTTPClient
from urllib.error import URLError, HTTPError
from http.client import InvalidURL


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

    def test_get_url_error(self):
        url = "http://fakeurl"
        with self.assertRaises(URLError):
            response = self.client.get(url)

    def test_get_http_error(self):
        url = "https://jsonplaceholder.typicode.com/dehuguad"
        with self.assertRaises(HTTPError):
            response = self.client.get(url)

    def test_get_invalid_url_error(self):
        url = "http://fake url"
        with self.assertRaises(InvalidURL):
            response = self.client.get(url)

    def test_get_not_url_error(self):
        url = "dg737cr4y37nxr8m2"
        with self.assertRaises(ValueError):
            response = self.client.get(url)

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

    def test_post_type_error(self):
        """Post function will send data to url and receive the response
        """
        data_post = [12, 43, 54]
        url = "https://jsonplaceholder.typicode.com/posts"
        with self.assertRaises(TypeError):
            return_response = self.client.post(url, data_post)

    def test_post_url_error(self):
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        url = "https://dummyurl"
        with self.assertRaises(URLError):
            return_response = self.client.post(url, data_post)
            return_data = self.client.get(return_response)

    def test_post_http_error(self):
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        url = "https://jsonplaceholder.typicode.com/hfdedewff"
        with self.assertRaises(HTTPError):
            return_response = self.client.post(url, data_post)
            return_data = self.client.get(return_response)

    def test_post_invalid_url_error(self):
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        url = "http://fake url"
        with self.assertRaises(InvalidURL):
            return_response = self.client.post(url, data_post)
            return_data = self.client.get(return_response)

    def test_post_not_url_error(self):
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        url = "dg737cr4y37nxr8m2"
        with self.assertRaises(ValueError):
            return_response = self.client.post(url, data_post)
            return_data = self.client.get(return_response)

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

    def test_put_type_error(self):
        data_post = 32
        url = "https://jsonplaceholder.typicode.com/posts/1"
        with self.assertRaises(TypeError):
            return_response = self.client.put(url, data_post)

    def test_put_url_error(self):
        data_post = {
            "id": 1,
            "name": "JOJO",
            "email": "jojo@example.com",
            "message": "My best day!"
        }
        url = "https://dummyurl"
        with self.assertRaises(URLError):
            return_response = self.client.put(url, data_post)
            return_data = self.client.get(return_response)

    def test_put_http_error(self):
        data_post = {
            "id": 1,
            "name": "JOJO",
            "email": "jojo@example.com",
            "message": "My best day!"
        }
        url = "https://jsonplaceholder.typicode.com/hfdeadasqf"
        with self.assertRaises(HTTPError):
            return_response = self.client.put(url, data_post)
            return_data = self.client.get(return_response)

    def test_invalid_url_error(self):
        data_post = {
            "id": 1,
            "name": "JOJO",
            "email": "jojo@example.com",
            "message": "My best day!"
        }
        url = "http://fadefg  url"
        with self.assertRaises(InvalidURL):
            return_response = self.client.put(url, data_post)
            return_data = self.client.get(return_response)

    def test_not_url_error(self):
        data_post = {
            "id": 1,
            "name": "JOJO",
            "email": "jojo@example.com",
            "message": "My best day!"
        }
        url = "dfeffdsdewfe2"
        with self.assertRaises(ValueError):
            return_response = self.client.put(url, data_post)
            return_data = self.client.get(return_response)

    def test_delete(self):
        url = "https://jsonplaceholder.typicode.com/posts/1"
        return_response = self.client.delete(url)
        return_data = self.client.get(return_response)
        # print(return_data)
        self.assertEqual(return_data, {})

    def test_delete_url_error(self):
        url = "http://fakdeffeurl"
        with self.assertRaises(URLError):
            return_response = self.client.delete(url)
            return_data = self.client.get(return_response)

    def test_delete_http_error(self):
        url = "https://jsonplaceholder.typicode.com/hffefasqf"
        with self.assertRaises(HTTPError):
            return_response = self.client.delete(url)
            return_data = self.client.get(return_response)

    def test_delete_invalid_url_error(self):
        url = "http://fadddefg  urdefffl"
        with self.assertRaises(InvalidURL):
            return_response = self.client.delete(url)
            return_data = self.client.get(return_response)

    def test_delete_not_url_error(self):

        url = "dfeffdfsdf2214fvvf"
        with self.assertRaises(ValueError):
            return_response = self.client.delete(url)
            return_data = self.client.get(return_response)


if __name__ == "__main__":
    unittest.main()
