from django.shortcuts import render
from .models import Terreno

def view(request, id):
    terreno = Terreno.objects.get(id=id)
    context = {
        'terreno':terreno
    }
    return render(request, 'terrenos/detail.html', context)