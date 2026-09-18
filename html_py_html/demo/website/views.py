from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def home1(request):
    return render(request, "home1.html")

def contactus(request):
    return render(request, "contactus.html")

def next(request):
    return render(request, "next.html")

def back(request):
    return render(request, "index.html")

