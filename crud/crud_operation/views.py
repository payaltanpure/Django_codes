from django.shortcuts  import get_object_or_404, redirect, render 
from django.contrib import messages
from .models import student

# Create your views here.
def home(request):
   return render(request, "crud_operation/home.html")


def add(request):
   if request.method == "POST":
      name= request.POST.get("name")
      marks= request.POST.get("marks")

      student.objects.create(
         name= name,
         marks= marks
      )

      messages.success(request, "Student added successfully!")


   return render(request, "crud_operation/add.html")


def main(request):

   students = student.objects.all()
   return render(request, "crud_operation/main.html", {'students': students})

# def delete(request):
#    if request.method == "POST":
#       name= request.POST.get("name")
#       student.objects.filter(name=name).delete()
#       messages.success(request, "Student deleted successfully!")

#    return render(request, "crud_operation/delete.html")


def delete(request, id):

    stu = get_object_or_404(student, id=id)

    stu.delete()

    messages.success(request, "Student deleted successfully!")

    return redirect('home')


def fetch(request):
   pass


def update(request):
   pass


