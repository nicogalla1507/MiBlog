from django import forms

class RegisterForm(forms.Form):
    usuario = forms.CharField()
    email = forms.EmailField()
    contrasena = forms.CharField()