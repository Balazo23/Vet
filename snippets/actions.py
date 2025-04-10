from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Facturas, Clientesdos, Veterinarios, Mascotas


# Decorador Action: filtrar veterinarios por especialidad


def especialidad_action(cls):
    @action(detail=False, methods=['get'])
    def especialidad(self, request):
        """
        Filtra veterinarios por especialidad.
        """
        especialidad = request.query_params.get('especialidad', None)
        if especialidad:
            veterinarios = Veterinarios.objects.filter(
                especialidad__iexact=especialidad)
            serializer = self.get_serializer(veterinarios, many=True)
            return Response(serializer.data)
        return Response({"error": "Debe proporcionar una especialidad"}, status=400)

    cls.especialidad = especialidad
    return cls

# Decorador Action: filtrar mascotas por especie


# def filtrar_por_especie_action(cls):
#     @action(detail=False, methods=['get'])
#     def filtrar_por_especie(self, request):
#         """
#         Filtra las mascotas por especie.
#         """
#         especie = request.query_params.get('especie', None)
#         if especie:
#             mascotas = Mascotas.objects.filter(especie__iexact=especie)
#             serializer = self.get_serializer(mascotas, many=True)
#             return Response(serializer.data)

#         return Response({"error": "Debe proporcionar una especie"}, status=400)

#     cls.filtrar_por_especie = filtrar_por_especie
#     return cls

# GET /api/mascotas/filtrar_por_especie/?especie=Canino

# Decorador Action: filtrar mascotas por peso


def filtrar_por_peso_action(cls):
    @action(detail=False, methods=['get'])
    def filtrar_por_peso(self, request):
        """
        Filtra las mascotas por peso mínimo y/o máximo.
        """
        peso_min = request.query_params.get('peso_min', None)
        peso_max = request.query_params.get('peso_max', None)

        mascotas = Mascotas.objects.all()

        if peso_min:
            mascotas = mascotas.filter(peso__gte=float(peso_min))

        if peso_max:
            mascotas = mascotas.filter(peso__lte=float(peso_max))

        serializer = self.get_serializer(mascotas, many=True)
        return Response(serializer.data)

    cls.filtrar_por_peso = filtrar_por_peso
    return cls
# GET /api/mascotas/filtrar_por_peso/?peso_min=5&peso_max=15

# Decorador Action: marcar una factura como pagada


def marcar_pagada_action(cls):
    @action(detail=True, methods=['POST', 'GET'])
    def marcar_pagada(self, request):
        factura = self.get_object()
        factura.estado_pago = "PAGADO"
        factura.save()
        return Response({"status": f"Factura{factura.id} marcada como PAGADA"})

    cls.marcar_pagada = marcar_pagada
    return cls
