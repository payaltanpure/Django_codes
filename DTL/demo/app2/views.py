from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#home
def home(request):
    return HttpResponse("I am home page of app2!")


#1st way hard do not use it
def home_html(request): #when this function gets invoked first it goes to last return becoz now if cond is false beocz now method type is get as user is fetching the webpage so method is get and cons of if is false
    #it goes to home.html and take the input vlaues from user of name and after taking value it comes again to the function with post method as user want to save the data not fetch the data or webpage so now if cond is true
    #so , now inside if code will run the value posted from html page will be taken into vaiable and agin passed to same html page from where we take input 
    #and over their the value is displayed of name 
    if request.method=="POST":
        uname= request.POST.get("fname")
        return render (request, "home.html", {"name":uname})
    return render(request, "home.html")



#this is correct way use this way 
#view calculator
#first call html page to take input 
#then after user given value in input field then after submit button is clicked it goes to action tag written in form tag then it goes to app2/calculation url in urls.py and then overthere there is a url which dirests towards the 
#view of calculation , logic is impelemneted and then agaon on same html page the output is dispalyed by passing output from view to html page in dict form
def view_cal(request):
    return render(request, "calci.html")

def calculation(request):
    if request.method== "POST":
        num1= int(request.POST.get("num1"))
        num2= int(request.POST.get("num2"))
        op= num1+num2
        # print(op)
        data={
            "num1":num1,
            "num2":num2,
            "op":op
        }
        return render(request,"calci.html",data)