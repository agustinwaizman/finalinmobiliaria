from django.shortcuts import render
from .models import Propiedad

def view(request, id):
    propiedad = Propiedad.objects.get(id=id)
    context = {
        'propiedad':propiedad
    }
    return render(request, 'propiedades/detail.html', context)
