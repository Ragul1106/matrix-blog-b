# posts/views.py
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Tag
from .serializers import PostListSerializer, PostDetailSerializer, PostCreateUpdateSerializer, TagSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('tags').all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author__id','tags__slug','status']
    search_fields = ['title','content']
    ordering_fields = ['published_at','created_at']

    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        if self.action in ['list']:
            return PostListSerializer
        if self.action in ['retrieve']:
            return PostDetailSerializer
        return PostCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['get'], url_path='comments')
    def get_comments(self, request, slug=None):
        from comments.models import Comment
        comments = Comment.objects.filter(post__slug=slug, is_approved=True)
        from comments.serializers import CommentSerializer
        return Response(CommentSerializer(comments, many=True).data)

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
