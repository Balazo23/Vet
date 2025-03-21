from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *
from .models import *
# Create your views here.

# Un ViewSet proporciona una implementacion de alto nivel para crear listas relacionadas con un modelo
# Se prefirio el uso de ViewSet antes que el de APIview porque este facilita la creacion de la api, DRF genera automatico los metodos CRUD


class VeterinariosViewSet(viewsets.ModelViewSet):
    # define los objetos que el ViewSet manejara
    queryset = Veterinarios.objects.all()
    serializer_class = VeterinariosSerializers


class MascotasViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all()  # define los objetos que el ViewSet manejara
    serializer_class = MascotasSerializers


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()  # define los objetos que el ViewSet manejara
    serializer_class = ClientesSerializers


class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()  # define los objetos que el ViewSet manejara
    serializer_class = ConsultasSerializers


class DiagnosticosViewSet(viewsets.ModelViewSet):
    # define los objetos que el ViewSet manejara
    queryset = Diagnosticos.objects.all()
    serializer_class = DiagnosticosSerializers


class MascotasPorNombre(APIView):
    def get(self, request):
        nombre = request.GET.get("Nombre", "").strip()

        if nombre:
            mascota = Mascotas.objects.filter(Nombre__icontains=nombre)

            if mascota.exists():
                serializer = MascotasSerializers(mascota, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response({"error": "No se encontró ninguna mascota con ese nombre"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": "Debes enviar un parámetro"}, status=status.HTTP_400_BAD_REQUEST)

# Mascotas


@api_view(['GET', 'POST'])
def Mascotas_list(request):
    if request.method == 'GET':
        mascotas = Mascotas.objects.all()
        serializer = MascotaSerializers(mascotas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MascotasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Mascotas_detail(request, pk):
    mascotas = get_object_or_404(Mascotas, pk=pk)

    if request.method == 'GET':
        serializer = MascotasSerializers(mascotas)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = MascotasSerializers(mascotas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        mascotas.delete()
        return Response({"message": "Mascota eliminada"}, status=status.HTTP_204_NO_CONTENT)
