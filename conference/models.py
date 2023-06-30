from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
