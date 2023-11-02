# Generated by Django 4.2 on 2023-10-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.IntegerField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=20)),
                ('record_of_crime_status', models.CharField(max_length=100)),
                ('safety_tips', models.CharField(max_length=100)),
            ],
        ),
    ]
