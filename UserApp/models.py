from django.db import models
from datetime import timedelta

class User(models.Model):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=150)  # Fixed typo here
    age = models.PositiveIntegerField(null=True, blank=True)
    dateofbirth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username + '\'s Profile'

class Period(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()  # Fixed typo here
    end_date = models.DateField()  # Fixed typo here

    def __str__(self):
        return self.user.username + "'s Period"
    
