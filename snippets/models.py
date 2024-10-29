from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(default= "", max_length=50)
    age = models.PositiveIntegerField()