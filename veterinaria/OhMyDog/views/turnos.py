from django.shortcuts import render
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.turnos import solicitar_turno, filtrar_turnos_pendientes, confirmar_turno_init, rechazar_turno_init, enviar_mail_confirmacion, enviar_mail_rechazo
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria
from datetime import date
from django.contrib import messages



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
        if (fecha_solicitada > date.today()):
            fecha_solicitada = request.POST.get("fecha_solicitada")
            franja_horaria = request.POST.get("franja_horaria")
            tipo_atencion = request.POST.get("tipo_de_atencion")
            notas = request.POST.get("notas")
            solicitar_turno(request.user.cliente, fecha_solicitada, franja_horaria, tipo_atencion, notas)
            messages.error(request, f"Turno solicitado con exito. ")
        else:
            messages.error(request, f"La fecha del turno debe ser posterior al dia de hoy.")
    
    return render(request, "solicitar_turno.html", context)

def solicitudes_de_turnos(request):
    turnos_pendientes = filtrar_turnos_pendientes()
    context = {
        'solicitudes_de_turnos': turnos_pendientes
    }
    return render (request, "solicitudes_de_turnos.html", context)

def confirmar_turno(request, turno_id):
    confirmar_turno_init(turno_id)
    enviar_mail_confirmacion(turno_id)
    return render (request, "solicitudes_de_turnos.html")


def rechazar_turno(request, turno_id):
    rechazar_turno_init(turno_id)
    enviar_mail_rechazo(turno_id)
    return render (request, "solicitudes_de_turnos.html")



    
