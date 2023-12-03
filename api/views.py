from rest_framework import viewsets
from .serializers import DocumentacionSerializer, ConductorSerializer, VehiculoSerializer, UsuariosSerializer, SolicitudSerializer, ObjetoSerializer, CargaSerializer
from .models import conductores, vehiculos,documentacion, usuarios, solicitudes

# Create your views here.

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = conductores.Conductor.objects.all()
    serializer_class = ConductorSerializer

class DocumentacionViewSet(viewsets.ModelViewSet):
    queryset = documentacion.Documentacion.objects.all()
    serializer_class = DocumentacionSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = vehiculos.Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = usuarios.Usuario.objects.all()
    serializer_class = UsuariosSerializer

class SolicitudesViewSet(viewsets.ModelViewSet):
    queryset = solicitudes.Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class ObjetosViewSet(viewsets.ModelViewSet):
    queryset = solicitudes.Objeto.objects.all()
    serializer_class = ObjetoSerializer

class CargasViewSet(viewsets.ModelViewSet):
    queryset = solicitudes.Carga.objects.all()
    serializer_class = CargaSerializer