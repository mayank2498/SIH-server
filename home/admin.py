from django.contrib import admin

from .models import Weather
class CartAdmin(admin.ModelAdmin):
	list_display = ["lat","lon","timestamp","precipIntensity","precipProbability","humidity","pressure"]
admin.site.register(Weather,CartAdmin)


from .models import Soil,Farmer,answer,post_question
# Register your models here.
class SoilAdmin(admin.ModelAdmin):
	list_display=["LAT","LON","ALUM3S","SNDPPT","SLTPPT","CLYPPT","PHIHOX","AWCH1"]
admin.site.register(Soil,SoilAdmin)

admin.site.register(Farmer)
admin.site.register(answer)
admin.site.register(post_question)
