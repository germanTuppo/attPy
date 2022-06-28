from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
#from AppCoder.models import Curso, Profesor #Import models
#from AppCoder.forms import CursoFormulario, ProfesorFormulario #Import Forms

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def inicio(request):

      return render(request, "blog/inicio.html")


def blog(request):

      return render(request, "blog/blog.html")