from django.contrib import admin

# Register your models here.

from django.contrib import admin
from  .models import * #importamos el archivo models

#registramos los modelos

admin.site.register(Consulta)

admin.site.register(ArmaViaje)