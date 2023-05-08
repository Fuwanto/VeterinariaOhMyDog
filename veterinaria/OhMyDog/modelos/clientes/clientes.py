from django.db import models

# Create your models here.

class Clientes (models.Model):
    id = models.BigAutoField(primary_key=True)   # autoincremental 
    nombre = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefono = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return f"Cliente con id {self.id} y email {self.email}"
    