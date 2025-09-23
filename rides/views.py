from django.shortcuts import render
from .models import Ride
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView


# rides private to user
def rides_index(request):
    rides = Ride.objects.filter(user=request.user)
    return render(request, 'rides/index.html', { 'rides': rides })

# rides public to all users
# def rides_index(request):
#    rides = Ride.objects.all()
#    return render(request, 'rides/index.html', {'rides': rides})


def rides_detail(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    return render(request, 'rides/detail.html', { 'ride': ride })


class RideCreate(LoginRequiredMixin, CreateView):
    model = Ride
    fields = ['title', 'mileage', 'bike_make', 'bike_model', 'photo', 'attractions', 'notes', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RideUpdate(LoginRequiredMixin, UpdateView):
    model = Ride
    fields = ['title', 'mileage', 'bike_make', 'bike_model', 'photo', 'attractions', 'notes', 'date']

    def get_queryset(self):
        return Ride.objects.filter(user=self.request.user)


class RideDelete(LoginRequiredMixin, DeleteView):
    model = Ride
    success_url = '/rides/'

    def get_queryset(self):
        return Ride.objects.filter(user=self.request.user)

