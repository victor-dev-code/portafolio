from django.db import models
from django.db.models.fields import CharField, URLField, BooleanField
from django.db.models.fields.files import ImageField

# Create your models here.

class Projects(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='static/images/projects/')
    description = CharField(max_length=250)
    url = URLField(blank=True)
    show = BooleanField(default=0)

class Technologies(models.Model):
    technology = CharField(max_length=30)
