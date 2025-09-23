from django.contrib import admin
from django.urls import path, include
from rides import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.community, name='community'),
    path('rides/', include('rides.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
