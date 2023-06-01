from django.db import models

class TipoDeDosisVacunacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre}"