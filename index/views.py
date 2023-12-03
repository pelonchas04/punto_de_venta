from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

# def index(request): 
#         if request.GET['usuario'] and request.GET['contraseña']

@login_required # obligamos al usuario a iniciar secion para poder entrar a la siguiente vista
def index(request):
    return render(request, 'index.html')

