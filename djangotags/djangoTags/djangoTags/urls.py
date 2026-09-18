"""
URL configuration for djangoTags project.

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
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex1/', v.ex1, name= "ex1"),
    path('ex2/<int:marks>/', v.ex2, name= "ex2"),
    path('ex3/<str:name>/', v.ex3, name= "ex3"),
    path('ex4/', v.ex4, name= "ex4"),
    path('ex5/', v.ex5, name="ex5"),
    path("ex6/", v.ex6, name= "ex6"),
]
