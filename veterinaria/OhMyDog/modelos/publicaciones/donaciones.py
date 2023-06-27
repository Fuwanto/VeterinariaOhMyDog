from django.db import models

class Donacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    objetivo = models.TextField(null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activa = models.BooleanField(default=True)
    def __str__ (self):
        return f"Campaña {self.nombre}, Inicio: {self.fecha_inicio}, Fin: {self.fecha_fin}"