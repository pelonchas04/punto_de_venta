from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Ingresar_mesa', views.IngresarMesas, name='ingresar_mesas'),
]
