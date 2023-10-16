from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .forms import RegisterForm, AutorForm
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("AppBlog/inicio_register.html")  # Asegúrate de que la URL esté configurada correctamente
    else:
        form = UserCreationForm()
    return render(request, "AppBlog/register_form.html", {'form': form})


def editar_informacion_personal(request):
    if request.method == 'POST':
        form1 = AutorForm(request.POST)
        if form1.is_valid():
            info= form1.cleaned_data
            instancia = AcercaDeMi(nombre=info['nombre'],contenido=info['contenido'])
            instancia.save()
        
            return render(request,"AppBlog/acerca_mi.html")
        print("se ejecuto la pagina acerca de mi")
    else:
        form1 = AutorForm()
    
    return render(request,"AppBlog/agregar_info.html",{"form1":form1})


def mostrar_info(request):
    publicacion = AcercaDeMi.objects.all()
    
    return render(request, "AppBlog/mostrar.html",{"publicacion":publicacion})