from django.contrib import admin
from .models import Conductor, Vehiculo, Documentacion

# Register your models here.

admin.site.register(Conductor)
admin.site.register(Vehiculo)
admin.site.register(Documentacion)
