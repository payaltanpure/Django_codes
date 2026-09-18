from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome3(request):
    return render(request, "app1/welcome3.html")


def welcome4(request):
    return render(request, "app1/welcome4.html")

def details_by_id(request,id):
    return HttpResponse(f"detail no {id}")

def details_by_name(request,uname):
    return HttpResponse(f"detail no {uname}")

def mutiple_para(request,id,name):
    return HttpResponse(f"Id is {id} and name is {name}")


#key value pairs data 
def mutiple_para_kwargs(request,**kwargs):
    return HttpResponse(f"data: {kwargs} ,  id: {kwargs['id']}, name: {kwargs['id']}")
   