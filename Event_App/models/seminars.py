from django.db import models


# Create your models here.
class SeminarEvents(models.Model):
	seminar_type = models.CharField(max_length=30)
	
	def __str__(self):
		return self.seminar_type


class SeminarEventRegistration(models.Model):
	event_type = models.ForeignKey(SeminarEvents, on_delete=models.CASCADE)
	event_date = models.DateField()
	people = models.IntegerField()
	cg = models.CharField(max_length=5)
	publicity = models.CharField(max_length=5)
	sponsor = models.CharField(max_length=5)
