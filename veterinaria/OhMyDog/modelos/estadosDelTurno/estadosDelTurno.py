from django.db import models


class EstadoDelTurno(models.Model):
    class Meta:
        verbose_name_plural = "(LT) Estados_del_turno"

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id},{self.nombre}"
