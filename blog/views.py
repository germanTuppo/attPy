from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from blog.models import Usuario, Comentario #Import models
from blog.forms import UsuarioFormulario, ComentarioFormulario #Import Forms

#esto aun no lo estoy usando
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


import datetime


def blog(request):
      return render(request, "blog/blog.html")



#crud usuarios
def leerUsuarios(request):
      usuarios = Usuario.objects.all()
      contexto = {"usuarios":usuarios}
      return render(request, "blog/leerUsuarios.html", contexto)


def usuarioFormulario(request):

      if request.method == 'POST':

            miFormulario = UsuarioFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  print(informacion)
                  usuario = Usuario (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], pais=informacion['pais'], deseaInfo=informacion['deseaInfo'], idioma=informacion['idioma'], fechaRegistro=datetime.datetime.now(), avatar=informacion['avatar']) 

                  #a ver si mete algo por default , fechaRegistro=informacion['fechaRegistro'], avatar=informacion['avatar']
                  #aca tengo problemas con la fecha, por hacerme el canchero me pasa
                  usuario.save()

                  return render(request, "blog/blog.html") #Vuelvo al inicio de blog

      else: 

            miFormulario= UsuarioFormulario() #Formulario vacio para construir el html

      return render(request, "blog/usuarioFormulario.html", {"miFormulario":miFormulario})


def buscar(request):

      if  request.GET["email"]: #if request.method == 'Get':

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            email = request.GET['email'] 
            print(email)
            usuarios = Usuario.objects.filter(email__icontains=email)
            print(usuarios)
            return render(request, "blog/blog.html", {"usuarios":usuarios, "email":email})

      else: 

	      respuesta = "No enviaste datos"

      return render(request, "blog/blog.html", {"respuesta":respuesta})
      #me altera este error (funciona, por eso me altera mas aún...)


def eliminarUsuario(request, usuarioNombre):

      usuario= Usuario.objects.get(nombre=usuarioNombre)
      usuario.delete()
      
      #vuelvo al menú
      usuarios = Usuario.objects.all() #trae todos los usuarios

      contexto= {"usuarios":usuarios} 

      return render(request, "blog/blog.html",contexto)


def editarUsuario(request, usuarioNombre):

      #Recibe el nombre del profesor que vamos a modificar
      usuario = Usuario.objects.get(nombre=usuarioNombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = UsuarioFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  usuario.nombre = informacion['nombre']
                  usuario.apellido = informacion['apellido']
                  usuario.email = informacion['email']
                  usuario.pais = informacion['pais']
                  usuario.deseaInfo = informacion['deseaInfo']
                  usuario.idioma = informacion['idioma']
                  usuario.fechaRegistro = informacion['fechaRegistro']
                  usuario.pais = informacion['pais']
                  usuario.avatar = informacion['avatar']

                  Usuario.save()

                  return render(request, "blog/blog.html") 
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UsuarioFormulario(initial={'nombre': usuario.nombre, 'apellido':usuario.apellido, 'email':usuario.email, 'pais':usuario.pais, 'deseaInfo': usuario.deseaInfo, 'idioma': usuario.idioma, 'fechaRegistro': usuario.fechaRegistro, 'pais': usuario.pais, 'avatar': usuario.avatar}) 

      #Voy al html que me permite editar
      return render(request, "blog/editarUsuario.html", {"miFormulario":miFormulario, "usuarioNombre":usuarioNombre})