from django.db import models

# Create your models here.
from django.db import models

class Conference(models.Model):
    conf_name = models.CharField(max_length=100)
    conf_date = models.DateField()
    conf_location = models.CharField(max_length=100)
    conf_organiser=models.CharField(max_length=100)
    conf_cost=models.IntegerField()
    # Add more fields as per your requirements
