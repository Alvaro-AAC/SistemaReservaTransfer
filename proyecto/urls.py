from django.urls import path
from .views import home, datos 

urlpatterns = [
    path('', home,name="home"),
    path('datos.html', datos, name="datos"),
]