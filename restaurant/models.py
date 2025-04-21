from django.db import models
from django.contrib.auth.models import User  # Use Django's built-in User model

class RestaurantTable(models.Model):
    table_number = models.CharField(max_length=10, unique=True)  # Unique table identifier
    capacity = models.IntegerField()  # Number of people the table can accommodate

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"


class RestaurantReservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)  # One-to-Many: A user can make multiple reservations
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)  # One-to-Many: A table can have multiple reservations
    reservation_date = models.DateField()
    reservation_time = models.TimeField()

    def __str__(self):
        return f"Reservation by {self.guest.username} for Table {self.table.table_number} on {self.reservation_date} at {self.reservation_time}"