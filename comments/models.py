from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    page = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)