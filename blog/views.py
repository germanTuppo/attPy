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

                  return render(request, "blog/blog.html") #Vuelvo al inicio o a donde quieran

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