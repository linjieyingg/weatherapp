from django.db import models

# Create your models here.

class Observation(models.Model):
    date = models.DateField()
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
    wind_mph = models.SmallIntegerField()
    wind_dir = models.CharField()
    pressure_in = models.SmallIntegerField()
    precip_in = models.SmallIntegerField()
    

    class Meta:
        ordering = ['date']

    def __str__(self):
    		return self.name
  
class Hourly(models.Model):
    date = models.DateTimeField()
    location = models.CharField()
    country = models.CharField()
    condition = models.CharField() ##cloud,rainy,sunny,etc
    temp_c = models.FloatField()
    temp_f = models.FloatField()
    humidity = models.SmallIntegerField()
    uv = models.SmallIntegerField()
    wind_mph = models.SmallIntegerField()
    wind_dir = models.CharField()
    pressure_in = models.SmallIntegerField()
    precip_in = models.SmallIntegerField()
    observation_id = models.ForeignKey(Observation, null=True, on_delete=models.SET_NULL)


    class Meta:
        ordering = ['date']

    def __str__(self):
    		return self.name
  

        
