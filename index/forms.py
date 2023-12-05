from django import forms
from ComerAqui.models import Mesas

class IngresoMesas(forms.ModelForm):
    class Meta:
        model = Mesas
        fields = ["numero_mesa", "descripcion"]
    def verificacion(self):
        data = self.cleaned_data['numero_mesa']
        if Mesas.objects.filter(numero_mesas = data).exists():
            raise forms.ValidationError("Este número de mesa ya esta asignado.")
        return data