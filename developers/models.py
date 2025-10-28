from django.conf import settings
from django.db import models

class DeveloperProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.user.email

class Project(models.Model):
    owner = models.ForeignKey(DeveloperProfile, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    demo_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=255, blank=True)  # مثلا "Django, React, Redis"
    created_at = models.DateTimeField(auto_now_add=True)

    stars = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='starred_projects', blank=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.owner.user.email})"

    @property
    def stars_count(self):
        return self.stars.count()

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.email} on {self.project.title}"
