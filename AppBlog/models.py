from django.db import models

# Create your models here.


class Register(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contrasena = models.CharField(max_length=50)
    
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()
    foto = models.ImageField(upload_to='autor_fotos/', blank=True, null=True)