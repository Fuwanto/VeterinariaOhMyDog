from django.db import models

class PaseadorCuidador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    latitud = models.TextField()
    longitud = models.TextField()
    franja_horaria = models.CharField(max_length=255)
    tipos = [("P", "Paseador"), ("C", "Cuidador")]
    tipo = models.CharField(max_length=1, choices=tipos, blank=False)

    def __str__(self):
        return f"Trabajador con id: {self.id}, tipo: {self.tipo} email: {self.email}, nombre:{self.nombre}, coodenadas: {self.latitud} | {self.longitud}"