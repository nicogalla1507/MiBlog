from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import AutorForm
from .models import AcercaDeMi

# Create your views here.

def PruebaPagina(request):
    return render(request,"AppBlog/base.html")


def inicio(request):
    return render(request, "AppBlog/inicio.html")

@login_required
def acercaDeMi(request):
    return render(request,"AppBlog/acerca_mi.html")

def error(request):
    return render(request,"AppBlog/error.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():             
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppBlog/inicio_register.html")
             
    else:
        form = UserCreationForm()
    return render(request, "AppBlog/register_form.html", {'form': form})


def iniciar_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, request.POST)

        if formulario.is_valid():
            usuario = request.POST.get('username')
            contrasena = request.POST.get('password')

            user = authenticate(username=usuario, password=contrasena)
            if user is not None:
                login(request, user)
                return render(request, "AppBlog/inicio_login.html")
            else:
                return redirect('error')
        else:

            print(formulario.errors)

    formulario = AuthenticationForm()
    return render(request, "AppBlog/login.html", {"formulario": formulario})

def logout_view(request):
    logout(request)
    return redirect('inicio')

def editar_informacion_personal(request):
    if request.method == 'POST':
        form1 = AutorForm(request.POST)
        if form1.is_valid():
            info= form1.cleaned_data
            instancia = AcercaDeMi(autor=info['autor'],titulo= info['titulo'],subtitulo=info['subtitulo'],contenido=info['contenido'], fecha=info['fecha'])
            instancia.save()
        
            return render(request,"AppBlog/inicio_login.html")
        print("se ejecuto la pagina acerca de mi")
    else:
        form1 = AutorForm()
    
    return render(request,"AppBlog/agregar_info.html",{"form1":form1})

def mostrar_info(request):
    publicacion = AcercaDeMi.objects.all()
    
    return render(request, "AppBlog/mostrar.html",{"publicacion":publicacion})


    
    