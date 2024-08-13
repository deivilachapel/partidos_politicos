from django.db import models

# Create your models here.

class Partido(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    fecha_fundacion = models.DateField()

    def __str__(self):
        return self.nombre
