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
    query = request.GET.get('q')
    resultados = []

    if query:
        resultados = AcercaDeMi.objects.filter(titulo__iexact=query)
    
    return render(request, 'AppBlog/inicio.html', {'resultados': resultados, 'query': query})
    
    

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

@login_required
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

@login_required
def mostrar_info(request):
    publicacion = AcercaDeMi.objects.all()
    
    return render(request, "AppBlog/mostrar.html",{"publicacion":publicacion})


def eliminar_info(request, nombre_id):
    try:
        elemento = AcercaDeMi.objects.get(id=nombre_id)
    except AcercaDeMi.DoesNotExist:
        
        elemento = None

    if elemento is not None:
        elemento.delete()

    elementos = AcercaDeMi.objects.all()
    contexto = {"elemento": elementos}
    return render(request, "AppBlog/mostrar.html", contexto)

@login_required
def editar_crud(request, publicacion_id):
    publicaciones = AcercaDeMi.objects.get(id=publicacion_id)

    if request.method == "POST":
        formulario = AutorForm(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            publicaciones.titulo = info["titulo"]
            publicaciones.subtitulo = info["subtitulo"]
            publicaciones.autor = info["autor"]
            publicaciones.fecha = info["fecha"]
            publicaciones.contenido = info["contenido"]

            publicaciones.save()

            return render(request, "AppBlog/inicio_login.html")
    else:
        formulario = AutorForm(initial={
            'titulo': publicaciones.titulo,
            'subtitulo': publicaciones.subtitulo,
            'autor': publicaciones.autor,
            'fecha': publicaciones.fecha,
            'contenido': publicaciones.contenido
        })

    return render(request, "AppBlog/CRUD_editar.html", {"form3": formulario})
            
          

    