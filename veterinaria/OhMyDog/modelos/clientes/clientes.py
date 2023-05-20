from django.db import models


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    telefono = models.CharField(max_length=20)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"Cliente con id {self.id} y email {self.email}"
