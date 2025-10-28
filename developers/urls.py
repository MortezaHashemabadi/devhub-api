from rest_framework.routers import DefaultRouter
from .views import DeveloperProfileViewSet, ProjectViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'profiles', DeveloperProfileViewSet)
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls
