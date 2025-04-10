from snippets.models import *
from Scripts.data import *

# metodo que crea mascota


# def create_mascota(mascotas):
#     for mascota in mascotas:
#         print('mascota', mascota)
#         Mascotas.objects.create(**mascota)


# create_mascota(mascotas_arr)


def create_cliente(clientes):
    for cliente in clientes:
        print('cliente', cliente)
        Clientesdos.objects.create(**cliente)


create_cliente(clientes_arr)


def create_veterinario(veterinarios):
    for veterinario in veterinarios:
        print('veterinario', veterinario)
        Veterinarios.objects.create(**veterinario)


create_veterinario(veterinarios_arr)


# def create_consulta(consultas):
#     for consulta in consultas:
#         print('consulta', consulta)
#         Consultas.objects.create(**consulta)


# create_consulta(consultas_arr)


# def create_factura(facturas):
#     for factura in facturas:
#         print('factura', factura)
#         Facturas.objects.create(**factura)


# create_factura(facturas_arr)


# def create_historialmedico(historialm):
#     for historialmedico in historialm:
#         print('historial', historialmedico)
#         HistorialMedico.objects.create(**historialmedico)


# create_historialmedico(historial_arr)
# buscar mascota y cambiarle el nombre

# todas las mascotas que sean caninos
# todas las mascotas caninas que hayan nacido en el 2015
# todas las mascotas que pesen mas de 10 kg
