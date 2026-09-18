from django.shortcuts import render
from django.http import HttpResponse
from device.models import device

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

def welcome(request):
    return HttpResponse("Hello Restapi!")


# def save(request):
#     if request.method=='POST':
#         name= request.POST.get("name")
#         price= request.POST.get("price")
#         brand= request.POST.get("price")

#         device.objects.create(name=name, price=price, brand=brand)
#         return HttpResponse("Data saved")
#     return HttpResponse("Invalid method type")



@api_view(['POST'])
def save(request):
    name= request.data.get("name")
    price= request.data.get("price")
    brand= request.data.get("brand")
    return Response(f"name is {name} price is {price} brand is {brand}")



    