# Generated by Django 3.2.5 on 2021-07-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event_App', '0003_auto_20210706_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='pro_name',
        ),
        migrations.AddField(
            model_name='home',
            name='pro_first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='home',
            name='pro_last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
