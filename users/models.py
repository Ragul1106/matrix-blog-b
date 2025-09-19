# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

def user_profile_pic_path(instance, filename):
    return f'profiles/{instance.username}/{filename}'

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=user_profile_pic_path, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.email
