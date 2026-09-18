"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import *
from django_task.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # this views present in shop/views.py
    path('', home_view),  #infront of url if we do not put anything empty empty this message will get display as reponse on the request
    path('show/', show),   #infront of url if we put show this message will get display as reponse on the request
    path('access/', access_html),
    path('get_view/', get_view),
]

