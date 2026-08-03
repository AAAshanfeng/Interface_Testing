import requests

login_url = "https://dummyjson.com/auth/login"
login_data = {
    "username": "emilys",
    "password": "emilyspass"
}

login_response = requests.post(login_url, json=login_data)
token = login_response.json()["accessToken"]

me_url = "https://dummyjson.com/auth/me"
headers = {
    "Authorization": f"Bearer {token}"
}

me_response = requests.get(me_url, headers=headers)

print(me_response.status_code)
print(me_response.json())

assert me_response.status_code == 200, "状态码不是200"
assert me_response.json()["username"] == "emilys", "用户名不对"
print("全部断言通过")