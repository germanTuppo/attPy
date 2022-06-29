from django.urls import path
from paquetes import views

urlpatterns = [   
    path('', views.paquetes, name="paquetes"), #esta seria la vista del inicio (index.html o home)
    path('destinos/', views.destinos, name="destinos"),
]
