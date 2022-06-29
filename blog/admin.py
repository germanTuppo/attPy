from django.contrib import admin
from  .models import * #importamos el archivo models

#registramos los modelos

admin.site.register(Usuario)

admin.site.register(Comentario)
