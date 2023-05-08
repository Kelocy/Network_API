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
        data_post = {
            "name": "Alex",
            "email": "alex@example.com",
            "message": "Hello, world!"
        }
        return_data = self.client.post(data_post)
        self.assertEqual(data_post, return_data.update({"id": 101}))
        # print(return_data)


if __name__ == "__main__":
    unittest.main()