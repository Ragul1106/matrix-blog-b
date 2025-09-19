# posts/serializers.py
from rest_framework import serializers
from .models import Post, Tag
from django.conf import settings

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name','slug']

class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id','title','slug','author','featured_image','status','published_at','created_at','tags']

class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id','title','slug','content','author','featured_image','status','published_at','created_at','updated_at','tags']

    def get_author(self, obj):
        return {
            'id': obj.author.id,
            'username': obj.author.username,
            'email': obj.author.email,
            'profile_picture': obj.author.profile_picture.url if obj.author.profile_picture else None
        }

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','content','featured_image','status','published_at','tags']
