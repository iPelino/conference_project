from django.db import models

# Create your models here.
from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length=100)
    dates = models.DateField()
    location = models.CharField(max_length=100)
    topics = models.TextField()



