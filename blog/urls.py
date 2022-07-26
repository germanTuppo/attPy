from django.urls import path
from blog import views


urlpatterns = [
   
    path('', views.blog, name="blog"), #esta sería la vista blog
    path('usuarioFormulario/', views.usuarioFormulario, name="usuarioFormulario"),
    path('buscar/', views.buscar),
    path('leerUsuarios/', views.leerUsuarios, name="leerUsuarios"),
    path('eliminarUsuario//<usuarioNombre>/', views.eliminarUsuario, name="eliminarUsuario"),
    path('editarUsuario//<usuarioNombre>/', views.editarUsuario, name="editarUsuario"),


]
