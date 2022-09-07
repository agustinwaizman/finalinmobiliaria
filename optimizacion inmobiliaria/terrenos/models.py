from django.db import models
from datetime import date

class Terreno(models.Model):
    nombre= models.CharField(max_length=20, blank=False, null=False, default='Terreno')
    descripcion_corta = models.TextField(max_length=250, blank=True, null=True)
    descripcion= models.TextField(max_length=500, blank=True, null=True)
    ubicacion= models.CharField(default= 'Resistencia, Chaco', max_length=20, blank=False, null=False)
    mtscuadrados= models.IntegerField(default=0, blank=False, null=False)
    precio= models.IntegerField(default=0, blank=False, null=False)
    fecha= models.DateField(default=date.today)
    mapa = models.URLField(help_text="https://www.google.com/maps/embed/v1/place?key=APIKEY-IxI&q=", blank=True, null=True)
    
    def __str__(self):
        return self.nombre