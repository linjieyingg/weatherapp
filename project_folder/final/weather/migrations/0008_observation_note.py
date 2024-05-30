from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0007_remove_observation_pressure_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='observation',
            name='note',
            field=models.CharField(default=''),
        ),
    ]
