from django import forms
from ComerAqui.models import Mesas

class IngresoMesas(forms.ModelForm):
    class Meta:
        model = Mesas
        fields = ["numero_mesa", "descripcion", "habilitado"]