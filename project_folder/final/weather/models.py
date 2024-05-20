from django.db import models

# Create your models here.

class Observation(models.Model):
    date = models.DateTimeField()
    location = models.CharField()
    country = models.CharField()
    condition = models.CharField() ##cloud,rainy,sunny,etc
    temp_c = models.FloatField()
    temp_f = models.FloatField()
    humidity = models.SmallIntegerField()
    max_c = models.FloatField()
    max_f = models.FloatField()
    min_c = models.FloatField()
    min_f = models.FloatField()
    uv = models.SmallIntegerField()
    wind_mph = models.SmallIntegerField()
    wind_dir = models.CharField()
    pressure_in = models.SmallIntegerField()
    precip_in = models.SmallIntegerField()

    class Meta:
        ordering = ['date']

    def __str__(self):
    		return self.name
  
class Forecast(models.Model):
    date = models.DateTimeField()
    location = models.CharField()
    country = models.CharField()
    condition = models.CharField() ##cloud,rainy,sunny,etc
    temp_c = models.FloatField()
    temp_f = models.FloatField()
    humidity = models.SmallIntegerField()
    max_c = models.FloatField()
    max_f = models.FloatField()
    min_c = models.FloatField()
    min_f = models.FloatField()
    uv = models.SmallIntegerField()
    wind_mph = models.SmallIntegerField()
    wind_dir = models.CharField()
    pressure_in = models.SmallIntegerField()
    precip_in = models.SmallIntegerField()

    class Meta:
        ordering = ['date']

    def __str__(self):
    		return self.name
  

        
