from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import GarbageSerializer

# Create your views here.
def home(request):
    pass # Landing page

def register(request):
    # 0 for success 1 for fail
    if request.user.is_authenticated:
        return render(request, "dashboard/dash.html") # Dashboard

    if request.method == "POST":
        data = request.POST

        # Checking password validity
        if (data.get('password') != data.get('re_password')):
            print("No match", data.get('password'), data.get('re_password'))
            return render(request, "Signup_page/Signup.html")

        username = data["username"]
        if username not in [i.username for i in User.objects.all()]:
            user = User.objects.create_user(
                    username=username,
                    password=data.get("password"),
                    email=data.get("email"),
                    first_name=data.get("firstname"),
                    last_name=data.get("lastname")
                )
            user.save()
            Volunteer(user=user, location=data.get("location"), phone=data.get("phone")).save()
            login(request, user)
            
            return render(request, "dashboard/dash.html") # Dashboard
    else:
        return render(request, "Signup_page/Signup.html")

def login_user(request):
    if request.user.is_authenticated:
        return render(request, "dashboard/dash.html") # Dashboard

    if request.method == "POST":
        data = request.POST
        
        user = authenticate(request, username=data["username"], password=data["password"])

        if user is not None:
            login(request, user)
            return render(request, "dashboard/dash.html")
        
        return render(request, "Login_page/Login.html")

    return render(request, "Login_page/Login.html")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return 0 # Landing Page

    return 1 # Landing page

def dashboard(request):
    if not request.user.is_authenticated:
        return 1 # Dashboard
    
    return render(request, "Login_page/Login.html")

@csrf_exempt
def add(request):
    if request.method == "POST":
        print(request)
        data = JSONParser().parse(request)
        serializer = GarbageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def delete(request, pk):
    try:
        garbage = Garbage.objects.get(id_number=pk)
    except GarbageDoesNotExist:
        return HttpResponse(status=404)

    if request.method == "DELETE":
        garbage.delete()
        return HttpResponse(status=204)
