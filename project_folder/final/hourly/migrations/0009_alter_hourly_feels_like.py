# Generated by Django 5.0.6 on 2024-05-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hourly', '0008_alter_hourly_feels_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourly',
            name='feels_like',
            field=models.FloatField(),
        ),
    ]
