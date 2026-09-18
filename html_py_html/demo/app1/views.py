# here we used redirect instead of passing action tag in form tag to redirect to new web page beocz of path issue
# In one sentence:
# ✅ redirect() → sends the browser to another URL, which again goes through urls.py → view → render() (or another response).
# ✅ render() → is called inside a view and returns the HTML template as the response to the browser.

# So your statement is almost correct. A more accurate version is:

# redirect() sends the browser to another URL, which is matched in urls.py, calls another view, and that view usually renders an HTML page. 
# render() is called from inside a view and directly returns an HTML template as the response.


# | `render()`                | `redirect()`                                                           |
# | ------------------------- | ---------------------------------------------------------------------- |
# | Displays an HTML template | Sends the browser to another URL                                       |
# | No new request            | Creates a new request                                                  |
# | Stays in the same view    | Calls another view through `urls.py`                                   |
# | Used to show pages        | Used after actions like login, logout, registration, update, or delete |
# | Returns HTML directly     | Returns a redirect response (HTTP 302 by default)                      |


# render() = "Show this page."
# redirect() = "Go to that URL first."

#render used when we want to pass the data html page as redirext do not pass the data to html page 



from django.shortcuts import render,redirect

# Create your views here.

data={}
#register form showing  view
def show_regi(request):
    if request.method== "POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        password= request.POST.get("pass")
        #set dict
        data["name"]= name
        data["email"]= email
        data["password"]= password
        return redirect("/app1/login/")
    
    return render(request,"registration.html")

#login form showing view
def show_login(request):
    msg=""
    #existing data should match to recent data login data and registration data should match
    if request.method == "POST":
        #data receive of login form
        email= request.POST.get("email")
        password= request.POST.get("pass")
        if email==data['email'] and password==data["password"]:
            # return redirect("/app1/home/")
            #used render becoz we want to pass data to home.html
            return render(request, "home.html", {"name": data["name"]})

        else:
            msg="Invalid credentials!"
            # return redirect('/app1/login')
            #used render becoz we want to pass data to home.html
            return render(request, "login.html", {"msg": msg})
    
    return render(request, "login.html")

#home page showing view
def home(request):
    return render(request, "home.html")






# Great question. Understanding the flow is much more important than memorizing the code. Let's go through exactly what happens from the moment the user opens the application until they see the home page.

# Project Flow
# Browser
#    │
#    ▼
# Registration Page
#    │
#    ▼
# Register User
#    │
#    ▼
# Store data in dictionary
#    │
#    ▼
# Redirect to Login Page
#    │
#    ▼
# Login Page
#    │
#    ▼
# Enter Email & Password
#    │
#    ▼
# Compare with dictionary
#    │
#    ├── Correct
#    │      ▼
#    │   Render Home Page
#    │      ▼
#    │   Welcome Payal
#    │
#    └── Wrong
#           ▼
#    Login Page + Invalid Credentials
# Step 1 : User visits Registration page

# URL

# http://127.0.0.1:8000/app1/registration/

# Django checks

# urls.py
# urlpatterns = [
#     path('registration/', views.show_regi),
# ]

# It says

# If URL is /registration/, call

# show_regi()
# Step 2 : show_regi() executes

# Initially

# def show_regi(request):

# Suppose the user just opened the page.

# The request method is

# GET

# So this condition

# if request.method == "POST":

# becomes

# False

# Therefore Django executes

# return render(request,"registration.html")

# Meaning

# Browser
#       ↓
# registration.html

# The browser now displays

# Name
# Email
# Password
# Register Button
# Step 3 : User fills the form

# Suppose user enters

# Name : Payal

# Email : payal@gmail.com

# Password : 123

# and clicks

# Register

# Now browser sends

# POST Request

# to

# /registration/

# Now

# request.method

# becomes

# POST
# Step 4 : Read form data

# These lines execute

# name = request.POST.get("name")

# What happens?

# Browser sent

# name=Payal

# So

# name

# ↓

# "Payal"

# Similarly

# email = request.POST.get("email")

# becomes

# payal@gmail.com

# And

# password = request.POST.get("pass")

