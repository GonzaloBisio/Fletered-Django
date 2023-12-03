from rest_framework import serializers
from .models import Conductor, Documentacion, Vehiculo

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class DocumentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentacion
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
