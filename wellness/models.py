from django.db import models
from django.contrib.auth.models import User  # Use Django's built-in User model

class Treatment(models.Model):
    name = models.CharField(max_length=100)  # Name of the treatment
    description = models.TextField()  # Description of the treatment
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the treatment

    def __str__(self):
        return self.name


class Appointment(models.Model):
    guest = models.ForeignKey(User, on_delete=models.CASCADE)  # One-to-Many: A user can schedule multiple appointments
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)  # One-to-Many: A treatment can be booked multiple times
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"Appointment for {self.guest.username} - {self.treatment.name} on {self.appointment_date} at {self.appointment_time}"