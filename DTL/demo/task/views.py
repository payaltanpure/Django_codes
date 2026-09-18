from django.shortcuts import render

# Create your views here.

def print_name(request):
    data = {"name": "ram",
            "age":15,
            "sub": ["java", "python", "html"]}
    return render (request, 'index.html', data)