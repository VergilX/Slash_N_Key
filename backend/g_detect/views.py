from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def home(request):
    pass # Landing page

def register(request):
    # 0 for success 1 for fail
    if request.user.is_authenticated:
        pass # Dashboard

    if request.method == "POST":
        data = request.POST

        # Checking password validity
        if (data.get('password') != data.get('re-password')):
            return render(request, "Signup_page/Signup.html")

        username = data["username"]
        if username not in [i.username for i in User.objects.all()]:
            user = User.objects.create_user(
                    username=username,
                    password=data.get("password"),
                    email=data.get("email"),
                    phone=data.get("phone"),
                    first_name=data.get("firstname"),
                    last_name=data.get("lastname")
                )
            user.save()
            login(request, user)
            Volunteer(user=user, location=data.get("location")).save()
            
            return 0 # Dashboard
    else:
        return render(request, "Signup_page/Signup.html")

def login_user(request):
    if request.user.is_authenticated:
        return render(request, "Login_page/Login.html")

    if request.method == "POST":
        data = request.POST

        user = authenticate(request, username=data.get("username"), password=data.get("password"))

        if user is not None:
            login(request, user)
            return 0 # Dashboard

        return render(request, "Login_page/Login.html")

    return render(request, "Login_page/Login.html")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return 0 # Dashboard

    return 1 # Landing page

def dashboard(request):
    if not request.user.is_authenticated:
        return 1 # Dashboard
    
    return render(request, "Login_page/Login.html")

def add(request):
    pass

def delete(request):
    pass
