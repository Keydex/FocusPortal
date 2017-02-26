from __future__ import unicode_literals
from mongoengine import *
connect('portal')
from django.db import models

class User(Document):
    id = IntegerField();
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Code(Document):
    id = IntegerField();
    date = DateField(auto=True)
    title = StringField(max_length=120, required=True)
    site = URLField(max_length=200)
    tag = StringField(max_length=30)
    code = StringField()

class Code(Document):
    site = StringField()
    title = StringField(max_length=120)
    category = StringField(max_length=30)
    code = StringField()

    def get_absolute_url(self):
        return reverse("homepage")
