from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"


class Reservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)  # Use User for guests
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reservation by {self.guest.username} for Room {self.room.room_number}"