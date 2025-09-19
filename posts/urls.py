from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagViewSet

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')   # /api/v1/posts/
router.register(r'tags', TagViewSet, basename='tag') # /api/v1/posts/tags/

urlpatterns = [
    path('', include(router.urls)),
]
