from django.urls import path
from .views import *

urlpatterns = [
    path('form/', form , name="form"),
    path('resume/', resume , name="resume"),
]
