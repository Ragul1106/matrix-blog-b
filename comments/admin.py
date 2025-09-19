from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','post','author','is_approved','created_at')
    search_fields = ('author__email','author__username','content','post__title')
    list_filter = ('is_approved','created_at')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f"{updated} comments approved.")
    approve_comments.short_description = "Approve selected comments"
