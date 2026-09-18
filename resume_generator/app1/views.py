from django.shortcuts import render

# Create your views here.

def form(request):
    return render(request, "app1/input.html")

def resume(request):
    if request.method =='POST':
        data={
            "name":request.POST.get("name"),
            "email": request.POST.get("email"),
            "skills": request.POST.get("skills"),
            "mobno": request.POST.get("mob_no")
        }

        return render(request, "app1/resume.html", data)
    return render(request, "app1/input.html")