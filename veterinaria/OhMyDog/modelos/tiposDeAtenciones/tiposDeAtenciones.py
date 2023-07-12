from django.db import models


class TipoDeAtencion(models.Model):
    class Meta:
        verbose_name_plural = "(LT) Tipos_atencion"

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}" f"{self.nombre}"
