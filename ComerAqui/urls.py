from django.urls import path
from . import views

urlpatterns = [
    path('Cantidad de mesas/', views.Mesas, name='Cantidad_de_mesas')
]
