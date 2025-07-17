import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", email="user@example.com", password="secure123")


@pytest.fixture
def auth_client(client, user):
    client.force_authenticate(user=user)
    return client


def test_me_requires_authentication(client):
    response = client.get("/api/auth/me/")
    assert response.status_code == 401


def test_me_returns_current_user(auth_client, user):
    response = auth_client.get("/api/auth/me/")
    assert response.status_code == 200
    assert response.data["username"] == user.username
    assert response.data["email"] == user.email
