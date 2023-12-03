from django.db import models

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    # Agrega más campos según sea necesario

    def __str__(self):
        return self.nombre

class Documentacion(models.Model):
    conductor = models.OneToOneField(Conductor, on_delete=models.CASCADE)
    licencia_conducir = models.CharField(max_length=20)
    permiso_flete = models.CharField(max_length=20)
    # Agrega más campos según sea necesario

    def __str__(self):
        return f"Documentación de {self.conductor}"

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    año = models.IntegerField()
    placa = models.CharField(max_length=10, unique=True)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    # Agrega más campos según sea necesario

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"
