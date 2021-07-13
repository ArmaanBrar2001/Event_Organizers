from django.urls import path
from . import views

urlpatterns = [
	path('home', views.home, name='Home'),
	path('about-us', views.about, name='About'),
	path('services', views.services, name='Services'),
	path('contact-form', views.contact_form, name='Contact_Info_Form'),
	path('business-events', views.business_events, name='Business_Events_Form'),
	path('cultural-events', views.cultural_events, name='Cultural_Events_Form'),
	path('charity-events', views.charity_events, name='Charity_Events_Form'),
	path('seminars', views.seminars, name='Seminars_Form'),
	path('family-events', views.family_events, name='Family_Events_Form'),
	path('thank-you', views.thank_you, name='Thanks'),
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('logout', views.logout, name='logout'),
]
