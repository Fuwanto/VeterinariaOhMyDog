from django.db import models
from OhMyDog.modelos.atenciones.atenciones import Atencion


class Desparacitacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    atencion = models.OneToOneField(Atencion, null=False, on_delete=models.CASCADE)
    dosis = models.CharField(max_length=255)
    farmaco = models.CharField(max_length=255)
    parasito = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.atencion.perro.nombre}, {self.atencion.tipo_atencion.nombre,}, {self.atencion.fecha}, {self.farmaco}, {self.parasito}"
