from django.contrib import admin
from .models import Contact, BusinessEventRegistration, CulturalEventRegistration, \
    CharityEventRegistration, SeminarEventRegistration, FamilyEventRegistration, Home, AboutUs, Services


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
        'state',
        'country',
        'mobile',
        'email',
        'org',
        'title'
    ]


@admin.register(BusinessEventRegistration)
class BusinessEventSelectionAdmin(admin.ModelAdmin):
    list_display = [
        'event_type',
        'event_date',
        'people',
        'food',
        'decoration',
        'cg',
        'publicity',
        'sponsor'
    ]


@admin.register(CulturalEventRegistration)
class CulturalEventSelectionAdmin(admin.ModelAdmin):
    list_display = [
        'event_type',
        'event_date',
        'people',
        'food',
        'decoration',
        'cg',
        'publicity',
        'sponsor'
    ]


@admin.register(SeminarEventRegistration)
class SeminarEventSelectionAdmin(admin.ModelAdmin):
    list_display = [
        'event_type',
        'event_date',
        'people',
        'cg',
        'publicity',
        'sponsor'
    ]


@admin.register(CharityEventRegistration)
class CharityEventSelectionAdmin(admin.ModelAdmin):
    list_display = [
        'event_type',
        'event_date',
        'people',
        'food',
        'decoration',
        'cg',
        'publicity',
        'sponsor'
    ]


@admin.register(FamilyEventRegistration)
class FamilyEventSelectionAdmin(admin.ModelAdmin):
    list_display = [
        'event_type',
        'event_date',
        'people',
        'food',
        'decoration'
    ]


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'company_logo',
        'address',
        'city',
        'email',
        'phone_code',
        'phone',
        'header_info',
        'about_intro',
        'job_title1',
        'pro_first_name1',
        'pro_last_name1',
        'pro_intro1',
        'job_title2',
        'pro_first_name2',
        'pro_last_name2',
        'pro_intro2',
        'job_title3',
        'pro_first_name3',
        'pro_last_name3',
        'pro_intro3',
        'pro_img1',
        'pro_img2',
        'pro_img3',
    ]


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = [
        'mission',
        'mission_bold',
        'vision',
        'vision_bold',
        'testimonial1',
        'testimonial2',
        'testimonial3',
        'testimonial4',
        'client_name1',
        'client_name2',
        'client_name3',
        'client_name4',
    ]


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = [
        'business_intro',
        'business_event_list1',
        'business_event_list2',
        'business_event_list3',
        'business_event_list4',
        'business_event_list5',
        'business_event_list6',
        'family_intro',
        'family_event_list1',
        'family_event_list2',
        'family_event_list3',
        'family_event_list4',
        'family_event_list5',
        'family_event_list6',
        'charity_intro',
        'charity_event_list1',
        'charity_event_list2',
        'charity_event_list3',
        'charity_event_list4',
        'charity_event_list5',
        'charity_event_list6',
        'cultural_intro',
        'cultural_event_list1',
        'cultural_event_list2',
        'cultural_event_list3',
        'cultural_event_list4',
        'seminar_intro',
        'seminar_event_list1',
        'seminar_event_list2',
        'seminar_event_list3',
        'seminar_event_list4',
        'seminar_event_list5',
    ]
