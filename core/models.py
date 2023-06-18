from django.db import models

class Model(models.Model):
    # Define fields and their types here
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # ... here you add many fields as you wish

    def __str__(self):
        return self.field1 
 # Return a string representation of the model instance
