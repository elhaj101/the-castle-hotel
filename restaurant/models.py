from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class RestaurantTable(models.Model):
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

class RestaurantBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()