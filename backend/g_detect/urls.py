from django.urls import path
from . import views

app_name = 'g_detect'

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("add", views.add, name="add"),
    path("delete", views.delete, name="delete"),
]
