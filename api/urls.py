from django.urls import path, include
from rest_framework import routers
from .views import ConductorViewSet, DocumentacionViewSet, VehiculoViewSet

router = routers.DefaultRouter()
router.register(r'conductores', ConductorViewSet)
router.register(r'documentacion', DocumentacionViewSet)
router.register(r'vehiculos', VehiculoViewSet)

urlpatterns = [
    path('',include(router.urls))
]