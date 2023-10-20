from django import forms

class RegisterForm(forms.Form):
    usuario = forms.CharField()
    email = forms.EmailField()
    contrasena = forms.CharField()
    

class AutorForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=70)
    fecha = forms.DateField()
    contenido = forms.CharField(widget=forms.TextInput())
    
    
class LoginForm(forms.Form):
    usuario= forms.CharField()
    contrasena = forms.CharField(widget=forms.PasswordInput())