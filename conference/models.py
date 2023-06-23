from django.db import models

# Create your models here.
class Conference(models.Model):
    name = models.CharField(max_length=100)
    dates = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    topics = models.TextField()

    def __str__(self):
        return self.name
