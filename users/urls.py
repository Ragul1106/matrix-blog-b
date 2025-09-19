from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),                   # /api/v1/users/
    path('register/', RegisterView.as_view(), name='register'),        # /api/v1/register/
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # /api/v1/token/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # /api/v1/token/refresh/
]
