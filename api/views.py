from rest_framework import viewsets
from .serializers import DocumentacionSerializer, ConductorSerializer, VehiculoSerializer
from .models import Conductor, Vehiculo, Documentacion

# Create your views here.

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer

class DocumentacionViewSet(viewsets.ModelViewSet):
    queryset = Documentacion.objects.all()
    serializer_class = DocumentacionSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
