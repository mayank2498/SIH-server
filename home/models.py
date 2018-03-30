from django.db import models

class Weather(models.Model):
    lat = models.CharField(default=0,null=False,max_length=140)
    lon = models.CharField(default=0,null=False,max_length=140)
    timestamp = models.CharField(max_length=140)
    precipIntensity = models.CharField(max_length=140)
    precipProbability = models.CharField(max_length=140)
    dewPoint = models.CharField(max_length=140)
    humidity = models.CharField(max_length=140)
    pressure = models.CharField(max_length=140)
    windSpeed = models.CharField(max_length=140)
    cloudCover = models.CharField(max_length=140)
    uvIndex = models.CharField(max_length=140)
    ozone = models.CharField(max_length=140)

    