from django.shortcuts import render



def home(request):
    return render(request, "home.html")

task=[]
def add_task(request):

    if request.method == 'POST':
        ip= request.POST.get("task")

        if ip:
            task.append(ip)
            print(task)
            return render(request,"home.html", {"task": task})
    return render(request, "add_task.html")




