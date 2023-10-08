from django.shortcuts import render
from .forms import RegisterForm
from .models import Register

# Create your views here.

def PruebaPagina(request):
    return render(request,"AppBlog/base.html")

def inicio(request):
    return render(request, "AppBlog/inicio.html")

def acercaDeMi(request):
    return render(request,"AppBlog/acerca_mi.html")

def register(request):
    if request.method == "POST":
        mi_formulario = RegisterForm(request.POST)
        
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            reg = Register(usuario=info["usuario"],email=info["email"],contrasena=info["contrasena"])
            reg.save()
            return render(request,"AppBlog/inicio.html")
    else:
        mi_formulario = RegisterForm()
    
    return render(request, "AppBlog/register_form.html",{"mi_formulario":mi_formulario})
