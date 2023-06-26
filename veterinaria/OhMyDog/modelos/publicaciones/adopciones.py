from django.db import models

from OhMyDog.modelos.clientes.clientes import Cliente
from OhMyDog.modelos.tamaniosPerros.tamaniosPerros import TamanioPerro
from OhMyDog.modelos.etapaVidaPerro.etapaVidaPerro import EtapaVidaPerro

class Adopcion(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente, null=False, on_delete=models.CASCADE
    )
    descripcion = models.TextField(null=True)
    nombre = models.CharField(max_length=30)
    tamanio_perro = models.ForeignKey(
        TamanioPerro, null=False, on_delete=models.CASCADE
    )
    etapa_vida_perro = models.ForeignKey(
        EtapaVidaPerro, null=False, on_delete=models.CASCADE
    )
    sexos = [("M", "Macho"), ("H", "Hembra")]
    sexo = models.CharField(max_length=1, choices=sexos, blank=False)
    castrado = models.CharField(max_length=1, choices=[("S", "Si"), ("N", "No")], blank=False)
    adoptado = models.BooleanField(default=False)
    


    def __str__(self):
        return f"Cliente: {self.cliente_id}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, {self.tamanio_perro.id}, Tamaño del perro: {self.tamanio_perro.id}, Etapa de vida del perro: {self.etapa_vida_perro}, Sexo: {self.sexo}, Castrado: {self.castrado}"
    
class UsuarioInteresaAdopcion(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente, null=False, on_delete=models.CASCADE
    )
    adopcion = models.ForeignKey(
        Adopcion, null=False, on_delete=models.CASCADE
    )