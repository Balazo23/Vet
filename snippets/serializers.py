from rest_framework import serializers
from .models import *

""" 
ModelSerializer sirve para simplificar ya que este genera los campos de manera automatica

"""

# Creacion de clases Veterinarias, Mascotas, Clientes, Consultas, Diagnosticos


class VeterinariosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Veterinarios
        fields = '__all__'
        read_only_fields = ['id']


class MascotasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = '__all__'
        read_only_fields = ['id']


class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'
        read_only_fields = ['id']


class ConsultasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = '__all__'
        read_only_fields = ['id']


class DiagnosticosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Diagnosticos
        fields = '__all__'
        read_only_fields = ['id']
