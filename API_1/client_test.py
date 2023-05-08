import unittest
from src.client import Client

class ClientTest(unittest.TestCase):
    def setUp(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        self.client = Client(url)

    def test_function_get(self):
        data = self.client.get()
        # print(data)

    def test_function_post(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        client = Client(url)
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        return_data = client.post(data_post)
        data_post.update({"id": 101})
        self.assertEqual(return_data, data_post)
        


if __name__ == "__main__":
    unittest.main()