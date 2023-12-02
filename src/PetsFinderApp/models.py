# from django.db import models

from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.Charfield(max_langth=200)
    roll = models.Charfield(max_langth=10)


    def_str_(self):
            return self.name