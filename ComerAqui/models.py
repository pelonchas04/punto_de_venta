from django.db import models


class Mesas(models.Model):
    numero_mesa = models.IntegerField(primary_key=True)
    descripcion = models.CharField(blank=True, null=True, max_length=40)
    habilitado = models.BooleanField()

    def Get_numero(self):
        return self.numero_mesa
    
    def Get_descripcion(self):
        return self.descripcion