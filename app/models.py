from __future__ import unicode_literals
from mongoengine import *
connect('portal')
from django.db import models

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Post(Document):
    title = StringField(max_length=120, required=True)
    tag = ListField(StringField(max_length=30))
    code = StringField()
