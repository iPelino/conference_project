from django.db import models

class Conference(models.Model):
    name  = models.CharField(max_length=200)
    topic = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name