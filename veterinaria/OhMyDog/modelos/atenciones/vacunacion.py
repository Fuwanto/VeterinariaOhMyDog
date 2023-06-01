from django.db import models
from OhMyDog.modelos.atenciones.atenciones import Atencion
from OhMyDog.modelos.tiposDeDosisVacunacion.tiposDeDosisVacunacion import TipoDeDosisVacunacion


class Vacunacion (models.Model):
    id = models.BigAutoField (primary_key=True)
    atencion = models.OneToOneField(Atencion, null=False, on_delete=models.CASCADE)
    vacuna = models.CharField(max_length=255)
    dosis = models.ForeignKey(TipoDeDosisVacunacion, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.atencion.perro.nombre}, {self.atencion.tipo_atencion.nombre,}, {self.atencion.fecha}, {self.vacuna}, {self.dosis.nombre}"    