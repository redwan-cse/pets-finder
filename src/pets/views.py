from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from pets.models import Pet


class PetsListView(ListView):
    model = Pet
    
class PetCreateView(CreateView):
    model = Pet
    fields = ["author", "title", "text", "text", "description", "created_date", "published_date"]