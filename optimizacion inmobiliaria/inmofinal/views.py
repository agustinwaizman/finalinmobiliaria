from django.shortcuts import render
from propiedades.models import Propiedad
from terrenos.models import Terreno
from django.db.models import Q


def ventas(request):
    propiedades = Propiedad.objects.filter(en_venta = True)
    terrenos = Terreno.objects.all()
    context = {
        'propiedades':propiedades,
        'terrenos':terrenos
    }
    return render(request, 'ventas.html', context)

def alquileres(request):
    propiedades = Propiedad.objects.filter(en_alquiler = True)
    context = {'propiedades':propiedades}
    return render(request, 'alquileres.html', context)

def index(request):
    queryset = request.GET.get("buscar")
    propiedades = Propiedad.objects.all()
    terrenos = Terreno.objects.all()
    if queryset:
        propiedades = Propiedad.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct
        terrenos = Terreno.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct

    context = {
        'propiedades':propiedades,
        'terrenos':terrenos,
    }
    return render(request, 'index.html', context)