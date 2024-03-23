from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    proyecto = models.ForeignKey('Proyectos', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Proyectos(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre