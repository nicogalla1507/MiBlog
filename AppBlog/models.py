from django.db import models

# Create your models here.


class Register(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contrasena = models.CharField(max_length=50)
    
    
class AcercaDeMi(models.Model):
    titulo = models.CharField(max_length=40,null=False)
    subtitulo = models.CharField(max_length=60,null=False)
    autor = models.CharField(max_length=60,null=False)
    fecha = models.DateField(null=False)
    contenido = models.TextField(null=False)