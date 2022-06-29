from django import forms


class UsuarioFormulario(forms.Form):

    #Especificar los campos
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()
    pais= forms.CharField(max_length=20)
    deseaInfo= forms.BooleanField()
    idioma= forms.CharField(max_length=2)
    fechaRegistro= forms.DateTimeField()
    avatar=forms.CharField(max_length=50)

class ComentarioFormulario(forms.Form):
    usuarioId= forms.IntegerField()
    fechaHora= forms.DateTimeField()
    contenido= forms.CharField(max_length=500)