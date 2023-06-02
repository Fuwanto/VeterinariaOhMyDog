from django.db import models

from OhMyDog.modelos.clientes.clientes import Cliente
from OhMyDog.modelos.estadosDelTurno.estadosDelTurno import EstadoDelTurno
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.perros.perros import Perro

class Turno(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente, null=False, on_delete=models.CASCADE
    )
    perro = models.ForeignKey(
        Perro, null=True, on_delete=models.CASCADE
    )
    fecha_del_turno = models.DateField(null=False)
    fecha_de_solicitud = models.DateTimeField(null=False)
    franja_horaria = models.ForeignKey(
        FranjaHoraria, null=False, on_delete=models.CASCADE
    )
    tipo_atencion = models.ForeignKey(
        TipoDeAtencion, null=False, on_delete=models.CASCADE
    )
    estado = models.ForeignKey(EstadoDelTurno, null=False, on_delete=models.CASCADE)
    notas = models.TextField(null=True)
    observaciones = models.TextField(null=True)

    def __str__(self):
        return f"Cliente: {self.cliente_id}, Atencion: {self.tipo_atencion_id}, Turno: {self.fecha_del_turno}, {self.franja_horaria_id}, Estado del Turno: {self.estado_id},"
