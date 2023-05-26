from django.db.models.query_utils import *  #  incluye funciones útiles para consultas de bases de datos en Django.
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from OhMyDog.modelos.turnos.turnos import Turno
from datetime import datetime
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria 
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.estadosDelTurno.estadosDelTurno import EstadoDelTurno

def solicitar_turno(cliente, fecha_del_turno, franja_horaria_id,tipo_atencion_id,notas):
    franja_horaria = get_object_or_404(FranjaHoraria, id=franja_horaria_id)
    tipo_atencion = get_object_or_404(TipoDeAtencion, id=tipo_atencion_id)
    turno = Turno(cliente = cliente, fecha_del_turno = fecha_del_turno, fecha_de_solicitud = datetime.today(),
                    franja_horaria= franja_horaria, tipo_atencion_ = tipo_atencion,
                    estado = get_object_or_404(EstadoDelTurno, id = 1), notas = notas)
    turno.save()
    return turno

def filtrar_turnos_pendientes():
    estado_pendiente = get_object_or_404(EstadoDelTurno, id = 1)
    return Turno.objects.filter(estado = estado_pendiente)

def filtrar_turnos_por_cliente(cliente):
    return Turno.objects.filter(cliente = cliente)