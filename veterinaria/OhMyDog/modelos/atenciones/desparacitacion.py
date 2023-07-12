from django.db import models
from OhMyDog.modelos.atenciones.atenciones import Atencion


class Desparacitacion(models.Model):
    class Meta:
        verbose_name_plural = "Desparasitaciones"

    id = models.BigAutoField(primary_key=True)
    atencion = models.OneToOneField(Atencion, null=False, on_delete=models.CASCADE)
    farmaco = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=50, blank=False, default="asd")
    num_serie = models.CharField(max_length=50, blank=False, default="asd")
    num_lote = models.CharField(max_length=50, blank=False, default="asd")
    dosis = models.CharField(max_length=255)
    diagnostico = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.atencion.perro.nombre}, {self.atencion.tipo_atencion.nombre,}, {self.atencion.fecha}, {self.farmaco}, {self.diagnostico}"
