import requests

# 发起GET请求


def get_request(url):
    response = requests.get(url)
    return response.json()

# 发起POST请求


def post_request(url, data):
    response = requests.post(url, json=data)
    return response.json()

# 发起PUT请求


def put_request(url, data):
    response = requests.put(url, json=data)
    return response.json()

# 发起DELETE请求


def delete_request(url):
    response = requests.delete(url)
    return response.json()


# 示例使用
base_url = 'https://api.example.com/users'

# 发起GET请求获取用户列表
users = get_request(base_url)
print(users)

# 发起POST请求创建新用户
new_user = {'name': 'John', 'email': 'john@example.com'}
created_user = post_request(base_url, new_user)
print(created_user)

# 发起PUT请求更新用户信息
user_id = 123
updated_user = {'name': 'John Doe', 'email': 'johndoe@example.com'}
updated_user = put_request(f'{base_url}/{user_id}', updated_user)
print(updated_user)

# 发起DELETE请求删除用户
user_id = 123
response = delete_request(f'{base_url}/{user_id}')
print(response)
