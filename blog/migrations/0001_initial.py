# Generated by Django 4.0.5 on 2022-06-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarioId', models.IntegerField()),
                ('fechaHora', models.DateTimeField()),
                ('contenido', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('pais', models.CharField(max_length=20)),
                ('deseaInfo', models.BooleanField()),
                ('idioma', models.CharField(max_length=2)),
                ('fechaRegistro', models.DateTimeField()),
                ('avatar', models.CharField(max_length=50)),
            ],
        ),
    ]
