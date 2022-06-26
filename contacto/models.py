from django.db import models

# Create your models here.
class Consulta(models.Model):
    fechaHora= models.DateTimeField()
    email= models.EmailField()
    contenido= models.CharField(max_length=500)

class ArmaViaje(models.Model):
    fechaHora= models.DateTimeField()
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    pais= models.CharField(max_length=20)
    idioma= models.CharField(max_length=10)
    telefono= models.CharField(max_length=15)
    fechaLlegada= models.DateField()
    fechasFlexibles= models.BooleanField()
    destinos=models.JSONField()
    cantidadNoches= models.IntegerField()
    adultos= models.IntegerField()
    menores= models.IntegerField()
    presupuesto= models.IntegerField()
    nivelAlojamiento= models.CharField(max_length=10)
    vuelosInternacionales= models.BooleanField()
    comentario= models.CharField(max_length=500)