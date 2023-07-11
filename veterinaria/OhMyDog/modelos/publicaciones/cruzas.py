from django.db import models
from OhMyDog.modelos.clientes.clientes import Cliente
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


class Cruza(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE, related_name="cruzas")
    nombre = models.CharField(max_length=30)
    sexos = [("M", "Macho"), ("H", "Hembra")]
    sexo = models.CharField(max_length=1, choices=sexos, blank=False)
    raza = models.TextField()
    edad_meses = models.IntegerField()
    peso = models.DecimalField(blank=False, max_digits=5, decimal_places=2)
    color = models.CharField(max_length=30)
    antecedentes_salud = models.TextField(null=True)
    foto = models.ImageField(upload_to="fotos/")
    intereses = models.ManyToManyField("self", blank=True, symmetrical=False)
    ultimo_celo = models.DateField(blank=True, null=True)


def __str__(self):
    return f"Cliente: {self.cliente}, Nombre de perro: {self.nombre}"


@receiver(pre_delete, sender=Cruza)
def borrar_foto(sender, instance, **kwargs):
    if instance.foto:
        path_foto = instance.foto.path
        if os.path.exists(path_foto):
            os.remove(path_foto)
