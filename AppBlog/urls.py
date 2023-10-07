from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('pagina/',PruebaPagina,name="index"),
    path('inicio/',inicio,name="inicio"),
    path('acerca/',acercaDeMi,name="about")
]
