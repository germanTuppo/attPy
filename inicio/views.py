from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

# Create your views here.
def inicio(request):

      return render(request, "inicio/inicio.html")
