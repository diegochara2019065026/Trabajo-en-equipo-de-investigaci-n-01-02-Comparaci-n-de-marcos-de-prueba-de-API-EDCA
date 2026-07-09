import pytest

from conftest import BASE_URL, REQUEST_TIMEOUT


REQUIRED_POST_FIELDS = {"userId", "id", "title", "body"}


def assert_valid_post_schema(post):
    assert REQUIRED_POST_FIELDS.issubset(post.keys())
    assert isinstance(post["userId"], int)
    assert isinstance(post["id"], int)
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)
    assert post["title"]
    assert post["body"]


@pytest.mark.smoke
@pytest.mark.parametrize(
    ("post_id", "expected_user_id"),
    [
        (1, 1),
        (2, 1),
        (11, 2),
    ],
)
def test_get_post_by_id(api_client, post_id, expected_user_id):
    response = api_client.get(f"{BASE_URL}/posts/{post_id}", timeout=REQUEST_TIMEOUT)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id
    assert data["userId"] == expected_user_id
    assert_valid_post_schema(data)


@pytest.mark.smoke
def test_get_posts_list(api_client):
    response = api_client.get(f"{BASE_URL}/posts", timeout=REQUEST_TIMEOUT)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert_valid_post_schema(data[0])


def test_create_post(api_client, post_payload):
    response = api_client.post(
        f"{BASE_URL}/posts",
        json=post_payload,
        timeout=REQUEST_TIMEOUT,
    )

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == post_payload["title"]
    assert data["body"] == post_payload["body"]
    assert data["userId"] == post_payload["userId"]
    assert "id" in data


@pytest.mark.negative
def test_get_missing_post_returns_404(api_client):
    response = api_client.get(f"{BASE_URL}/posts/999999", timeout=REQUEST_TIMEOUT)

    assert response.status_code == 404
