from django.contrib import admin

from django.contrib import admin
from .models import RestaurantTable, RestaurantReservation

admin.site.register(RestaurantTable)
admin.site.register(RestaurantReservation)