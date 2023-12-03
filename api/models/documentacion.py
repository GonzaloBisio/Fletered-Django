from django.db import models
from .conductores import Conductor

class Documentacion(models.Model):
    conductor = models.OneToOneField(Conductor, on_delete=models.CASCADE)
    licencia_conducir = models.CharField(max_length=20)
    permiso_flete = models.CharField(max_length=20)

    def __str__(self):
        return f"Documentación de {self.conductor}"
