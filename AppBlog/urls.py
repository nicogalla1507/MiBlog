from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('pagina/',PruebaPagina,name="index"),
    path('inicio/',inicio,name="inicio"),
    path('acerca/',acercaDeMi,name="about"),
    path('register/', register,name="register"),
    path('editar/',editar_informacion_personal,name="editar"),
    path('mostrar/',mostrar_info,name="mostrar"),
    path('login/',login,name="login"),
    path('error/',login,name='error'),
    path('eliminar/<int:id>/',Eliminar.as_view(), name='eliminar'),
]
