from typing import List
from django.http.request import QueryDict #ver
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
#from AppCoder.models import Curso, Profesor #Import models
#from AppCoder.forms import CursoFormulario, ProfesorFormulario #Import Forms

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def contacto(request):

      return render(request, "contacto/contacto.html")


def arma(request):

      return render(request, "contacto/arma.html")