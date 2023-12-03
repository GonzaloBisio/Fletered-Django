from django.urls import path, include
from rest_framework import routers
from .views import ConductorViewSet, DocumentacionViewSet, VehiculoViewSet, UsuariosViewSet, SolicitudesViewSet, CargasViewSet, ObjetosViewSet

router = routers.DefaultRouter()
router.register(r'conductores', ConductorViewSet)
router.register(r'documentacion', DocumentacionViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'usuarios', UsuariosViewSet)
router.register(r'solicitudes', SolicitudesViewSet)
router.register(r'objetos', ObjetosViewSet)
router.register(r'cargas', CargasViewSet)

urlpatterns = [
    path('',include(router.urls))
]