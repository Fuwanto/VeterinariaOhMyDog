from django.db import models
from OhMyDog.modelos.clientes.clientes import Cliente
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os


class Busqueda(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(null=True)
    zona = models.TextField()
    encontrado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to="fotos/")

    def __str__(self):
        return f"Cliente: {self.cliente_id}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, Zona: {self.zona}"


@receiver(pre_delete, sender=Busqueda)
def borrar_foto(sender, instance, **kwargs):
    if instance.foto:
        path_foto = instance.foto.path
        if os.path.exists(path_foto):
            os.remove(path_foto)

class UsuarioTieneInformacionBusqueda (models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, null=False, on_delete=models.CASCADE)
    busqueda = models.ForeignKey(Busqueda, null=False, on_delete=models.CASCADE)
