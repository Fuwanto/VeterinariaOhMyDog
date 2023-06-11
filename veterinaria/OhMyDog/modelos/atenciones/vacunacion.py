from django.db import models
from OhMyDog.modelos.atenciones.atenciones import Atencion
from OhMyDog.modelos.tiposDeDosisVacunacion.tiposDeDosisVacunacion import TipoDeDosisVacunacion


class Vacunacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    atencion = models.OneToOneField(Atencion, null=False, on_delete=models.CASCADE)
    vacunas = [("Antiviral", "Antiviral"), ("Antirrabica", "Antirrabica")]
    vacuna = models.CharField(choices=vacunas, max_length=14)
    fabricante = models.CharField(max_length=50, blank=False, default="asd")
    num_serie = models.CharField(max_length=50, blank=False, default="asd")
    num_lote = models.CharField(max_length=50, blank=False, default="asd")
    dosis = models.DecimalField(blank=False, max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.atencion.perro.nombre}, {self.atencion.tipo_atencion.nombre,}, {self.atencion.fecha}, {self.vacuna}, {self.dosis}"
