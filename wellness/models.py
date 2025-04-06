from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class WellnessSession(models.Model):
    type = models.CharField(max_length=100)
    schedule = models.DateTimeField()
    is_available = models.BooleanField(default=True)

class WellnessBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(WellnessSession, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()