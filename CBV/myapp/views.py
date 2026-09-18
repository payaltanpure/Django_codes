from django.shortcuts import render
from django.views import View 
# imported view module becoz we want to create class in this view.py and the view inside that class
from django.http import HttpResponse

# Create your views here.

class homeview(View):
    def get(self, request):
        return HttpResponse("HII")
    
class aboutview(View):
    def get(self, request):
        return render(request, 'myapp/about.html')
    
class formview(View):
    def get(self, request):
        return render(request, "myapp/form.html")
    
    # def get(self, request):
    #     return render(request, "myapp/op.html")
    
    def post(self, request):
        if request.method == 'POST':
            fname= request.POST.get("name")
            print(fname)
            return render(request, 'myapp/op.html', {'fname': fname})
        # return render (request, 'myapp/form.html')

    

