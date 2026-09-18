from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("<h1>Hello I am from Django</h1>")


def show(request):
    return HttpResponse("<h1>Hello Django</h1>")

def access_html(request):
    return render(request, 'index.html')