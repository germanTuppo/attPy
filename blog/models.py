from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    pais= models.CharField(max_length=20)
    deseaInfo= models.BooleanField()
    idioma= models.CharField(max_length=2)
    fechaRegistro= models.DateTimeField()
    avatar=models.CharField(max_length=50)

class Comentario(models.Model):
    usuarioId= models.IntegerField()
    fechaHora= models.DateTimeField()
    contenido= models.CharField(max_length=500)