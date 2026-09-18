from django.core.checks import database
from django.shortcuts import render
from .models import student
# Create your views here.

def register(request):
    if request.method == "POST":
        name= request.POST.get("name")
        lname= request.POST.get("lname")

        # inserted data into student table
        student.objects.create(
            name= name,
            lname= lname
        )
    return render(request, "app1/register.html")



def get_data(request):
    data= student.objects.all()
    return render(request, "app1/op.html", {"data": data})

def get_data_one(request):
    data= student.objects.get(id=1)
    return render(request,  "app1/op.html", {"new": data})


# In Django, ORM stands for Object-Relational Mapping. It lets you work with a database using Python objects instead of writing SQL directly.

# For example, instead of SQL like:

# SELECT * FROM student WHERE age > 18;

# Django ORM lets you write:

# Student.objects.filter(age__gt=18)

# A Django model represents a database table, and each model object generally represents a row:

# from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

# Django can then perform common database operations:
    
# # Create
# Student.objects.create(name="John", age=20)

# # Read
# students = Student.objects.all()

# # Filter
# students = Student.objects.filter(age__gte=18)

# # Update
# student = Student.objects.get(id=1)
# student.age = 21
# student.save()

# # Delete
# student.delete()

# So the basic idea is:

# Python model → Django ORM → SQL → Database