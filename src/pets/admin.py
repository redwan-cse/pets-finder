from django.contrib import admin
from .models import Pet

admin.site.register(Pet)

admin.site.site_header = "Pet Finders Admin Panel"
admin.site.site_title = "Pet Finders Admin Panel"