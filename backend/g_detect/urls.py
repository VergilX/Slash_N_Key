from django.urls import path
from . import views

app_name = 'g_detect'

urlpatterns = [
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login_user", views.login, name="login_user"),
    path("logout_user", views.login, name="logout_user"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("add", views.add, name="add"),
    path("delete", views.delete, name="delete"),
]
