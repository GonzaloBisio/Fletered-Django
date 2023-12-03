from django.db import models

from .conductores import Conductor
from .usuarios import Usuario

class Objeto(models.Model):
    nombre = models.CharField(max_length=100)
    peso = models.PositiveIntegerField(default=0)
    alto = models.PositiveIntegerField(default=0)
    ancho = models.PositiveIntegerField(default=0)
    caracteristica = models.CharField(max_length=100, default='')
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.nombre} - {self.caracteristica}"

class Carga(models.Model):
    objetos = models.ManyToManyField(Objeto)

    def __str__(self):
        return f"Carga con {self.objetos.count()} objetos"

class Solicitud(models.Model):
    cliente = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    conductor = models.OneToOneField(Conductor, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    ciudad_origen = models.CharField(max_length=100, default='')
    provincia_origen = models.CharField(max_length=100, default='')
    calle_origen = models.CharField(max_length=100, default='')
    numeracion_origen = models.PositiveIntegerField(default=0)
    ciudad_destino = models.CharField(max_length=100, default='')
    provincia_destino = models.CharField(max_length=100, default='')
    calle_destino = models.CharField(max_length=100, default='')
    numeracion_destino = models.PositiveIntegerField(default=0)
    carga = models.ForeignKey(Carga, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"Solicitud de {self.cliente}"

    def objetos(self):
        object_names = self.carga.objetos.values_list('nombre', flat=True)
        return ', '.join(object_names)

    def total_peso(self):
        total_weight = sum(self.carga.objetos.values_list('peso', flat=True))
        return f"{total_weight} (kg)"

