from django.db import models

class EstadoDelTurno (models.Model)
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)