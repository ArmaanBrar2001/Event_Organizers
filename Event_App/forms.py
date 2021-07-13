from django import forms
from .models import Contact, BusinessEventRegistration, CulturalEventRegistration, \
	SeminarEventRegistration, CharityEventRegistration, FamilyEventRegistration

RADIO_CHOICES = [
	('Yes', 'Yes'),
	('No', 'No'),
]


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
			'name',
			'address',
			'state',
			'country',
			'mobile',
			'email',
			'org',
			'title',
			'message'
		]
	
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = 'Full Name'
		self.fields['org'].label = 'Organization Name'
		self.fields['org'].required = False
		self.fields['title'].label = 'Designation'
		self.fields['title'].required = False
		self.fields['message'].required = False
		self.fields['message'].widget.attrs['placeholder'] = 'Type your message'


class BusinessEventsForm(forms.ModelForm):
	class Meta:
		model = BusinessEventRegistration
		fields = [
			'event_type',
			'event_date',
			'people',
			'food',
			'decoration',
			'cg',
			'publicity',
			'sponsor'
		]
	
	def __init__(self, *args, **kwargs):
		super(BusinessEventsForm, self).__init__(*args, **kwargs)
		self.fields['food'].empty_label = 'Select'


class CulturalEventsForm(forms.ModelForm):
	class Meta:
		model = CulturalEventRegistration
		fields = [
			'event_type',
			'event_date',
			'people',
			'food',
			'decoration',
			'cg',
			'publicity',
			'sponsor'
		]


class SeminarEventsForm(forms.ModelForm):
	class Meta:
		model = SeminarEventRegistration
		fields = [
			'event_type',
			'event_date',
			'people',
			'cg',
			'publicity',
			'sponsor'
		]


class CharityEventsForm(forms.ModelForm):
	class Meta:
		model = CharityEventRegistration
		fields = [
			'event_type',
			'event_date',
			'people',
			'food',
			'decoration',
			'cg',
			'publicity',
			'sponsor'
		]


class FamilyEventsForm(forms.ModelForm):
	class Meta:
		model = FamilyEventRegistration
		fields = [
			'event_type',
			'event_date',
			'people',
			'food',
			'decoration'
		]
