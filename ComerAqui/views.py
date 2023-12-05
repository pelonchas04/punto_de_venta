from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ComerAqui import models



@login_required
def Mesas(request):
    cantidad_mesas = models.Mesas.objects.filter()
    return render(request, 'Mesas.html', {'MesasTotales': cantidad_mesas})

@login_required
def ElegirBebidadComidas(request):
    return HttpResponse("Elejir comida o bebida")