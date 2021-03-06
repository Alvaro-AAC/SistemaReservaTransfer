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

class DestinoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destino
        fields = '__all__'

class PasajeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pasajero
        fields = '__all__'

class ViajeSerializer(serializers.ModelSerializer):

    pasajero = PasajeroSerializer(read_only = True)
    chofer = ChoferSerializer(read_only = True)
    destino = DestinoSerializer(read_only = True)
    
    class Meta:
        model = Viaje
        fields = ['pasajero', 'chofer', 'destino']