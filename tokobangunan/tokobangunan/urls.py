from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('batubata/', include('batubata.urls')),
    path('cat/', include('cat.urls')),
    path('genting/', include('genting.urls')),
]
