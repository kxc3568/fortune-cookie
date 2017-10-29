from django.db import models

# Create your models here.
class Fortune(models.Model):
	message = models.TextField()
	emotions = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.message

	def create(cls, message, emotions):
		text = ''
		for i in emotions.split(','):
			text += emotions[e] + ' '
		text = text.rstrip()
		fortune = cls.objects.create(message=message, emotions=text)
		return fortune