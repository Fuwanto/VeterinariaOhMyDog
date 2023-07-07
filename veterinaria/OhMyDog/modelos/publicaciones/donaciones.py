from django.db import models


class Donacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    objetivo = models.TextField(null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activa = models.BooleanField(default=True)
    monto_objetivo = models.DecimalField(max_digits=10, decimal_places=2)
    monto_recaudado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cantidad_donaciones = models.IntegerField(default=0)
    def __str__ (self):
        return f"{self.id} Campaña {self.nombre}, Inicio: {self.fecha_inicio}, Fin: {self.fecha_fin}"
    

class Transaccion(models.Model):
    transaccion_id = models.IntegerField(primary_key=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    campania = models.ForeignKey(Donacion,null=False, on_delete=models.CASCADE)
    finalizada = models.BooleanField(default=False)
    def __str__ (self):
        return f"{self.transaccion_id}, {self.monto}, {self.campania.nombre}"

class Descuento(models.Model):
    mail = models.EmailField(unique=True)