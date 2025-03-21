from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


router = DefaultRouter()
# router es un DefaultRouter de Django Rest Framework, que genera automáticamente las rutas para los viewsets de la API.
router.register(r'Mascotas', MascotasViewSet)
router.register(r'Clientes', ClientesViewSet)
router.register(r'Veterinarios', VeterinariosViewSet)
router.register(r'Consultas', ConsultasViewSet)
router.register(r'Diagnosticos', DiagnosticosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('Mascotas/buscar/', MascotasPorNombre.as_view(), name='buscar-nombre'),
    path('Mascotas/<int:pk>/', Mascotas_detail, name='Mascotas_detail'),
    path('Mascotas/', Mascotas_list, name='Mascotas_list')
]
