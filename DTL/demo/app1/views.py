from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#home page
def home(request):
    return HttpResponse("I am app1 home page")


#get id from url
def get_id(request, id):
    return HttpResponse(f"Hello {id} no student")


#get name from url
def get_name(request, name):
    return HttpResponse(f"Hello {name}")


#get name and id from url
def get_id_name(request, id, name):
    return HttpResponse(f"Hello {name} with id {id}")
