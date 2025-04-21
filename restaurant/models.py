from django.db import models
from django.contrib.auth.models import User  # Use Django's built-in User model
from datetime import timedelta  # Add this import

class RestaurantTable(models.Model):
    table_number = models.CharField(max_length=10, unique=True)  # Unique table identifier
    capacity = models.IntegerField()  # Number of people the table can accommodate

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"

class RestaurantReservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey('RestaurantTable', on_delete=models.CASCADE)
    reservation_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    duration = models.DurationField(default=timedelta(hours=2))

    def __str__(self):
        return f"Reservation '{self.reservation_name}' by {self.guest.username} for Table {self.table.table_number} on {self.reservation_date} at {self.reservation_time}"