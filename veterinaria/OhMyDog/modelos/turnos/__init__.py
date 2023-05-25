from django.db.models.query_utils import *  #  incluye funciones útiles para consultas de bases de datos en Django.

from OhMyDog.modelos.turnos.turnos import Turno
from datetime import date

def solicitar_turno(cliente_id, fecha_del_turno, franja_horaria_id,tipo_atencion_id,notas):
    turno = Turno(cliente_id = cliente_id, fecha_del_turno = fecha_del_turno, fecha_de_solicitud = date.today(),
                    franja_horaria_id= franja_horaria_id, tipo_atencion_id = tipo_atencion_id, estado_id = 1, notas = notas)
    turno.save()
    return turno