from django.db.models.query_utils import *  #  incluye funciones útiles para consultas de bases de datos en Django.
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from OhMyDog.modelos.turnos.turnos import Turno
from datetime import datetime,date
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria 
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.estadosDelTurno.estadosDelTurno import EstadoDelTurno
from django.core.mail import send_mail
from django.conf import settings

def solicitar_turno(cliente, fecha_del_turno, franja_horaria_id,tipo_atencion_id,notas):
    franja_horaria = get_object_or_404(FranjaHoraria, id=franja_horaria_id)
    tipo_atencion = get_object_or_404(TipoDeAtencion, id=tipo_atencion_id)
    turno = Turno(cliente = cliente, fecha_del_turno = fecha_del_turno, fecha_de_solicitud = datetime.today(),
                    franja_horaria= franja_horaria, tipo_atencion = tipo_atencion,
                    estado = get_object_or_404(EstadoDelTurno, id = 1), notas = notas)
    turno.save()
    return turno

def filtrar_turnos_pendientes():
    estado_pendiente = get_object_or_404(EstadoDelTurno, id = 1)
    return Turno.objects.filter(estado = estado_pendiente)

def filtrar_turnos_por_cliente(cliente):
    return Turno.objects.filter(cliente = cliente)

def confirmar_turno_init (turno_id, observaciones):
    turno = Turno.objects.get(id = turno_id)
    turno.observaciones = observaciones
    estado = EstadoDelTurno.objects.get(id = 2)
    turno.estado = estado
    turno.save()

def rechazar_turno_init (turno_id, observaciones):
    turno = Turno.objects.get(id = turno_id)
    turno.observaciones = observaciones
    estado = EstadoDelTurno.objects.get(id = 3)
    turno.estado = estado
    turno.save()

def enviar_mail_confirmacion (turno_id, observaciones):
    turno = Turno.objects.get(id = turno_id)
    send_mail(
        "Su turno ha sido confirmado.",
        f"Estimado cliente, su turno para el dia {turno.fecha_del_turno} para una {turno.tipo_atencion.nombre} ha sido confirmado.\nObservaciones: {observaciones}",
        settings.EMAIL_HOST_USER,
        [turno.cliente.email],
        fail_silently=False,
    )

def enviar_mail_rechazo (turno_id, observaciones):
    turno = Turno.objects.get(id = turno_id)
    send_mail(
        "Su turno ha sido rechazado.",
        f"Estimado cliente, su turno para el dia {turno.fecha_del_turno} para una {turno.tipo_atencion.nombre} ha sido rechazado.\nObservaciones: {observaciones}",
        settings.EMAIL_HOST_USER,
        [turno.cliente.email],
        fail_silently=False,
    )

def cliente_tiene_turno_en_fecha (cliente, fecha):
    try:
        return Turno.objects.get(cliente = cliente, fecha_del_turno = fecha)
    except:
        return None
    

        
       



