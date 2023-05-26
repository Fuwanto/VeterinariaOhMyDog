from django.shortcuts import render
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.turnos import solicitar_turno, filtrar_turnos_pendientes
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria


def solicitar_turnos(request):
    atenciones = TipoDeAtencion.objects.all()
    franjas_horarias = FranjaHoraria.objects.all()
    context = {
        'atenciones': atenciones,
        'franjas_horarias': franjas_horarias
    }
    if request.method == 'GET':
        render(request, "solicitar_turno.html", context)
    if request.method == 'POST':
        fecha_solicitada = request.POST.get("fecha_solicitada")
        franja_horaria = request.POST.get("franja_horaria")
        tipo_atencion = request.POST.get("tipo_de_atencion")
        notas = request.POST.get("notas")
        solicitar_turno(request.user.cliente, fecha_solicitada, franja_horaria, tipo_atencion, notas)
    return render(request, "solicitar_turno.html", context)

def turnos_pendientes(request):
    turnos_pendientes = filtrar_turnos_pendientes()
    return(request, "turnos_pendientes.html", {'turnos_pendientes' : turnos_pendientes})
