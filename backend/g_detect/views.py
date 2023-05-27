from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def home(request):
    pass

def register(request):
    # 0 for success 1 for fail
    if request.user.is_authenticated():
        pass

    if request.method == "POST":
        data = request.POST

        username = data["username"]
        if username not in [i.username for i in Volunteer.objects.all()]:
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
            
            return 0
    else:
        return 1

def login_user(request):
    if request.user.is_authenticated:
        return 1

    if request.method == "POST":
        data = request.POST

        user = authenticate(request, username=data.get("username"), password=data.get("password"))

        if user is not None:
            login(request, user)
            return 0

        return 1

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return 0

    return 1

def dashboard(request):
    if not request.user.is_authenticated:
        return 1
    
    return 0

def add(request):
    pass

def delete(request):
    pass
