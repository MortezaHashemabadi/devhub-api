from .models import DeveloperProfile, Project, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'project', 'user_email', 'content', 'created_at']
        read_only_fields = ['user_email', 'created_at']


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    stars_count = serializers.IntegerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

class DeveloperProfileSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    def perform_create(self, serializer):
        profile, _ = DeveloperProfile.objects.get_or_create(user=self.request.user)
        serializer.save(owner=profile)

    class Meta:
        model = DeveloperProfile
        fields = '__all__'
