from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name
