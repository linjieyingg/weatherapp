from django.db import models
from weather.models import Observation
from datetime import datetime
# Create your models here.

class Hourly(models.Model):
    date = models.DateTimeField(default=datetime.now().strftime(("%d.%m.%Y %H:00")))
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
    observation_id = models.ForeignKey(Observation, null=True, on_delete=models.PROTECT, related_name='hourlys')

    class Meta:
        ordering = ['date']

    def __str__(self):
    	return self.date