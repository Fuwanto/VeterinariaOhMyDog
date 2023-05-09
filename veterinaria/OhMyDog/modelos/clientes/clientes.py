from django.db import models

# Create your models here.


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)  # autoincremental
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    telefono = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return f"Cliente con id {self.id} y email {self.email}"
