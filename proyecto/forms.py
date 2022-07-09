from django import forms
from .models import Pasajero

class Pasajero_Form(forms.ModelForm):

    class Meta:
        model = Pasajero
        fields = ['rut', 'nombre','apellido','telefono']

        widgets = {
            'rut':forms.TextInput(attrs={"class":"form-control", 'placeholder': '12345678-9', 'pattern': '^[0-9]{7,8}-[0-9Kk]{1}$', 'title': 'Debe ingresar un rut válido.'}),
            'nombre':forms.TextInput(attrs={"class":"form-control", 'pattern': '^[A-Z\u00d1Á-Ú]{1}[a-z\u00f1á-ú]{1,}$',  'title': 'Debe contener la primera letra en mayuscula y el resto en minuscula.'}),
            'apellido':forms.TextInput(attrs={"class":"form-control",  'pattern': '^[A-Z\u00d1Á-Ú]{1}[a-z\u00f1á-ú]{1,}$', 'title': 'Debe contener la primera letra en mayuscula y el resto en minuscula.'}),
            'telefono':forms.NumberInput(attrs={"class":"form-control",  'min': '910000000', 'max': '999999999'}),
        }

        labels = {
            'nombre':'Nombre',
            'apellido':'Apellido',
            'edad':'Edad',
            'telefono':'Telefono',
        }