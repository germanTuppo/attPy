from django import forms


class ConsultaFormulario(forms.Form):

    #Especificar los campos
    fechaHora= forms.DateTimeField()
    email= forms.EmailField()
    contenido= forms.CharField(max_length=500)


class ArmaViaje(forms.Form):
    fechaHora= forms.DateTimeField()
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()
    pais= forms.CharField(max_length=20)
    idioma= forms.CharField(max_length=10)
    telefono= forms.CharField(max_length=15)
    fechaLlegada= forms.DateField()
    fechasFlexibles= forms.BooleanField()
    destinos=forms.JSONField()
    cantidadNoches= forms.IntegerField()
    adultos= forms.IntegerField()
    menores= forms.IntegerField()
    presupuesto= forms.IntegerField()
    nivelAlojamiento= forms.CharField(max_length=10)
    vuelosInternacionales= forms.BooleanField()
    comentario= forms.CharField(max_length=500)