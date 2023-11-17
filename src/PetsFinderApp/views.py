from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "PetsFinderApp/index.html", {})


def pets(request):
    return render(request, "PetsFinderApp/pets.html", {})


def register(request):
    return render(request, "PetsFinderApp/register.html", {})


def login(request):
    return render(request, "PetsFinderApp/login.html", {})


def logout(request):
    pass


def password_reset(request):
    return render(request, "PetsFinderApp/password_reset.html", {})
