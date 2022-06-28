from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

# Create your views here.
def paquetes(request):

      return render(request, "paquetes/paquetes.html")


def destinos(request):

      return render(request, "paquetes/destinos.html")

