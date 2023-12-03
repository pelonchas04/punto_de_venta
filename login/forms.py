from django import forms # importamos forms para poder iniciar el formulario

class LoginForms(forms.Form):
    # Declaramos las variables que tendrá el formulario, así como tambien el tipo password 
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)