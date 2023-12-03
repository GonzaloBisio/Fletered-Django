from django.contrib import admin
from django.utils.html import format_html

from .models import conductores, vehiculos, documentacion, usuarios, solicitudes

# Register your models here.

class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'correo', 'telefono', 'display_imagen_conductor')

    def display_imagen_conductor(self, obj):
        # Display the conductor's image in the admin list view
        if obj.imagen_conductor:
            return format_html('<img src="{}" height="50" />', obj.imagen_conductor.url)
        return '-'

    display_imagen_conductor.allow_tags = True
    display_imagen_conductor.short_description = 'Conductor Image'

admin.site.register(conductores.Conductor, ConductorAdmin)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'año', 'placa', 'conductor', 'display_images')

    def display_images(self, obj):
        # Display thumbnail images in the admin list view
        image_tags = []
        for field_name in ['image_1', 'image_2', 'image_3', 'image_4']:
            image_field = getattr(obj, field_name)
            if image_field:
                image_tags.append(f'<img src="{image_field.url}" height="50" />')

        return format_html(', '.join(image_tags))

    display_images.allow_tags = True
    display_images.short_description = 'Images'

admin.site.register(vehiculos.Vehiculo, VehiculoAdmin)
admin.site.register(documentacion.Documentacion)
admin.site.register(usuarios.Usuario)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'conductor', 'objetos', 'total_peso', 'creation_time')

admin.site.register(solicitudes.Solicitud, SolicitudAdmin)
admin.site.register(solicitudes.Objeto)
admin.site.register(solicitudes.Carga)