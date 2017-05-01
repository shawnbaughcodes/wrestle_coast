from __future__ import unicode_literals

from django.db import models
from login_and_registration.models import User, Config
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField()
    user = models.ForeignKey(User, related_name='company')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Season(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    name = models.ForeignKey(Company, related_name='company')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Episode(models.Model):
    number = models.IntegerField()
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    image = models.FileField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
