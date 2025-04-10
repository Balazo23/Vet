from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from snippets import views

restful_lc = {'get': 'list', 'post': 'create'}
restful_rud = {'get': 'retrieve',
               'patch': 'partial_update', 'delete': 'destroy'}
# Router es un DefaultRouter de Django Rest Framework, que genera automáticamente las rutas para los viewsets de la API.
# router = DefaultRouter()
# router.register(r'mascotas', MascotasViewSet)
# router.register(r'clientes', ClientesdosViewSet)
# router.register(r'veterinarios', VeterinariosViewSet)
# router.register(r'consultas', ConsultasViewSet)
# router.register(r'facturas', FacturasViewSet)
# router.register(r'historial-medico', HistorialMedicoViewSet)

# Rutas manuales
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
    re_path(r'^mascotas/all/$', views.MascotasViewSet.as_view(restful_lc)),
    re_path(r'^mascota(s)?/(?P<pk>[0-9]+)/$',
            views.MascotasViewSet.as_view(restful_rud)),
    re_path(r'^mascotas/terranova/$',
            views.MascotasDosViewSet.as_view(restful_lc)),
    re_path(r'^veterinarios/all/$',
            views.VeterinariosViewSet.as_view(restful_lc)),
    re_path(r'^veterinario(s)?/(?P<pk>[0-9]+)/$',
            views.VeterinariosViewSet.as_view(restful_rud)),
    re_path(r'^clientes/all/$',
            views.ClientesdosViewSet.as_view(restful_lc)),
    re_path(r'^cliente(s)?/(?P<pk>[0-9]+)/$',
            views.ClientesdosViewSet.as_view(restful_rud)),
    re_path(r'^consultas/all/$',
            views.ConsultasViewSet.as_view(restful_lc)),
    re_path(r'^consulta(s)?/(?P<pk>[0-9]+)/$',
            views.ConsultasViewSet.as_view(restful_rud)),
    re_path(r'^facturas/all/$',
            views.FacturasViewSet.as_view(restful_lc)),
    re_path(r'^factura(s)?/(?P<pk>[0-9]+)/$',
            views.FacturasViewSet.as_view(restful_rud)),
    re_path(r'^historialmedico/all/$',
            views.HistorialMedicoViewSet.as_view(restful_lc)),
    re_path(r'^historialmedico(s)?/(?P<pk>[0-9]+)/$',
            views.HistorialMedicoViewSet.as_view(restful_rud)),
]
