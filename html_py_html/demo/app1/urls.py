from django.urls import path
from . import views

#create url
urlpatterns = [
    path('registration/', views.show_regi),
    path('login/', views.show_login),
    path('home/', views.home),
]
