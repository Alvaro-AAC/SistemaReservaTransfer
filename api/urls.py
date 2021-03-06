from django.urls import path
from .views import *

urlpatterns = [
    path('chofer/all/', lista_choferes),
    path('chofer/all/disponible/', lista_choferes_disponibles),
    path('chofer/<int:rut>/', chofer_rut),
    path('viaje/post/', generar_viaje),
    path('viaje/<int:id>/', viaje_id),
    path('pasajero/<int:rut>/', pasajero_rut),
]