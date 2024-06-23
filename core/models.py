from django.db import models

# Create your models here.
class Genero(models.Model):
    descripcion = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.descripcion

class Marca(models.Model):
    descripcion = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.descripcion

class CustomUsuario(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="usuarios", blank=True, null=True)
    """ user = models.ForeignKey(User, on_delete=models.CASCADE) """

    def __str__(self) -> str:
        return self.nombre


class Vehiculo(models.Model):
    propietario = models.CharField(max_length = 20)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    cant_puertas = models.IntegerField(default=0)
    cant_pasajeros = models.IntegerField(default=0)
    transmision = models.CharField(max_length = 20)
    capacidad = models.IntegerField(default=0)
    velo_maxima = models.IntegerField(default=0)
    image = models.ImageField(upload_to="vehiculos", blank=True, null=True)

    def __str__(self) -> str:
        return self.propietario

class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return self.descripcion
    

class Empleado(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    correo = models.CharField(max_length = 100)
    tipo = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="empleados", blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nombre + " " + self.apellido


class Mantenimiento(models.Model):
    fecha_revision = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.descripcion

class AgendarHora(models.Model):
    nombre = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    capacidad = models.IntegerField(default=0)
    servicio = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.nombre

