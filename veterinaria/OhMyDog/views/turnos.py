from django.shortcuts import render, redirect
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.turnos import (
    solicitar_turno,
    filtrar_turnos_pendientes,
    confirmar_turno_init,
    rechazar_turno_init,
    enviar_mail_confirmacion,
    enviar_mail_rechazo,
)
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria
from datetime import datetime, date, timedelta
from django.contrib import messages


def solicitar_turnos(request):
    atenciones = TipoDeAtencion.objects.all()
    franjas_horarias = FranjaHoraria.objects.all()

    hoy = date.today()
    hoy = hoy + timedelta(days=1)

    context = {
        "atenciones": atenciones,
        "franjas_horarias": franjas_horarias,
        "min": hoy.strftime("%Y-%m-%d"),
    }
    if request.method == "GET":
        render(request, "solicitar_turno.html", context)
    if request.method == "POST":
        fecha_solicitada = request.POST.get("fecha_solicitada")
        formato = "%Y-%m-%d"
        fecha_solicitada = datetime.strptime(fecha_solicitada, formato).date()
        if fecha_solicitada > date.today():
            franja_horaria = request.POST.get("franja_horaria")
            tipo_atencion = request.POST.get("tipo_de_atencion")
            notas = request.POST.get("notas")
            solicitar_turno(
                request.user.cliente,
                fecha_solicitada,
                franja_horaria,
                tipo_atencion,
                notas,
            )
            messages.success(request, f"Turno solicitado con exito. ")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                f"La fecha del turno debe ser posterior al dia de hoy.",
                extra_tags="danger",
            )

    return render(request, "solicitar_turno.html", context)


def solicitudes_de_turnos(request):
    turnos_pendientes = filtrar_turnos_pendientes()
    context = {"solicitudes_de_turnos": turnos_pendientes}
    return render(request, "solicitudes_de_turnos.html", context)


def confirmar_turno(request):
    if request.method == "POST":
        turno_id = request.POST.get("turno_id")
        next_url = request.POST.get("next")
        confirmar_turno_init(turno_id)
        enviar_mail_rechazo(turno_id)
        print(next_url)
        if next_url:
            messages.success(request, f"Turno confirmado con exito. ")
            return redirect(next_url)
    return render(request, "solicitudes_de_turnos.html")


def rechazar_turno(request):
    if request.method == "POST":
        turno_id = request.POST.get("turno_id")
        rechazar_turno_init(turno_id)
        enviar_mail_rechazo(turno_id)
        next_url = request.POST.get("next")

        if next_url:
            messages.success(request, f"Turno rechazado con exito. ")
            return redirect(next_url)
    return render(request, "solicitudes_de_turnos.html")
