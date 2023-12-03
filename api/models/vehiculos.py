from django.db import models
from .conductores import Conductor


class Vehiculo(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    año = models.IntegerField()
    placa = models.CharField(max_length=10, unique=True)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    image_1 = models.ImageField(upload_to='vehiculo_images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='vehiculo_images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='vehiculo_images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='vehiculo_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.conductor} {self.marca} {self.modelo} - {self.placa} "
