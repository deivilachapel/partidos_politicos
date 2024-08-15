

# Create your models here.
from django.db import models

class Partido(models.Model):
    nombre = models.CharField(max_length=255)
    ideologia = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
