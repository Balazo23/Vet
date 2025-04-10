from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from .queries import calcular_total_deuda, filtrar_mascotas_por_especie
""" 
ModelSerializer sirve para simplificar ya que este genera los campos de manera automatica

"""

# Creacion de clases Veterinarias, Mascotas, Clientes, Consultas, Diagnosticos


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class VeterinariosSerializers(serializers.ModelSerializer):
    user = UserSerializers()  # Relacionar el usuario con los veterinarios

    class Meta:
        model = Veterinarios
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        veterinarios = Veterinarios.objects.create(user=user, **validated_data)
        return veterinarios


class MascotasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = '__all__'

    def get_mascotas_por_especie(self, obj):
        return filtrar_mascotas_por_especie(obj)


class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clientesdos
        fields = '__all__'

    # def get_total_deuda(self, obj):
    #     return calcular_total_deuda(obj)


class ConsultasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = '__all__'


class FacturasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Facturas
        fields = '__all__'


class HistorialMedicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = HistorialMedico
        fields = '__all__'
