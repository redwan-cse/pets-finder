from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("petdetails/", views.petdetails, name="petdetails"),
    path("pets/", views.pets, name="pets"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("password_reset/", views.password_reset, name="password_reset"),
]
