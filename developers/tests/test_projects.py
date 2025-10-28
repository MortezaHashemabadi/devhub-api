import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from developers.models import Project, DeveloperProfile
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestProjectsAPI:
    @pytest.fixture
    def client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        user = User.objects.create_user(password="12345", email="test@test.com")
        DeveloperProfile.objects.get_or_create(user=user)
        return user

    def test_project_creation(self, client, user):
        client.force_authenticate(user=user)
        response = client.post("/api/projects/", {
            "title": "Test Project",
            "description": "A cool Django API test",
            "tech_stack": "Django, DRF"
        }, format='json')
        assert response.status_code == 201
        assert response.data['title'] == "Test Project"

    def test_trending_endpoint(self, client, user):
        Project.objects.create(owner=user.developerprofile, title="Popular Project", tech_stack="Django")
        response = client.get("/api/projects/trending/")
        assert response.status_code == 200
