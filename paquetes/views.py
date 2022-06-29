from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse


def paquetes(request):

      return render(request, "paquetes/paquetes.html")


def destinos(request):

      return render(request, "paquetes/destinos.html")

