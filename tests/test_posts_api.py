import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1", timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)
    assert data["title"]
    assert data["body"]


def test_get_posts_list():
    response = requests.get(f"{BASE_URL}/posts", timeout=10)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert {"userId", "id", "title", "body"}.issubset(data[0].keys())


def test_create_post():
    payload = {
        "title": "API Testing with Pytest",
        "body": "This is a practical API testing example.",
        "userId": 1,
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


def test_get_missing_post_returns_404():
    response = requests.get(f"{BASE_URL}/posts/999999", timeout=10)

    assert response.status_code == 404
