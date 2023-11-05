
#cloud_journey/src/App/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [path("admin/", admin.site.urls), path("pets/", include("pets.urls"))]