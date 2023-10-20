from django.db import models

# Create your models here.


class Register(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contrasena = models.CharField(max_length=50)
    
    
class AcercaDeMi(models.Model):
    tiutlo = models.CharField(max_length=40,null=True)
    subtitulo = models.CharField(max_length=60,null=True)
    autor = models.CharField(max_length=60,null=True)
    fecha = models.DateField(null=True)
    contenido = models.TextField(null=True)