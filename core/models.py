from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Marca(models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descripcion

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    propietario = models.CharField(max_length=255)
    cant_puertas = models.IntegerField(default=0)
    cant_pasajeros = models.IntegerField(default=0)
    transmision = models.CharField(max_length=255)
    capacidad = models.IntegerField(default=0)
    velo_maxima = models.IntegerField(default=0)
    image = models.ImageField(upload_to="vehiculos", blank=True, null=True)

    def __str__(self) -> str:
        return self.propietario

class Mantenimiento(models.Model):
    fecha_revision = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.descripcion

class AgendarHora(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    capacidad = models.IntegerField(default=0)
    servicio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    precio = models.IntegerField()
    image = models.ImageField(upload_to="productos", blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    productos = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fecha} -> {self.total}'