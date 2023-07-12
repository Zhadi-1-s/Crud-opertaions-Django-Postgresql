from django.db import models

# Create your models here.
class User(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=55)
    car = models.CharField(max_length=255)
