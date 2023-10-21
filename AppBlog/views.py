from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views import View
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
        if form.is_valid():
            info = form.cleaned_data
            instancia = Register(usuario = info['usuario'],email = info['email'], contrasena = info['contrasena'])
            instancia.save()
            
            return render("AppBlog/inicio_register.html")  
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


                return render(request,'AppBlog/inicio_login.html')  
            except Register.DoesNotExist:
                return render(request, 'AppBlog/error.html')

    
    else:
        form = LoginForm()

    return render(request, 'AppBlog/login.html', {'formulario': form})

                   
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


class Eliminar(View):
    def obtener(self,request,id):
        try:
            objeto_eliminar = AcercaDeMi.objects.get(pk=id)
            texto = "NO EXISTE ESTE OBJETO|VOLVER AL INICIO"
        except AcercaDeMi.DoesNotExist:
            return render(request,"AppBlog/objeto_inexistente.html",{"texto":texto})
        
        else:
            return render(request,"AppBlog/eliminar_info.html")
        
    def post(self, request, id):
        objeto_eliminar = AcercaDeMi.objects.get(pk=id)
        
        objeto_eliminar.delete()
        
        return redirect('mostrar')
    
    