from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=100)
    seniority = models.CharField(max_length=50, choices=[
        'Junior',
        'Mid-level',
        'Senior',
        'Lead'
    ])

    def __str__(self):
        return f"{self.name} ({self.seniority})"


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username
