from django.contrib import admin
from .models import Flight

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_name', 'departure_date', 'departure_time', 'departure_city', 'destination_city')
