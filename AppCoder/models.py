
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#recordar cada vez que se haga un modelo nuevo se debe hacer la migracion a la base de datos apra que tome la table del modelo, entonce debemos ejecutar comando primero makemigrations y despues el migrate, si esta k quiere decir que se cargo en la DB.
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
        return f'{self.nombre} {self.apellido}'
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    

class Avatar(models.Model):
    #vinculo el usuario a la imagen
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #vinculo el modelo para poder subir imagenes
    imagen = models.ImageField(upload_to='avatares', null=True,blank=True)
    def __str__(self):
        return f"imagen de: {self.user.username}"