from django.db import models


class TamanioPerro(models.Model):
    class Meta:
        verbose_name_plural = "(LT) Tamaños_perro"

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id},{self.nombre}"
