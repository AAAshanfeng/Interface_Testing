import requests

base_url = "https://dummyjson.com/products"


def test_get_product():
    """查询：获取单个商品"""
    response = requests.get(f"{base_url}/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_add_product():
    """新增：添加一个商品"""
    response = requests.post(f"{base_url}/add", json={"title": "我的测试商品"})
    assert response.status_code == 201
    assert response.json()["title"] == "我的测试商品"


def test_update_product():
    """更新：修改商品信息"""
    response = requests.put(f"{base_url}/1", json={"title": "修改后的标题"})
    assert response.status_code == 200
    assert response.json()["title"] == "修改后的标题"


def test_delete_product():
    """删除：删除一个商品"""
    response = requests.delete(f"{base_url}/1")
    assert response.status_code == 200
    assert response.json()["isDeleted"] == True