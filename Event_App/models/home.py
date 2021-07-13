from django.db import models


# Your models here
class Home(models.Model):
	company_name = models.CharField(max_length=100)
	header_info = models.TextField(max_length=500)
	about_intro = models.TextField(max_length=200)
	job_title1 = models.CharField(max_length=50, default='')
	pro_first_name1 = models.CharField(max_length=100, default='')
	pro_last_name1 = models.CharField(max_length=100, default='')
	pro_intro1 = models.TextField(max_length=400, default='')
	job_title2 = models.CharField(max_length=50, default='')
	pro_first_name2 = models.CharField(max_length=100, default='')
	pro_last_name2 = models.CharField(max_length=100, default='')
	pro_intro2 = models.TextField(max_length=400, default='')
	job_title3 = models.CharField(max_length=50, default='')
	pro_first_name3 = models.CharField(max_length=100, default='')
	pro_last_name3 = models.CharField(max_length=100, default='')
	pro_intro3 = models.TextField(max_length=400, default='')
	pro_img1 = models.ImageField(upload_to='pro_images', default='')
	pro_img2 = models.ImageField(upload_to='pro_images', default='')
	pro_img3 = models.ImageField(upload_to='pro_images', default='')
	company_logo = models.ImageField(upload_to='logo', default='')
	address = models.CharField(max_length=20, default='')
	city = models.CharField(max_length=20, default='')
	email = models.CharField(max_length=100, default='')
	phone_code = models.CharField(max_length=2, default='')
	phone = models.CharField(max_length=10, default='')
