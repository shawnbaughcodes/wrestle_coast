from __future__ import unicode_literals

from django.db import models
from login_and_registration.models import User
# Create your models here.

class Videos(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    image = models.ImageField()
    description = models.TextField()
    season = models.CharField(max_length=255)
    episode = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
