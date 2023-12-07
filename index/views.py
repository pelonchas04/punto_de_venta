from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from index.forms import IngresoMesas

@login_required # obligamos al usuario a iniciar secion para poder entrar a la siguiente vista
def index(request):
    return render(request, 'index.html')

@login_required
def IngresarMesas(request):
    if request.method == 'POST':
        nueva = IngresoMesas(request.POST)
        if nueva.is_valid():
            nueva.save()
            return render(request, 'Mesa_ingresada.html', {'formulario_mesa': nueva})
    else:
        nueva = IngresoMesas()
    return render(request, 'Ingresar_mesa.html', {'formulario_mesa': nueva})

@login_required
def ModificarMesa(request):
    return HttpResponse("Modificador de contraseñas")
