from django.db import models

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=False)  # Add default value
    edad = models.PositiveIntegerField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    imagen_conductor = models.ImageField(upload_to='conductor_images/', blank=True, null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
