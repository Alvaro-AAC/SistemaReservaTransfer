from django.shortcuts import render
from .forms import Pasajero_Form

# Create your views here.

def home(request):
    ctx = {}
    form = Pasajero_Form().as_p()
    ctx['pasajeroForm'] = form
    return render(request, 'core/home.html', ctx)