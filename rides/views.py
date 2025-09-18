from django.shortcuts import render, redirect
from .models import Ride


def rides_index(request):
    rides = Ride.objects.all()
    return render(request, 'rides/index.html', { 'rides': rides })



def rides_detail(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    return render(request, 'rides/detail.html', { 'ride': ride })
