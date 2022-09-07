from email.policy import default
from django.db import models
from datetime import date
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='imgs')

class Propiedad(models.Model):
    nombre = models.CharField(max_length=20, default='Departamento', blank=False, null=False)
    descripcion_corta = models.TextField(max_length=250, blank=True, null=True)
    descripcion = models.TextField(max_length=10000, blank=True, null=True)
    ambientes = models.IntegerField(default=2, blank=False, null=False)
    baños = models.IntegerField(default=1, blank=False, null=False)
    cochera = models.BooleanField(default=False)
    en_alquiler = models.BooleanField(default=True)
    en_venta = models.BooleanField(default=False)
    precio = models.IntegerField(default=0, blank=False, null=False)
    ubicacion = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField(default=date.today)
    imagen1 = models.ImageField(upload_to = 'propiedades', blank=True, null=True)
    imagen2 = models.ImageField(upload_to = 'propiedades', blank=True, null=True)
    imagen3 = models.ImageField(upload_to = 'propiedades', blank=True, null=True)
    imagen4 = models.ImageField(upload_to = 'propiedades', blank=True, null=True)
    mapa = models.URLField(help_text="https://www.google.com/maps/embed/v1/place?key=APIKEY-IxI&q=", blank=True, null=True)

    def __str__(self):
        return self.nombre