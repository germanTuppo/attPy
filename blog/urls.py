from django.urls import path
from blog import views


urlpatterns = [
   
    path('', views.blog, name="blog"), #esta sería la vista blog
    path('usuarioFormulario/', views.usuarioFormulario, name="usuarioFormulario"),
    path('buscar/', views.buscar),
]
