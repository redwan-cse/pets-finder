# ./src/PetsFinderApp/admin.py

from django.contrib import admin
from .models import Category, Pet, PetInstance, Owner


# Register the Admin class for Category using the decorator
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# Register the Admin class for Pet using the decorator
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'description', 'microchip_id', 'display_breed')
    search_fields = ('name', 'owner__last_name', 'owner__first_name', 'microchip_id', 'breed')
    list_filter = ('category', 'owner')
    ordering = ('name', 'category', 'owner')


# Register the Admin class for PetInstance using the decorator
@admin.register(PetInstance)
class PetInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet', 'breed', 'birth_date', 'status', 'available')
    search_fields = ('id', 'pet__name', 'breed')
    list_filter = ('status', 'available')
    ordering = ('birth_date',)

    fieldsets = (
        (None, {
            'fields': ('pet', 'breed', 'birth_date')
        }),
        ('Availability', {
            'fields': ('status', 'available')
        }),
    )


# Register the Admin class for Owner using the decorator
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    search_fields = ('last_name', 'first_name')
    ordering = ('last_name',)

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'date_of_birth')
        }),
    )
