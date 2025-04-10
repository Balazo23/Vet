from django.db.models import Sum
from .models import *


def calcular_total_deuda(cliente):
    """Calcula la deuda total de un cliente."""
    return Facturas.objects.filter(
        clientes=cliente,
        estado_pago__in=['PENDIENTE', 'PARCIAL']
    ).aggregate(total=Sum('total_deuda'))['total'] or 0


def filtrar_mascotas_por_especie(especie):
    return Mascotas.objects.filter(especie__iexact=especie)
