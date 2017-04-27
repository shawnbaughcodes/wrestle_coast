from __future__ import unicode_literals
from login_and_registration.models import User
from django.db import models
import re, bcrypt
# Create your models here.


class Series(models.Model):
    name = models.CharField(max_length=300)
    creator = models.CharField(max_length=255)
    company = models.CharField()
    rating = models.IntegerField()
    description = models.TextField()
    img = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Season(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Episodes(models.Model):
    name = models.CharField(max_length=300)
    url = models.CharField()
    img = models.ImageField()
    description = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
