from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Hourly(models.Model):
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField()
    country = models.CharField()
    condition = models.CharField() ##cloud,rainy,sunny,etc
    condition_img = models.URLField(default='')
    temp_f = models.FloatField(default=30)
    feels_like = models.FloatField(default=30)
    humidity = models.SmallIntegerField()
    uv = models.SmallIntegerField()
    wind_mph = models.SmallIntegerField()
    wind_dir = models.CharField()
    pressure_in = models.SmallIntegerField()
    precip_in = models.SmallIntegerField()

    class Meta:
        ordering = ['date']

    def __str__(self):
    	return str(self.date)