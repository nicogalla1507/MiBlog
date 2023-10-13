from django import forms
from .models import AcercaDeMi

class RegisterForm(forms.Form):
    usuario = forms.CharField()
    email = forms.EmailField()
    contrasena = forms.CharField()
    

class AutorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    contenido = forms.CharField()