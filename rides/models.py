from django.db import models
from django.contrib.auth.models import User


class Ride(models.Model):
    title = models.CharField(max_length=100)
    mileage = models.IntegerField(null=True, blank=True)
    bike_make = models.CharField(max_length=50, null=True, blank=True)
    bike_model = models.CharField(max_length=50, null=True, blank=True)
    photo = models.URLField(max_length=200, null=True, blank=True)
    attractions = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

