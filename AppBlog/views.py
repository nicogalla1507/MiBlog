from django.shortcuts import render, redirect
from .forms import RegisterForm, AutorForm
from .models import Register, AcercaDeMi

# Create your views here.

def PruebaPagina(request):
    return render(request,"AppBlog/base.html")

def inicio(request):
    return render(request, "AppBlog/inicio.html")

def acercaDeMi(request):
    return render(request,"AppBlog/acerca_mi.html")

def probandoNotebook(request):
    return "hola"

def register(request):
    if request.method == "POST":
        mi_formulario = RegisterForm(request.POST)
        
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            reg = Register(usuario=info["usuario"],email=info["email"],contrasena=info["contrasena"])
            reg.save()
            return render(request,"AppBlog/inicio_register.html")
    else:
        mi_formulario = RegisterForm()
    
    return render(request, "AppBlog/register_form.html",{"mi_formulario":mi_formulario})


def editar_informacion_personal(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            contexto = AcercaDeMi(nombre=info["nombre"], contenido=info["contenido"])
            contexto.save()
            return redirect('about') 
    else:
        form = AutorForm()
    return render(request, 'AppBlog/agregar_info.html', {'form': form})