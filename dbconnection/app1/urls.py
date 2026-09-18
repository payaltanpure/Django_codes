from django.urls import path
from .views import *

urlpatterns = [
    path("", register, name="register"),
    path("get_data/", get_data, name="get_data"),
    path("get_data_one/", get_data_one, name="get_data_one"),
    
]
