from dataclasses import Field, field
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField('nombre',max_length=50)
    camada = models.IntegerField()
    def __str__(self):
        return f'{self.nombre}-{self.camada}'
     
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return self.apellido
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    def __str__(self):
        return self.apellido
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    
