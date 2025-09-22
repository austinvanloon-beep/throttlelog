from django.urls import path
from . import views
from .views import rides_index, rides_detail, RideCreate



urlpatterns = [
    path('', rides_index, name='index'),
    path('<int:ride_id>/', rides_detail, name='detail'),
    path('create/', RideCreate.as_view(), name='rides_create'),
]
