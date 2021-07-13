from django.db import models

FOOD_CHOICES = [
	('snacks', 'Snacks'),
	('breakfast', 'Breakfast'),
	('lunch', 'Lunch'),
	('dinner', 'Dinner'),
]


# Create your models here.
class CharityEvents(models.Model):
	charity_type = models.CharField(max_length=30)
	
	def __str__(self):
		return self.charity_type


class CharityEventRegistration(models.Model):
	event_type = models.ForeignKey(CharityEvents, on_delete=models.CASCADE)
	event_date = models.DateField()
	people = models.IntegerField()
	food = models.CharField(max_length=10, choices=FOOD_CHOICES)
	decoration = models.CharField(max_length=40)
	cg = models.CharField(max_length=5)
	publicity = models.CharField(max_length=5)
	sponsor = models.CharField(max_length=5)
