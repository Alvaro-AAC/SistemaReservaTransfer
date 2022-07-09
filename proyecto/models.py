import datetime
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.hashers import make_password, identify_hasher

# Create your models here.

class Marca(models.Model):
    descripcion = models.CharField(unique=True, max_length=100)
    
    def __str__(self):
        return self.descripcion

class Modelo(models.Model):
    descripcion = models.CharField(max_length=100)
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)

    class Meta:
        unique_together = [['marca', 'descripcion']]

    def __str__(self):
        return self.descripcion

class Tipo_Vehiculo(models.Model):
    descripcion = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = 'Tipos de vehiculo'
        verbose_name = 'Tipo vehiculo'

class Empresa(models.Model):
    rut_empresa = models.IntegerField(unique=True)
    dv_empresa = models.CharField(max_length=1)
    nombre = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.CheckConstraint(check = models.Q(rut_empresa__range=(48000000, 99000000)), name='check_empresa_rut'),
            models.CheckConstraint(check = models.Q(dv_empresa__in='0123456789K'), name='check_empresa_dv'),
        ]

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    patente = models.CharField(unique=True, max_length=6)
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    tipo_vehiculo = models.ForeignKey('Tipo_Vehiculo', on_delete=models.CASCADE)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.patente[0:2] + '-' + self.patente[2:4] + '-' + self.patente[4:6]

class Chofer(models.Model):
    rut = models.IntegerField(unique=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField(unique=True)
    password = models.CharField(max_length=3000)
    habilitado = models.BooleanField(default=True)
    disponible = models.BooleanField(default=False)
    vehiculo = models.OneToOneField('Vehiculo', on_delete=models.CASCADE)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(check = models.Q(rut__range=(1000000, 40000000)), name='check_chofer_rut'),
            models.CheckConstraint(check = models.Q(dv__in='0123456789K'), name='check_chofer_dv'),
            models.CheckConstraint(check = models.Q(telefono__range=(100000000, 999999999)), name='check_chofer_telefono'),
        ]
        verbose_name_plural = 'Choferes'

    def save(self, *args, **kwargs):
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super(Chofer, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Pasajero(models.Model):
    rut = models.IntegerField(unique=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField(null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check = models.Q(rut__range=(1000000, 40000000)), name='check_pasajero_rut'),
            models.CheckConstraint(check = models.Q(dv__in='0123456789K'), name='check_pasajero_dv'),
            models.CheckConstraint(check = models.Q(telefono__range=(100000000, 999999999)), name='check_pasajero_telefono'),
        ]
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Destino(models.Model):
    direccion = models.CharField(max_length=300)

    def __str__(self):
        return self.direccion

class Viaje(models.Model):
    pasajero = models.ForeignKey('Pasajero', on_delete=models.CASCADE)
    chofer = models.ForeignKey('Chofer', on_delete=models.CASCADE)
    destino = models.ForeignKey('Destino', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pasajero) + ' - ' + str(self.chofer) + ' - ' + str(self.destino)