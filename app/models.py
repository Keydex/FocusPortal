from __future__ import unicode_literals
import datetime
from mongoengine import *
connect('portal')
from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone

class User(models.Model):
    email = models.EmailField()

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author, filename)

class Post(models.Model):
    author = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    url = models.URLField()
    code = models.FileField(upload_to=user_directory_path)
    date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse("homepage")

    # Set title for object in the database
    def __str__(self):
        return self.title
