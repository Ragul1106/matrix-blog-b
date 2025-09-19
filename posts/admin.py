from django.contrib import admin
from .models import Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','status','published_at','created_at')
    search_fields = ('title','content','author__email','author__username')
    list_filter = ('status','published_at','created_at','author')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name','slug')
    search_fields = ('name','slug')
