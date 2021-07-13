from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=80)
	state = models.CharField(max_length=30)
	country = CountryField(blank=False)
	mobile = models.CharField(max_length=12)
	email = models.EmailField()
	org = models.CharField(max_length=100)
	title = models.CharField(max_length=20)
	message = models.TextField(max_length=500, default='')
