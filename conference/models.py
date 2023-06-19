from django.db import models

class Conferences(models.Model):
    name = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    dates = models.DateField(max_length = 255)
    description = models.CharField(max_length = 255)
    hoster = models.CharField(max_length = 255)
# Create your models here.
