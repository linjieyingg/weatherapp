# Generated by Django 5.0.6 on 2024-05-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observation',
            name='max_c',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='min_c',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='temp_c',
        ),
        migrations.AddField(
            model_name='observation',
            name='uv',
            field=models.SmallIntegerField(default=1),
        ),
    ]
