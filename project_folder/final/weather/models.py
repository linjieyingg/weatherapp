from django.db import models

# Create your models here.

class Observation(models.Model):
    date = models.DateField()
    location = models.CharField()
    country = models.CharField()
    condition = models.CharField() ##cloud,rainy,sunny,etc
    temp_f = models.FloatField()
    humidity = models.SmallIntegerField()
    max_f = models.FloatField()
    min_f = models.FloatField()
    wind_mph = models.SmallIntegerField()
    wind_dir = models.CharField()
    pressure_in = models.SmallIntegerField()
    precip_in = models.SmallIntegerField()
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    moonrise = models.DateTimeField()
    moonset = models.DateTimeField()
    moon_phase = models.CharField()
    uv = models.SmallIntegerField(default = 1)
    

    class Meta:
        ordering = ['date']

    def __str__(self):
    		return self.name
  
  

        
