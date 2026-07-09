import pytest
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"
REQUEST_TIMEOUT = 10


@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()


@pytest.fixture
def post_payload():
    return {
        "title": "API Testing with Pytest",
        "body": "This is a practical API testing example.",
        "userId": 1,
    }
