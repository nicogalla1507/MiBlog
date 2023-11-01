from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from .views import*

urlpatterns = [
    path('pagina/',PruebaPagina,name="index"),
    path('home/',inicio,name="inicio"),
    path('acerca/',acercaDeMi,name="about"),
    path('register/', register,name="register"),
    path('editar/',editar_informacion_personal,name="editar"),
    path('mostrar/',mostrar_info,name="mostrar"),
    path('login/',iniciar_sesion,name="login"),
    path('error/',error,name="error"),
    path('logout/',logout_view,name="logout")
]