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
        chofer = Chofer.objects.get(rut = rut)
        serializer = ChoferSerializer(chofer, many=False)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)