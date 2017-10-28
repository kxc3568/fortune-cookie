from django.db import models

# Create your models here.
class Fortune(models.Model):
	fortune = models.TextField()

	def __str__(self):
		return self