from django.shortcuts import render
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required # obligamos al usuario a iniciar secion para poder entrar a la siguiente vista
def index(request):
    return render(request, 'index.html')

