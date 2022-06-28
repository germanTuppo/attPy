from django.urls import path
from inicio import views


urlpatterns = [
   
    path('', views.inicio, name="inicio"), #esta seria la vista del inicio (index.html o home)

]
