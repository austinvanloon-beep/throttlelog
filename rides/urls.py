from django.urls import path
from . import views

urlpatterns = [
    path('', views.rides_index, name='index'),
    path('<int:ride_id>/', views.rides_detail, name='detail'),
]


