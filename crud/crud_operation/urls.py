from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name="home"),

    path('add/', add, name="add"  ),

    path('delete/<int:id>/',delete, name='delete'),

    # path('delete/',delete, name='delete'),

    path('fetch/<int:id>/', fetch, name='fetch'),

    path('update/<int:id>/', update, name='update'),

    path('main/', main, name='main')
]