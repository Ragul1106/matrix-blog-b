# comments/serializers.py
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id','post','author','content','is_approved','created_at','updated_at']
        read_only_fields = ['is_approved','created_at','updated_at','author']

    def get_author(self, obj):
        return {'id': obj.author.id, 'username': obj.author.username, 'email': obj.author.email}
