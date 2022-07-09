from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from proyecto.models import *
from .serializers import *

# Create your views here.

@api_view(['GET',])
def lista_choferes(request):
    if request.method == 'GET':
        choferes = Chofer.objects.all()
        serializer = ChoferSerializer(choferes, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def lista_choferes_disponibles(request):
    if request.method == 'GET':
        choferes = Chofer.objects.filter(disponible = True).all()
        serializer = ChoferSerializer(choferes, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def chofer_rut(request, rut):
    if request.method == 'GET':
        try:
            chofer = Chofer.objects.get(rut = rut)
        except Chofer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ChoferSerializer(chofer, many=False)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST',])
def generar_viaje(request):
    if request.method == 'POST':
        rut = request.POST['rut'][0:len(request.POST['rut'])-2]
        dv = request.POST['rut'][-1]
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        rut_chofer = request.POST['chofer']
        try:
            pasajero = Pasajero.objects.get(rut = rut)
        except Pasajero.DoesNotExist:
            pasajero = Pasajero(rut = rut, dv = dv, nombre = nombre, apellido = apellido, telefono = telefono)
            pasajero.save()
        destino = Destino(direccion = direccion)
        destino.save()
        try:
            chofer = Chofer.objects.get(rut = rut_chofer)
        except Chofer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        viaje = Viaje(pasajero = pasajero, chofer = chofer, destino = destino)
        viaje.save()
        idViaje = viaje.pk
        return Response({'id': idViaje}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def viaje_id(request, id):
    if request.method == 'GET':
        try:
            viaje = Viaje.objects.get(pk = id)
        except Viaje.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ViajeSerializer(viaje, many=False)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def pasajero_rut(request, rut):
    if request.method == 'GET':
        try:
            pasajero = Pasajero.objects.get(rut = rut)
        except Pasajero.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PasajeroSerializer(pasajero, many=False)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)