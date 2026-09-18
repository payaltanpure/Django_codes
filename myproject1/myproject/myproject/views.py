

from django.shortcuts import render,redirect

#call file from main myproject
def welcome1(request):
    return render(request, 'welcome1.html')

def welcome2(request):
    return render(request, 'welcome2.html')
