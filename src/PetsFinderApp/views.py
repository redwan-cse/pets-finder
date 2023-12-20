# /src/PetsFinderApp/views.py

from django.shortcuts import render, get_object_or_404
from .models import Pet, PetInstance, Owner  # We can use , Category as well if we want to display the category in the views.


# Create your views here.
def home(request):
    """View function to display the home page."""
    context = {}
    return render(request, "PetsFinderApp/index.html", context=context)

def petDetails(request):
    """View function to display a list of pets."""
    context = {}
    return render(request, "PetsFinderApp/petDetails.html", context=context)



def pets(request):
    """View function to display a list of pets."""
    context = {}
    return render(request, "PetsFinderApp/pets.html", context=context)


def register(request):
    """View function to display a registration form."""
    context = {}
    return render(request, "PetsFinderApp/register.html", context=context)


def login(request):
    """View function to display a login form."""
    context = {}
    return render(request, "PetsFinderApp/login.html", context=context)


def logout(request):
    """View function to logout a user."""
    pass


def password_reset(request):
    """View function to display a password reset form."""
    context = {}
    return render(request, "PetsFinderApp/password_reset.html", context=context)


# The following views are for the Pet, PetInstance, and Owner models.
def pet_list(request):
    """View function to display a list of pets."""
    pets = Pet.objects.all()
    return render(request, 'pet_list.html', {'pets': pets})


def pet_detail(request, pet_id):
    """View function to display details of a specific pet."""
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'pet_detail.html', {'pet': pet})


def petinstance_list(request):
    """View function to display a list of pet instances."""
    pet_instances = PetInstance.objects.all()
    return render(request, 'petinstance_list.html', {'pet_instances': pet_instances})


def petinstance_detail(request, petinstance_id):
    """View function to display details of a specific pet instance."""
    pet_instance = get_object_or_404(PetInstance, id=petinstance_id)
    return render(request, 'petinstance_detail.html', {'pet_instance': pet_instance})


def owner_list(request):
    """View function to display a list of owners."""
    owners = Owner.objects.all()
    return render(request, 'owner_list.html', {'owners': owners})


def owner_detail(request, owner_id):
    """View function to display details of a specific owner."""
    owner = get_object_or_404(Owner, id=owner_id)
    return render(request, 'owner_detail.html', {'owner': owner})
