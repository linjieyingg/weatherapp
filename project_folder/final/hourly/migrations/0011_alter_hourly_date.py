# Generated by Django 4.2 on 2024-05-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hourly', '0010_alter_hourly_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourly',
            name='date',
            field=models.DateTimeField(default='27.05.2024 14:00'),
        ),
    ]
