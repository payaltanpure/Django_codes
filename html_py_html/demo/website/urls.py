from django.urls import path
from  . import views as v

urlpatterns = [
    path('index/', v.index),
    path('home1/', v.home1 ,name="home1"),
    #name attribure is compulsory to give when we pass url from html file using url tag not in action tag or redirect in view

    path('contactus/', v.contactus, name="contactus"),
    path('next/', v.next, name="next"),
    path('back/', v.back, name="back"),

]
