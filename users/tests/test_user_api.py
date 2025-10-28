import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

@pytest.mark.django_db
def test_auth_flow():
    user = User.objects.create_user(email="a@a.com", password="1234")
    client = APIClient()
    res = client.post("/api/token/", {"email": "a@a.com", "password": "1234"})
    assert res.status_code == 200
    assert "access" in res.data
