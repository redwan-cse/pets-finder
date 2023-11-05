from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from pets.models import Pet


class PetsListView(ListView):
    model = Pet
    
class PetCreateView(CreateView):
    model = Pet
    fields = ["author", "title", "color", "place", "description", "created_date", "published_date"]