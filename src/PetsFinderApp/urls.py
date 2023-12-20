from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("petDetails/", views.petDetails, name="petDetails"),
    path("register/", views.register, name="register"),
    path("pets/", views.pets, name="pets"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("password_reset/", views.password_reset, name="password_reset"),
]
