from django.db import models
from OhMyDog.modelos.perros.perros import Perro
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion

class Atencion(models.Model):
    id = models.BigAutoField(primary_key=True)
    perro = models.ForeignKey(Perro, null=False, on_delete=models.CASCADE)
    fecha = models.DateField(null=False)
    observacion = models.TextField(null=True)
    tipo_atencion = models.ForeignKey(TipoDeAtencion, null=False, on_delete=models.CASCADE)
    url_mostrar_datos = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id},{self.perro.nombre}, {self.perro.id}, {self.tipo_atencion.nombre,}, {self.fecha}, {self.url_mostrar_datos}"