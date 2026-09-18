from django.shortcuts import render 

def index(request):
    return render(request, "index.html")

def mobile(request):
    return render(request, "mobile.html")

def beauty(request):
    return render(request, "beauty.html")

def index2(request):
    return render(request, "index2.html")