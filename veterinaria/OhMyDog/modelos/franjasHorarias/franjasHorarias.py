from django.db import models


class FranjaHoraria(models.Model):
    class Meta:
        verbose_name_plural = "(LT) Franjas_horarias"

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}" f"{self.nombre}"
