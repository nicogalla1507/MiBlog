from django import forms
from .models import Autor

class RegisterForm(forms.Form):
    usuario = forms.CharField()
    email = forms.EmailField()
    contrasena = forms.CharField()
    

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'biografia', 'foto']