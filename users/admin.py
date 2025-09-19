# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id','email','username','first_name','last_name','is_staff','date_joined')
    search_fields = ('email','username','first_name','last_name')
    list_filter = ('is_staff','is_superuser','is_active')
    fieldsets = (
        (None, {'fields': ('email','username','password')}),
        ('Personal info', {'fields': ('first_name','last_name','bio','profile_picture')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
        ('Important dates', {'fields': ('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username','password1','password2'),
        }),
    )
