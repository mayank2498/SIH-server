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

class Soil(models.Model):
    LAT=models.CharField(max_length=100,default=True)
    LON=models.CharField(max_length=100,default=True)
    ALUM3S=models.CharField(max_length=100,default="45")
    SNDPPT=models.CharField(max_length=100,default=True)
    SLTPPT=models.CharField(max_length=100,default=True)
    CLYPPT=models.CharField(max_length=100,default=True)
    PHIHOX=models.CharField(max_length=100,default=True)
    AWCH1=models.CharField(max_length=100,default=True)

class Farmer(models.Model):
    name=models.CharField(max_length=500,default=True)
    address=models.CharField(max_length=1000,default=True)
    aadhar=models.CharField(max_length=16,default=True)
    mobile=models.CharField(max_length=10,default=True)

    def __str__(self):
        return self.name


class post_question(models.Model):
    name=models.CharField(max_length=200)
    ask = models.CharField(max_length=20000)
    def __unicode__(self):
        return self.name


class answer(models.Model):
    ques = models.ForeignKey(post_question)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    def __str__(self):
          return self.user_name
