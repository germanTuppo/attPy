"# attPy"
https://github.com/germanTuppo/attPy.git

En este caso, mi intencion es comenzar un nuevo proyecto, para dejar el anterior ("miProyectoPy") como zona de pruebas, algo donde probar cosas para poder romper todo, pero tener un proyecto mas serio para poder trabajarlo tanto en esta preentrega como en la entrega del proyecto final (y despues, ya que este proyecto es algo real, en el que empece a trabajar con html y css y javascript, y es mi intención mirarlo a django para poder hacer uso de las bases de datos)

Crear proyecto:
    django-admin startproject miProyectoPy

Creando las Apps:
    python manage.py startapp blog
    python manage.py startapp contacto
    python manage.py startapp paquetes
(de momento 3 apps, que es lo que mas siento que usa todas las ventajas de python)



Crear modelos e insertar la aplicacion en settings python manage.py makemigrations (con esto se crea base de datos, vacia de momento.)

MODELOS:


    Modelos de la app blog:

        class Usuario(models.Model):
            nombre= models.CharField(max_length=40)
            apellido= models.CharField(max_length=40)
            email= models.EmailField()
            pais= models.CharField(max_length=20)
            deseaInfo= models.BooleanField
            idioma= models.CharField(max_length=2)
            fechaRegistro= models.DateTimeField
            avatar=models.ImageField

        class Comentario(models.Model):
            usuarioId= models.IntegerField
            fechaHora= models.DateTimeField
            contenido= models.CharField(max_length=500)
        

    Modelos de la app CONTACTO:

        class Consulta(models.Model):
            fechaHora= models.DateTimeField
            email= models.EmailField()
            contenido= models.CharField(max_length=500)

    class ArmaViaje(models.Model):
        fechaHora= models.DateTimeField
        nombre= models.CharField(max_length=40)
        apellido= models.CharField(max_length=40)
        email= models.EmailField()
        pais= models.CharField(max_length=20)
        idioma= models.CharField(max_length=10)
        telefono= models.CharField(max_length=15)
        fechaLlegada= models.DateField
        fechasFlexibles= models.BooleanField
        destinos=models.JSONField
        cantidadNoches= models.IntegerField
        adultos= models.IntegerField
        menores= models.IntegerField
        presupuesto= models.IntegerField
        nivelAlojamiento= models.CharField(max_length=10)
        vuelosInternacionales= models.BooleanField
        comentario= models.CharField(max_length=500)

    Modelos de la app Paquetes:

Para meter las tablas: python manage.py sqlmigrate "nombre de la app" 0001 esto crea la sentencia sql que crea la tabla y con python manage.py migrate las crea en el archivo db.sqlite3

Los elementos de la db los voy a crear a mano para el desafío, por lo menos algunos (despues ver poner mas con código)

Panel de administracion: python manage.py createsuperuser



cree las vistas y me copie los archivos que hizo el profe para ir probando. No me gusta la idea de copiarme una plantilla pero de momento vaaa!

Di funcionalidad la plantilla http://127.0.0.1:8000/integrantes/ para que traiga los elementos de la tabla integrantes y los muestre mediante una tabla hecha con bootstrap
