from django.db import models

FOOD_CHOICES = [
	('snacks', 'Snacks'),
	('breakfast', 'Breakfast'),
	('lunch', 'Lunch'),
	('dinner', 'Dinner'),
]


# Create your models here.
class FamilyEvents(models.Model):
	family_type = models.CharField(max_length=30)
	
	def __str__(self):
		return self.family_type


class FamilyEventRegistration(models.Model):
	event_type = models.ForeignKey(FamilyEvents, on_delete=models.CASCADE)
	event_date = models.DateField()
	people = models.IntegerField()
	food = models.CharField(max_length=10, choices=FOOD_CHOICES)
	decoration = models.CharField(max_length=40)
