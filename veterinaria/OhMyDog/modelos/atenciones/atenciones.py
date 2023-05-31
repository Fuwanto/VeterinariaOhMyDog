from django.db import models
from OhMyDog.modelos.perros.perros import Perro
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion

class Atencion(models.Model):
    id = models.BigAutoField(primary_key=True)
    perro = models.OneToOneField(Perro, null=False, on_delete=models.CASCADE)
    fecha = models.DateField()
    observacion = models.TextField(null=True)
    tipo_atencion = models.ForeignKey(TipoDeAtencion, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.perro.nombre, self.tipo_atencion, self.fecha