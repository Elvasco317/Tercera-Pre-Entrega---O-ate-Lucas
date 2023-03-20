from django.db import models 

# Create your models here.

class Cursos(models.Model): 
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.camada}"

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido} - {self.email}"

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido} - {self.email}"