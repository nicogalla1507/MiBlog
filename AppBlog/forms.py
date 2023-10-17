from django import forms
from .models import AcercaDeMi

class RegisterForm(forms.Form):
    usuario = forms.CharField()
    email = forms.EmailField()
    contrasena = forms.CharField()
    

class AutorForm(forms.ModelForm):
    class Meta:
        model = AcercaDeMi
        fields = ['nombre', 'contenido']

class LoginForm(forms.Form):
    usuario= forms.CharField()
    contrasena = forms.CharField()