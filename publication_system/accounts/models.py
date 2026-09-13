from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", default="avatars/default.png")
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[
            ("M", "Male"),
            ("F", "Female"),
            ("N", "Non-binary"),
            ("O", "Other"),
        ],
        blank=True,
        null=True,  
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    is_verified = models.BooleanField(default=False)
    email_notifications = models.BooleanField(default=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orcid = models.CharField(max_length=50, blank=True, null=True)
    affiliation = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Author: {self.user.username}"


class Reviewer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    expertise = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reviewer: {self.user.username}"


class Editor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Editor: {self.user.username}"