# becomes

# 123

# Now variables are

# name = "Payal"

# email = "payal@gmail.com"

# password = "123"
# Step 5 : Store inside dictionary

# Initially

# data={}

# Empty dictionary

# {}

# After

# data["name"]=name

# Dictionary becomes

# {
# "name":"Payal"
# }

# Next

# data["email"]=email

# becomes

# {
# "name":"Payal",
# "email":"payal@gmail.com"
# }

# Next

# data["password"]=password

# Dictionary becomes

# {
# "name":"Payal",
# "email":"payal@gmail.com",
# "password":"123"
# }

# This dictionary is stored in memory.

# Step 6 : Redirect

# Now

# return redirect("/app1/login/")

# Very important.

# Many beginners think redirect sends data.

# It DOES NOT.

# It only tells browser

# Go to this URL

# Response sent

# 302 Redirect

# Browser immediately opens

# /app1/login/
# Step 7 : URL mapping again

# Now Django checks

# urls.py
# path("login/",views.show_login)

# So

# show_login()

# is called.

# Step 8 : First time Login page opens

# Method

# GET

# So

# if request.method=="POST"

# is False.

# Hence

# return render(request,"login.html")

# Browser shows

# Email

# Password

# Login Button
# Step 9 : User enters login details

# Suppose

# Email

# payal@gmail.com

# Password

# 123

# User clicks

# Login

# Browser sends

# POST

# to

# /login/
# Step 10 : Read login data
# email=request.POST.get("email")

# gets

# payal@gmail.com

# And

# password=request.POST.get("pass")

# gets

# 123
# Step 11 : Compare

# Now

# if email==data["email"] and password==data["password"]:

# Actually compares

# payal@gmail.com

# ==

# payal@gmail.com

# Result

# True

# and

# 123

# ==

# 123

# Result

# True

# Overall

# True AND True

# ↓

# True
# Step 12 : Render Home page

# This line executes

# return render(request,
#               "home.html",
#               {"name":data["name"]})

# Here Django creates a context dictionary

# {
# "name":"Payal"
# }

# and sends it to

# home.html
# Step 13 : Template rendering

# Inside HTML

# <h1>Welcome {{name}}!!!</h1>

# Django looks for

# name

# inside

# {
# "name":"Payal"
# }

# It finds

# Payal

# So HTML becomes

# <h1>Welcome Payal!!!</h1>

# Browser receives

# Welcome Payal!!!
# If login is wrong

# Suppose

# Password

# 456

# Comparison

# 456==123

# ↓

# False

# Then

# msg="Invalid credentials!"

# and

# return render(request,
#               "login.html",
#               {"msg":msg})

# Template

# <h1>{{msg}}</h1>

# becomes

# Invalid credentials!
# Why isn't home() executed after successful login?

# Notice that in your successful login you have:

# return render(request, "home.html", {"name": data["name"]})

# Since you're directly rendering home.html, the home() view is not called.

# The home() view:

# def home(request):
#     return render(request, "home.html")

# is only executed when the browser requests:

# /app1/home/

# For example, if someone manually enters:

# http://127.0.0.1:8000/app1/home/

# or if you write:

# return redirect("/app1/home/")
# Summary
# User opens registration URL
#         │
#         ▼
# show_regi() → GET
#         │
#         ▼
# registration.html
#         │
#         ▼
# User submits form
#         │
#         ▼
# show_regi() → POST
#         │
#         ▼
# Read form data
#         │
#         ▼
# Store in data dictionary
#         │
#         ▼
# redirect("/login/")
#         │
#         ▼
# show_login() → GET
#         │
#         ▼
# login.html
#         │
#         ▼
# User submits login form
#         │
#         ▼
# show_login() → POST
#         │
#         ▼
# Compare email & password
#         │
#    ┌────┴─────┐
#    │          │
# Correct     Wrong
#    │          │
#    ▼          ▼
# render()   login.html
# home.html   + error message
#    │
#    ▼
# Welcome Payal!!!

# This example is good for learning Django views and request flow. In a real application, instead of using the global data dictionary, you would store users in a database and typically use Django's built-in authentication system.