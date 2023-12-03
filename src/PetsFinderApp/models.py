# ./src/PetsFinderApp/models.py

from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique pet instances


class Category(models.Model):
    """Model representing a pet category."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a pet category (e.g. Dogs, Cats, Birds etc.)"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a particular category instance."""
        return reverse('category-detail', args=[str(self.id)])


class Pet(models.Model):
    """Model representing a pet (but not a specific instance of a pet)."""

    # Title of the pet (you may want to adjust this field based on your pet data model)
    name = models.CharField(max_length=200)

    # Foreign Key to the Author model (assuming pets have an 'owner' or some reference)
    owner = models.ForeignKey('Owner', on_delete=models.RESTRICT, null=True)
    # Foreign Key used because a pet can only have one owner, but owners can have multiple pets.
    # Owner as a string rather than an object because it hasn't been declared yet in the file.

    # Brief description of the pet
    description = models.TextField(
        max_length=1000, help_text="Enter a brief description of the pet")

    # Unique identifier for the pet
    microchip_id = models.CharField('Microchip ID', max_length=13,
                                    unique=True,
                                    help_text='13 Character Microchip ID')

    # ManyToManyField used because a pet can belong to multiple categories, and a category can contain multiple pets.
    # Category class has already been defined so we can specify the object above.
    category = models.ManyToManyField(
        Category, help_text="Select a category for this pet")

    # Breed of the pet
    breed = models.CharField(max_length=200)

    @property
    def display_breed(self):
        # Your logic to compute/display the breed in a custom way
        return f"{self.breed} - Custom Display"

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this pet."""
        return reverse('pet-detail', args=[str(self.id)])


class PetInstance(models.Model):
    """Model representing a specific instance of a pet."""

    # Unique ID for the pet instance
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular pet instance")

    # Foreign key to the Pet model
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, null=True)

    # Breed of the pet
    breed = models.CharField(max_length=200)

    # Birth date of the pet
    birth_date = models.DateField(null=True, blank=True)

    # Boolean field representing the availability of the pet
    available = models.BooleanField(default=True)

    # Choices for the availability status of the pet
    PET_STATUS = (
        ('a', 'Available'),
        ('p', 'Pending Adoption'),
        ('r', 'Reserved'),
    )

    # Status field indicating the availability status of the pet
    status = models.CharField(
        max_length=1,
        choices=PET_STATUS,
        blank=True,
        default='a',
        help_text='Pet availability',
    )

    # Meta class for specifying model-specific metadata
    class Meta:
        ordering = ['birth_date']

    # String representation of the model object
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.pet.name})'


class Owner(models.Model):
    """Model representing an owner."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular owner instance."""
        return reverse('owner-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
