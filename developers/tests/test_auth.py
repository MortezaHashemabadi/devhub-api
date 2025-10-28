import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(password="1234", email="ali@test.com")
    assert user.email == "ali@test.com"
