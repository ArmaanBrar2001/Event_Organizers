# Generated by Django 3.2.5 on 2021-07-03 03:54

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CharityEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charity_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=30)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('org', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=20)),
                ('message', models.TextField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CulturalEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cultural_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SeminarEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seminar_type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SeminarEventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('people', models.IntegerField()),
                ('cg', models.CharField(max_length=5)),
                ('publicity', models.CharField(max_length=5)),
                ('sponsor', models.CharField(max_length=5)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event_App.seminarevents')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyEventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('people', models.IntegerField()),
                ('food', models.CharField(choices=[('snacks', 'Snacks'), ('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], max_length=10)),
                ('decoration', models.CharField(max_length=40)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event_App.familyevents')),
            ],
        ),
        migrations.CreateModel(
            name='CulturalEventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('people', models.IntegerField()),
                ('food', models.CharField(choices=[('snacks', 'Snacks'), ('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], max_length=10)),
                ('decoration', models.CharField(max_length=40)),
                ('cg', models.CharField(max_length=5)),
                ('publicity', models.CharField(max_length=5)),
                ('sponsor', models.CharField(max_length=5)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event_App.culturalevents')),
            ],
        ),
        migrations.CreateModel(
            name='CharityEventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('people', models.IntegerField()),
                ('food', models.CharField(choices=[('snacks', 'Snacks'), ('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], max_length=10)),
                ('decoration', models.CharField(max_length=40)),
                ('cg', models.CharField(max_length=5)),
                ('publicity', models.CharField(max_length=5)),
                ('sponsor', models.CharField(max_length=5)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event_App.charityevents')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessEventRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('people', models.IntegerField()),
                ('food', models.CharField(choices=[('snacks', 'Snacks'), ('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], max_length=10)),
                ('decoration', models.CharField(max_length=40)),
                ('cg', models.CharField(max_length=5)),
                ('publicity', models.CharField(max_length=5)),
                ('sponsor', models.CharField(max_length=5)),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event_App.businessevents')),
            ],
        ),
    ]
