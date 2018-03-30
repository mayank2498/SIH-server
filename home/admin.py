from django.contrib import admin

from .models import Weather
class CartAdmin(admin.ModelAdmin):
	list_display = ["lat","lon","timestamp","precipIntensity","precipProbability","humidity","pressure"]
admin.site.register(Weather,CartAdmin)
