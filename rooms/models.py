from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"


class Reservation(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField(max_length=100)
    children = models.CharField(max_length=10)
    extras = models.CharField(max_length=255, blank=True)
    agree = models.BooleanField(default=False)
    # Add other fields as needed

    def clean(self):
        super().clean()
        today = timezone.now().date()
        if self.check_in_date < today:
            raise ValidationError({'check_in_date': "Check-in date cannot be in the past."})
        if self.check_out_date <= self.check_in_date:
            raise ValidationError({'check_out_date': "Check-out date must be after check-in date."})

    def __str__(self):
        return f"Reservation by {self.guest.username} for Room {self.room.room_number}"