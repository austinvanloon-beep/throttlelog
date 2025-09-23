from django.urls import path
from . import views

urlpatterns = [
    path('', views.community, name='community'),
    path('rides/', views.rides_index, name='index'),
    path('rides/<int:ride_id>/', views.rides_detail, name='detail'),
    path('rides/create/', views.RideCreate.as_view(), name='rides_create'),
    path('rides/<int:pk>/update/', views.RideUpdate.as_view(), name='rides_update'),
    path('rides/<int:pk>/delete/', views.RideDelete.as_view(), name='rides_delete'),
]
