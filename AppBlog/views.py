from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import RegisterForm, AutorForm, LoginForm
from .models import Register, AcercaDeMi

# Create your views here.

def PruebaPagina(request):
    return render(request,"AppBlog/base.html")

def inicio(request):
    return render(request, "AppBlog/inicio.html")

def acercaDeMi(request):
    return render(request,"AppBlog/acerca_mi.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():             #una funcion para que el usuario se registre y pueda agregar informacion a la base de datos y mostrarla por la pagina 
            info = form.cleaned_data
            instancia = Register(usuario = info['usuario'],email = info['email'], contrasena = info['contrasena'])
            instancia.save()
            
            return HttpResponseRedirect("AppBlog/inicio_register.html")  
    else:
        form = RegisterForm()
    return render(request, "AppBlog/register_form.html", {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['contrasena']

            try:
                user = Register.objects.get(usuario=username, contrasena=password)
                # Si se encuentra un usuario con las credenciales, el usuario es válido
                # Puedes realizar la acción de inicio de sesión aquí

                return render(request,'AppBlog/inicio_login.html')  # Reemplaza 'inicio' con la URL de tu página de inicio
            except Register.DoesNotExist:
                return render(request, 'AppBlog/error.html')

    # Si la solicitud no es un POST o el formulario no es válido, muestra el formulario de inicio de sesión
    else:
        form = LoginForm()

    return render(request, 'AppBlog/login.html', {'formulario': form})

                   
def editar_informacion_personal(request):
    if request.method == 'POST':
        form1 = AutorForm(request.POST)
        if form1.is_valid():
            info= form1.cleaned_data
            instancia = AcercaDeMi(nombre=info['nombre'],contenido=info['contenido'])
            instancia.save()
        
            return render(request,"AppBlog/inicio_login.html")
        print("se ejecuto la pagina acerca de mi")
    else:
        form1 = AutorForm()
    
    return render(request,"AppBlog/agregar_info.html",{"form1":form1})


def mostrar_info(request):
    publicacion = AcercaDeMi.objects.all()
    
    return render(request, "AppBlog/mostrar.html",{"publicacion":publicacion})