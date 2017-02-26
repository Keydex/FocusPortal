from __future__ import unicode_literals
import datetime
from mongoengine import *
connect('portal')
from django.db import models
from django import forms
from django.core.urlresolvers import reverse

class CategoryField(models.CharField):
    def to_python(self, value):
        return value.lower()

class Post(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    url = models.URLField()
    code = models.FileField(upload_to="snippets/")
    date = models.DateTimeField(auto_now=True)
    category = CategoryField(max_length=30)

    def get_absolute_url(self):
        return reverse("homepage")
