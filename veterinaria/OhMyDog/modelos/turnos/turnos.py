from django.db import models
from OhMyDog.modelos.clientes.clientes import Cliente
from OhMyDog.modelos.estadosDelTurno.estadosDelTurno import EstadoDelTurno
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion

class Turno (models.Model):
    id = models.BigAutoField(primary_key = True)
    cliente_id = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)
    fecha_del_turno = models.DateField()
    fecha_de_solicitud = models.DateTimeField()
    franja_horaria_id = models.ForeignKey(FranjaHoraria, null=False,on_delete=models.CASCADE)
    tipo_atencion_id = models.ForeignKey(TipoDeAtencion, null=False,on_delete=models.CASCADE)
    estado_id = models.ForeignKey(EstadoDelTurno, null=False, on_delete=models.CASCADE)
    notas = models.TextField(null=True)
    
    def __str__(self):
        return f"Cliente: {self.cliente_id}, Atencion: {self.tipo_atencion_id}, Turno: {self.fecha_del_turno}, {self.franja_horaria_id}, Estado del Turno: {self.estado_id},"
