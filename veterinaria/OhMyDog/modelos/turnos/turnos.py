from django.db import models
from VeterinariaOhMyDog.veterinaria.OhMyDog.modelos import Clientes, EstadoDelTurno, FranjaHoraria,TipoDeAtencion



    


class Turnos (models.Model):
    id = models.BigAutoField(primary_key = True)
    cliente_id = models.ForeignKey(Cliente, null=False)
    fecha_del_turno = models.DateField()
    fecha_de_solicitud = models.DateTimeField()
    franja_horaria_id = models.ForeignKey(FranjaHoraria, null=False)
    tipo_atencion_id = models.ForeignKey(TipoDeAtencion, null=False)
    estado_id = models.ForeignKey(EstadoDelTurno, null=False)
    notas = models.TextField()

