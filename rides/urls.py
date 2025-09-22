from django.urls import path, include
from . import views
from .views import rides_index, rides_detail, RideCreate, RideUpdate, RideDelete
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rides/', include('rides.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]