from django.utils import timezone
from datetime import timedelta
from .models import DeveloperProfile, Project, Comment
from .serializers import DeveloperProfileSerializer, ProjectSerializer, CommentSerializer
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
class DeveloperProfileViewSet(viewsets.ModelViewSet):
    queryset = DeveloperProfile.objects.all()
    serializer_class = DeveloperProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tech_stack', 'owner']
    search_fields = ['title', 'description', 'tech_stack']
    ordering_fields = ['created_at', 'title']

    def perform_create(self, serializer):
        profile, _ = DeveloperProfile.objects.get_or_create(user=self.request.user)
        serializer.save(owner=profile)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def toggle_star(self, request, pk=None):
        project = self.get_object()
        user = request.user
        if user in project.stars.all():
            project.stars.remove(user)
            return Response({'status': 'unstarred'}, status=status.HTTP_200_OK)
        else:
            project.stars.add(user)
            return Response({'status': 'starred'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[permissions.AllowAny])
    def add_view(self, request, pk=None):
        project = self.get_object()
        project.views += 1
        project.save()
        return Response({'views': project.views}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def trending(self, request):
        one_week_ago = timezone.now() - timedelta(days=7)
        projects = Project.objects.filter(created_at__gte=one_week_ago)
        # امتیاز ساده: stars + views / 10
        sorted_projects = sorted(
            projects,
            key=lambda p: p.stars.count() + (p.views / 10),
            reverse=True
        )

        serializer = self.get_serializer(sorted_projects, many=True)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)