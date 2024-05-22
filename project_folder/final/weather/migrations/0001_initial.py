# Generated by Django 5.0.6 on 2024-05-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('location', models.CharField()),
                ('country', models.CharField()),
                ('condition', models.CharField()),
                ('temp_c', models.FloatField()),
                ('temp_f', models.FloatField()),
                ('humidity', models.SmallIntegerField()),
                ('max_c', models.FloatField()),
                ('max_f', models.FloatField()),
                ('min_c', models.FloatField()),
                ('min_f', models.FloatField()),
                ('wind_mph', models.SmallIntegerField()),
                ('wind_dir', models.CharField()),
                ('pressure_in', models.SmallIntegerField()),
                ('precip_in', models.SmallIntegerField()),
                ('sunrise', models.DateTimeField()),
                ('sunset', models.DateTimeField()),
                ('moonrise', models.DateTimeField()),
                ('moonset', models.DateTimeField()),
                ('moon_phase', models.CharField()),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
