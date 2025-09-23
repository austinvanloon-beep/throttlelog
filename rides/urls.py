from django.urls import path
from . import views

urlpatterns = [
    path('', views.rides_index, name='index'),
    path('<int:ride_id>/', views.rides_detail, name='detail'),
    path('create/', views.RideCreate.as_view(), name='rides_create'),
    path('<int:pk>/update/', views.RideUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.RideDelete.as_view(), name='delete'),
]
