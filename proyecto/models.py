from django.db import models

# Create your models here.

class Chofer(models.Model):
    nomchofer = models.CharField(max_length=100, verbose_name='Nombre del chofer')
    tipovehiculo = models.CharField(max_length=50, verbose_name='Tipo de vehiculo')
    empresa = models.CharField(max_length=100, verbose_name='Nombre de la empresa')


    def __str__(self):
        return self.nomchofer


class Vehiculo(models.Model):
    colorvehiculo = models.CharField(max_length=25, verbose_name='Color del vehiculo')