from django.db import models

from OhMyDog.modelos.clientes.clientes import Cliente


class Perro(models.Model):
    id = models.BigAutoField(primary_key=True)
    dueño = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=35, blank=False)
    raza = models.CharField(max_length=255, blank=False)
    peso = models.IntegerField(blank=False)
    descripcion = models.CharField(max_length=255)
    fecha_de_nacimiento = models.DateField(blank=False)
    sexos = [("M", "Macho"), ("H", "Hembra")]
    sexo = models.CharField(max_length=1, choices=sexos, blank=False)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}, Dueño: {self.dueño}"
