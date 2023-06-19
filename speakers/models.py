from django.db import models

class Speaker(models.Model):
	full_name = models.CharField(max_length=50)
	bios = models.TextField()
	other_info = models.CharField(max_length=200)

	def __str__(self):
		return self.full_name




    

   
