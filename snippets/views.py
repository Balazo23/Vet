from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.reverse import reverse
from rest_framework import mixins, permissions, generics, status
from rest_framework import viewsets, renderers, filters
from .serializers import *
from .models import *
from django.http import Http404
from django.db.models import Sum
from pygments import highlight
from .abstractviews import AbstractViewSet
from .actions import *
# Create your views here.


# Un ViewSet proporciona una implementacion de alto nivel para crear listas relacionadas con un modelo

@especialidad_action
class VeterinariosViewSet(viewsets.ModelViewSet):
    queryset = Veterinarios.objects.all()
    serializer_class = VeterinariosSerializers
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
# /api/veterinarios/por_especialidad/?especialidad=Cardiologo


# @filtrar_por_especie_action
# @filtrar_por_peso_action
class MascotasViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all()
    serializer_class = MascotasSerializers
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

# /api/Mascotas/caninos/
# /api/Mascotas/ligeros/


class ClientesdosViewSet(AbstractViewSet):
    queryset = Clientesdos.objects.all()
    serializer_class = ClientesSerializers
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

# /api/Clientes/deudores/


class ConsultasViewSet(AbstractViewSet):
    queryset = Consultas.objects.all().order_by("pk")
    serializer_class = ConsultasSerializers
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


@marcar_pagada_action
class FacturasViewSet(AbstractViewSet):
    queryset = Facturas.objects.all()
    serializer_class = FacturasSerializers
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]

# /api/facturas/{id}/marcar_pagada/


class HistorialMedicoViewSet(AbstractViewSet):
    queryset = HistorialMedico.objects.all().order_by("pk")
    serializer_class = HistorialMedicoSerializers
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]


class MascotasDosViewSet(MascotasViewSet):
    queryset = Mascotas.objects.filter(raza="Terranova")
