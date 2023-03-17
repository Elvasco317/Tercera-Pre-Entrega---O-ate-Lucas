from django.db import models

# Create your models here.

class Persona:
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField()

#Genero un modelo que herede lo mismo

class Persona2(models.Model, Persona):
    pass

