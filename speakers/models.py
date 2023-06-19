from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

