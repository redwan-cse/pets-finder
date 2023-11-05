from django.urls import path
from pets.views import PetsListView, PetCreateView
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path("all/", PetsListView.as_view(), name="pet_list"),
    path("add/", PetCreateView.as_view(), name="pet_form"),
]