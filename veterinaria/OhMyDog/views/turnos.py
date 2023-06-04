from django.shortcuts import render, redirect
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.turnos import (
    solicitar_turno,
    filtrar_turnos_pendientes,
    confirmar_turno_init,
    rechazar_turno_init,
    enviar_mail_confirmacion,
    enviar_mail_rechazo,
    cliente_tiene_turno_en_fecha,
)
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria
from datetime import datetime, date, timedelta
from django.contrib import messages
from OhMyDog.modelos.perros import buscar_perros_por_dueño
from OhMyDog.views.utils import agregar_mensaje_error


def solicitar_turnos(request):
    atenciones = TipoDeAtencion.objects.all()
    franjas_horarias = FranjaHoraria.objects.all()
    perros = buscar_perros_por_dueño(request.user.cliente)
    hoy = date.today()
    hoy = hoy + timedelta(days=1)

    context = {
        "atenciones": atenciones,
        "franjas_horarias": franjas_horarias,
        "min": hoy.strftime("%Y-%m-%d"),
        "perros": perros,
    }
    if request.method == "GET":
        render(request, "solicitar_turno.html", context)
    if request.method == "POST":
        fecha_solicitada = request.POST.get("fecha_solicitada")
        formato = "%Y-%m-%d"
        fecha_solicitada = datetime.strptime(fecha_solicitada, formato).date()
        if cliente_tiene_turno_en_fecha(request.user.cliente, fecha_solicitada) is None:
            if fecha_solicitada > date.today():
                franja_horaria = request.POST.get("franja_horaria")
                tipo_atencion = request.POST.get("tipo_de_atencion")
                notas = request.POST.get("notas")
                perro_id = request.POST.get("perro_id")
                solicitar_turno(
                    request.user.cliente,
                    fecha_solicitada,
                    franja_horaria,
                    perro_id,
                    tipo_atencion,
                    notas,
                )
                messages.success(request, f"Turno solicitado con exito. ")
            else:
                agregar_mensaje_error(
                    request, "La fecha del turno debe ser posterior al día de hoy."
                )
        else:
            agregar_mensaje_error(
                request, "Usted ya ha solicitado un turno en esa fecha."
            )
    return render(request, "solicitar_turno.html", context)


def solicitudes_de_turnos(request):
    turnos_pendientes = filtrar_turnos_pendientes()
    context = {"solicitudes_de_turnos": turnos_pendientes}
    return render(request, "solicitudes_de_turnos.html", context)


def confirmar_turno(request):
    if request.method == "POST":
        turno_id = request.POST.get("turno_id")
        observaciones = request.POST.get("observaciones")
        confirmar_turno_init(turno_id, observaciones)
        enviar_mail_confirmacion(turno_id, observaciones)
        messages.success(request, f"Turno confirmado con exito. ")
        return redirect("solicitudes_de_turnos")
    return render(request, "solicitudes_de_turnos.html")


def rechazar_turno(request):
    if request.method == "POST":
        turno_id = request.POST.get("turno_id")
        observaciones = request.POST.get("observaciones")
        rechazar_turno_init(turno_id, observaciones)
        enviar_mail_rechazo(turno_id, observaciones)
        messages.success(request, f"Turno rechazado con exito. ")
        return redirect("solicitudes_de_turnos")
    return render(request, "solicitudes_de_turnos.html")
