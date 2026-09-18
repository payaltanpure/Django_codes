
from django.shortcuts import render 

def webpage(request):
    return render(request, "webpage.html")

def homepage(request):
    return render(request, "home.html")