from django.shortcuts import render

# Create your views here.


def get_view(request):
    return render(request, 'index.html')
