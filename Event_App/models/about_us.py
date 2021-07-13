from django.db import models


# Your models here
class AboutUs(models.Model):
	mission = models.TextField(max_length=500)
	mission_bold = models.TextField(max_length=300)
	vision = models.TextField(max_length=500)
	vision_bold = models.TextField(max_length=300)
	testimonial1 = models.TextField(max_length=800)
	testimonial2 = models.TextField(max_length=800)
	testimonial3 = models.TextField(max_length=800)
	testimonial4 = models.TextField(max_length=800)
	client_name1 = models.CharField(max_length=100)
	client_name2 = models.CharField(max_length=100)
	client_name3 = models.CharField(max_length=100)
	client_name4 = models.CharField(max_length=100)
