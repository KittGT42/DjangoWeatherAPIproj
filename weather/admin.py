from django.contrib import admin

from weather.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
