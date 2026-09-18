from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),

    
    path('home_html/', views.home_html),


    path('view_cal/', views.view_cal),
    path('calculation/', views.calculation),
]
