from rest_framework import serializers
from proyecto.models import *

class TipoVehiculoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipo_Vehiculo
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):

    tipo_vehiculo = TipoVehiculoSerializer(read_only = True)

    class Meta:
        model = Vehiculo
        fields = '__all__'

class ChoferSerializer(serializers.ModelSerializer):

    vehiculo = VehiculoSerializer(read_only = True)
    empresa = EmpresaSerializer(read_only = True)

    class Meta:
        model = Chofer
        fields = ['rut', 'dv', 'nombre', 'apellido', 'telefono', 'vehiculo', 'empresa']