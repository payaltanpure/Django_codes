from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Student

def add_student(request):

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        course = request.POST.get("course")
        marks = request.POST.get("marks")

        # ORM - inserting data into database
        Student.objects.create(
            name=name,
            age=age,
            course=course,
            marks=marks
        )

    return render(request, "app1/index.html")



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