from django.conf import settings
from django.db import models
from django.utils import timezone

class Pet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(verbose_name="Color")  # Set the verbose_name attribute
    text = models.TextField(verbose_name="Place ")  # Set the verbose_name attribute
    description = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return f"/pets/{self.id}/"

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title