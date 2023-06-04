from django.db import models

from OhMyDog.modelos.clientes.clientes import Cliente


class Perro(models.Model):
    id = models.BigAutoField(primary_key=True)
    dueño = models.ForeignKey(
        Cliente, null=False, on_delete=models.CASCADE, related_name="perros"
    )
    nombre = models.CharField(max_length=35, blank=False)
    raza = models.CharField(max_length=255, blank=False)
    peso = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    fecha_de_nacimiento = models.DateField(blank=False)
    sexos = [("M", "Macho"), ("H", "Hembra")]
    sexo = models.CharField(max_length=1, choices=sexos, blank=False)
    habilitado = models.BooleanField(default=True)
    tiene_castracion = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}, Dueño: {self.dueño}"
