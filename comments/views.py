# comments/views.py
from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from posts.permissions import IsOwnerOrReadOnly

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('author','post').all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # override update/destroy permissions: allow admins to moderate (approve) any comment
    def get_permissions(self):
        if self.action in ['partial_update','approve']:
            return [IsAdminUser()]
        return super().get_permissions()
