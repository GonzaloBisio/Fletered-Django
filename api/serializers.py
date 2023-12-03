from rest_framework import serializers
from .models import conductores, documentacion, vehiculos, usuarios, solicitudes

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = conductores.Conductor
        fields = '__all__'

class DocumentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = documentacion.Documentacion
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = vehiculos.Vehiculo
        fields = '__all__'
class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios.Usuario
        fields = '__all__'
        read_only_fields = ('creation_time',)

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = solicitudes.Solicitud
        fields = '__all__'
        read_only_fields = ('creation_time',)

class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = solicitudes.Objeto
        fields = '__all__'

class CargaSerializer(serializers.ModelSerializer):
    class Meta:
        model = solicitudes.Carga
        fields = '__all__'