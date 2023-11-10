from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("password_reset/", views.password_reset, name="password_reset"),
]
