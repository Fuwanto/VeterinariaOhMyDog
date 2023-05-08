from django.contrib import admin
from OhMyDog.modelos.clientes.clientes import Cliente
from OhMyDog.modelos.estadosDelTurno.estadosDelTurno import EstadoDelTurno
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.turnos.turnos import Turno

# Register your models here.

admin.site.register(Cliente)
admin.site.register(EstadoDelTurno)
admin.site.register(FranjaHoraria)
admin.site.register(TipoDeAtencion)
admin.site.register(Turno)
