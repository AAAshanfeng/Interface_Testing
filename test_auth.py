import requests

login_url = "https://dummyjson.com/auth/login"
me_url = "https://dummyjson.com/auth/me"

def get_token():
    response = requests.post(login_url, json={"username": "emilys","password": "emilyspass"})
    return response.json()["accessToken"]


def test_auth_with_valid_token():
    """携带正确token访问，应该成功"""
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(me_url, headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == "emilys"


def test_auth_with_invalid_token():
    """携带错误token访问，应该被拒绝"""
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.get(me_url, headers=headers)
    assert response.status_code == 401


def test_auth_without_token():
    """不携带token访问，应该被拒绝"""
    response = requests.get(me_url)
    assert response.status_code == 401