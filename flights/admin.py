from django.contrib import admin
from .models import Flight, Airport, Passenger


class FlightAdmin(admin.ModelAdmin):
    list_display = ('origin', 'destination', 'duration')


admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger)
