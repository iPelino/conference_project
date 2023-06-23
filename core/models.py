from conference_project.db import models
# Create your models here.
class Conference(models.Model):
    name = models.Charfield(max_length=100)
    date = models.Datefield()
    location = models.Charfield(max_length=100)
    company = models.Charfield()
    organization = models.Charfield(max_length=100)
 def __str__self(self):
     return self.name

