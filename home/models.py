from django.db import models
from django.contrib.auth.models import User

# Create your models here. 
class Perfil(models.Model):
    GENERO      = (('femenino', 'Femenino'), 
                   ('masculino', 'Masculino'))

    imagen      = models.ImageField(upload_to = 'perfiles', null = True, blank = True)
    telefono    = models.CharField(max_length = 100, null = True, blank = True)
    genero      = models.CharField(max_length = 25, choices = GENERO)
    user        = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.telefono

class Marca(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__ (self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__ (self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length = 100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    status = models.BooleanField(default = True)
    picture = models.ImageField(upload_to = 'pictures', null = True, blank = True)
    marca = models.ForeignKey(Marca, on_delete = models.PROTECT)
    categoria = models.ManyToManyField(Categoria, blank = True)

    def __str__ (self):
        return self.nombre
