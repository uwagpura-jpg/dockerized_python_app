
from dockerized_app import app


def test_homepage_returns_success():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_homepage_returns_expected_message():
    client = app.test_client()

    response = client.get("/")

    assert response.data == b"Hello from Dockerized Python App!"
