from src.client import Client

url = "https://jsonplaceholder.typicode.com/posts"
client = Client(url)
data = client.get()
print(data)

data_post = {
    "name": "Alex",
    "email": "alex@example.com",
    "message": "Hello, world!"
}
return_data = client.post(data_post)
print(data_post)
