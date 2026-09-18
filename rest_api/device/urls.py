from device.views import *
from django.urls import path

urlpatterns = [
    path("",welcome, name="welcome"),
    path('save/', save, name="save"),
]
