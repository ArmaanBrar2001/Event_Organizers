# Generated by Django 3.2.5 on 2021-07-06 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event_App', '0004_auto_20210706_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='home_business_img',
        ),
        migrations.RemoveField(
            model_name='home',
            name='home_charity_img',
        ),
        migrations.RemoveField(
            model_name='home',
            name='home_cultural_img',
        ),
        migrations.RemoveField(
            model_name='home',
            name='home_family_img',
        ),
        migrations.RemoveField(
            model_name='home',
            name='home_seminar_img',
        ),
    ]