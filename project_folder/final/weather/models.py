from django.db import models
from datetime import date

# Create your models here.

class Observation(models.Model):
    date = models.DateField()
    location = models.CharField()
    country = models.CharField()
    condition = models.CharField() ##cloud,rainy,sunny,etc
    condition_img = models.URLField(default='')
    humidity = models.SmallIntegerField()
    max_f = models.FloatField()
    min_f = models.FloatField()
    wind_mph = models.SmallIntegerField()
    precip_in = models.SmallIntegerField()
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    moonrise = models.DateTimeField()
    moonset = models.DateTimeField()
    moon_phase = models.CharField()
    uv = models.SmallIntegerField(default = 1)
    
    @property
    def is_today(self):
        return date.today() == self.date
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
    	return self.date
    
    
  

        
