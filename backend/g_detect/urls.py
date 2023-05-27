from django.urls import path
from . import views

app_name = 'g_detect'

urlpatterns = [
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("add", views.add, name="add"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
