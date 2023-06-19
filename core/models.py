from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    dates = models.DateField(max_length = 255)
    topic = models.CharField(max_length = 255)

# Create your models here.
