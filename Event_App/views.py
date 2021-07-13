from django.shortcuts import render, redirect
from .models import Contact, Home, AboutUs, Services, BusinessEventRegistration, \
	CulturalEventRegistration, SeminarEventRegistration, CharityEventRegistration, \
	FamilyEventRegistration
from .forms import ContactForm, BusinessEventsForm, CulturalEventsForm, SeminarEventsForm, \
	CharityEventsForm, FamilyEventsForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib.auth.decorators import login_required
import smtplib


# Create your views here.
def navi(request):
	home = Home.objects.all()
	return render(request, 'navigation.html', {'home': home})


def footer(request):
	home = Home.objects.all()
	return render(request, 'footer.html', {'home': home})


def register(request):
	if request.method == 'POST':
		email = request.POST['email']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		
		if password1 == password2:
			if User.objects.filter(username=username):
				messages.info(request, 'Username already exists!')
				return redirect('register')
			
			elif User.objects.filter(email=email):
				messages.info(request, 'Email already registered!')
				return redirect('register')
			
			else:
				user = User.objects.create_user(email=email, username=username, password=password1)
				user.save()
				print('Registration Complete')
				subject = 'welcome to Events Management App'
				message = f'Hi {user.username}, thank you for registering with Events Management. \n We are looking forward to work with you. We are a group of creative event ' \
				          'managers, you will not regret hiring us for your event.'
				sender = settings.EMAIL_HOST_USER
				email_password = settings.EMAIL_HOST_PASSWORD
				s = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
				
				s.starttls()
				
				s.login(sender, email_password)
				
				s.sendmail(sender, [user.email, ], subject, message)
				s.quit()
				return redirect('login')
		
		else:
			messages.info(request, 'Passwords do not match!')
			return redirect(register)
	
	else:
		return render(request, 'register.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('Home')
		else:
			messages.info(request, 'Username or password are invalid!')
			return redirect('login')
	
	else:
		return render(request, 'login.html')


def logout(request):
	auth.logout(request)
	return redirect('Home')


def contact_form(request, id=0):
	home = Home.objects.all()
	if request.method == 'GET':
		if id == 0:
			form = ContactForm()
		else:
			contact = Contact.objects.get(pk=id)
			form = ContactForm(instance=contact)
		return render(request, 'contact_form.html', {'form': form, 'home': home})
	
	else:
		if id == 0:
			form = ContactForm(request.POST)
		else:
			contact = Contact.objects.get(pk=id)
			form = ContactForm(request.POST, instance=contact)
		if form.is_valid():
			form.save()
		return redirect('Home')


def home(request):
	home = Home.objects.all()
	return render(request, 'Home.html', {'home': home})


def services(request):
	home = Home.objects.all()
	serv = Services.objects.all()
	return render(request, 'services.html', {'home': home, 'serv': serv})


def about(request):
	home = Home.objects.all()
	about = AboutUs.objects.all()
	return render(request, 'about_us.html', {'home': home, 'about': about})


def thank_you(request):
	home = Home.objects.all()
	return render(request, 'reply.html', {'home': home})


@login_required(login_url='login')
def business_events(request, id=0):
	home = Home.objects.all()
	if request.method == 'GET':
		if id == 0:
			form = BusinessEventsForm()
		else:
			event = BusinessEventRegistration.objects.get(pk=id)
			form = BusinessEventsForm(instance=event)
		return render(request, 'business_events.html', {'form': form, 'home': home})
	
	else:
		if id == 0:
			form = BusinessEventsForm(request.POST)
		else:
			event = BusinessEventRegistration.objects.get(pk=id)
			form = BusinessEventsForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
		return redirect('Thanks')


@login_required(login_url='login')
def cultural_events(request, id=0):
	home = Home.objects.all()
	if request.method == 'GET':
		if id == 0:
			form = CulturalEventsForm()
		else:
			event = CulturalEventRegistration.objects.get(pk=id)
			form = CulturalEventsForm(instance=event)
		return render(request, 'cultural_events.html', {'form': form, 'home': home})
	
	else:
		if id == 0:
			form = CulturalEventsForm(request.POST)
		else:
			event = CulturalEventRegistration.objects.get(pk=id)
			form = CulturalEventsForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
		return redirect('Thanks')


@login_required(login_url='login')
def charity_events(request, id=0):
	home = Home.objects.all()
	if request.method == 'GET':
		if id == 0:
			form = CharityEventsForm()
		else:
			event = CharityEventRegistration.objects.get(pk=id)
			form = CharityEventsForm(instance=event)
		return render(request, 'charity_events.html', {'form': form, 'home': home})
	
	else:
		if id == 0:
			form = CharityEventsForm(request.POST)
		else:
			event = CharityEventRegistration.objects.get(pk=id)
			form = CharityEventsForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
		return redirect('Thanks')


@login_required(login_url='login')
def seminars(request, id=0):
	home = Home.objects.all()
	if request.method == 'GET':
		if id == 0:
			form = SeminarEventsForm()
		else:
			event = SeminarEventRegistration.objects.get(pk=id)
			form = SeminarEventsForm(instance=event)
		return render(request, 'seminars.html', {'form': form, 'home': home})
	
	else:
		if id == 0:
			form = SeminarEventsForm(request.POST)
		else:
			event = SeminarEventRegistration.objects.get(pk=id)
			form = SeminarEventsForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
		return redirect('Thanks')


@login_required(login_url='login')
def family_events(request, id=0):
	home = Home.objects.all()
	if request.method == 'GET':
		if id == 0:
			form = FamilyEventsForm()
		else:
			event = FamilyEventRegistration.objects.get(pk=id)
			form = FamilyEventsForm(instance=event)
		return render(request, 'family_events.html', {'form': form, 'home': home})
	
	else:
		if id == 0:
			form = FamilyEventsForm(request.POST)
		else:
			event = FamilyEventRegistration.objects.get(pk=id)
			form = FamilyEventsForm(request.POST, instance=event)
		if form.is_valid():
			form.save()
		return redirect('Thanks')
