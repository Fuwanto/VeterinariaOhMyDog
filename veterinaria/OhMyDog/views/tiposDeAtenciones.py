from django.contrib import messages
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from django.shortcuts import render

def todasAtenciones(request):
    atenciones = TipoDeAtencion.objects.all()
    context = {
        "atenciones": atenciones
    }
    return render(request, 'solicitar_turno.html', context)