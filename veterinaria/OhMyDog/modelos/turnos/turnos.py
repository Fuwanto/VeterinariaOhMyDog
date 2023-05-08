from django.db import models
from VeterinariaOhMyDog.veterinaria.OhMyDog.modelos import Clientes

class FranjasHorarias(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

class EstadosDelTurno(model.Model):
    


class Turnos (models.Model):
    id = models.BigAutoField(primary_key = True)
    cliente_id = models.ForeignKey(Clientes, null=False)
    fecha_del_turno = models.DateField()
    fecha_de_solicitud = models.DateTimeField()
    franjas_horarias = models.ForeignKey(FranjasHorarias, null=False)
    tipo_atencion_id = models.ForeignKey(TiposDeAtencion, null=False)
    estado_id = models.ForeignKey(EstadosDelTurno, null=False)
    notas = models.TextField()

