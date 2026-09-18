from .views import *
from django.urls import path

urlpatterns = [
    path('homeview/', homeview.as_view() ,name="homeview"),
    # calling view inside the class , as_view() method internally created object of class and calls the method according to type of that method weather post, get , put or delete no need to specify the view name in url like earlier 
    # according to data passed or not passed the view is invoked , the behavior of the view is identified by django internally and that particular view is invoked  , get , post , put and del methods are used in the class and that methods are identified by django internally
    # for eg if data is accepted in html form means method is post then post view should be invoked from the class 
    # if not data get simply without any data and methodthe req came so get virew is invoked from the class

    path('about/', aboutview.as_view(), name="about"),
    path('form/', formview.as_view(), name="form"),
    # path('op/', formview.as_view(), name="op"),
]
