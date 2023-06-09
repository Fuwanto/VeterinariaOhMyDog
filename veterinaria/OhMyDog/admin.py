from django.contrib import admin

from OhMyDog.modelos.clientes.clientes import Cliente
from OhMyDog.modelos.estadosDelTurno.estadosDelTurno import EstadoDelTurno
from OhMyDog.modelos.franjasHorarias.franjasHorarias import FranjaHoraria
from OhMyDog.modelos.perros.perros import Perro
from OhMyDog.modelos.tiposDeAtenciones.tiposDeAtenciones import TipoDeAtencion
from OhMyDog.modelos.turnos.turnos import Turno
from OhMyDog.models import Usuario
from OhMyDog.modelos.atenciones.atenciones import Atencion
from OhMyDog.modelos.atenciones.desparacitacion import Desparacitacion
from OhMyDog.modelos.atenciones.vacunacion import Vacunacion
from OhMyDog.modelos.tamaniosPerros.tamaniosPerros import TamanioPerro
from OhMyDog.modelos.etapaVidaPerro.etapaVidaPerro import EtapaVidaPerro
from OhMyDog.modelos.publicaciones.paseadores_cuidadores import PaseadorCuidador
from OhMyDog.modelos.publicaciones.busquedas import Busqueda, UsuarioTieneInformacionBusqueda
from OhMyDog.modelos.publicaciones.adopciones import Adopcion, UsuarioInteresaAdopcion
from OhMyDog.modelos.publicaciones.donaciones import Donacion, Transaccion, Descuento
from OhMyDog.modelos.publicaciones.cruzas import Cruza

admin.site.register(Cliente)
admin.site.register(EstadoDelTurno)
admin.site.register(FranjaHoraria)
admin.site.register(Perro)
admin.site.register(TipoDeAtencion)
admin.site.register(Turno)
admin.site.register(Usuario)
admin.site.register(Atencion)
admin.site.register(Desparacitacion)
admin.site.register(Vacunacion)
admin.site.register(TamanioPerro)
admin.site.register(EtapaVidaPerro)
admin.site.register(PaseadorCuidador)
admin.site.register(Busqueda)
admin.site.register(Adopcion)
admin.site.register(UsuarioInteresaAdopcion)
admin.site.register(UsuarioTieneInformacionBusqueda)
admin.site.register(Donacion)
admin.site.register(Cruza)
admin.site.register(Transaccion)
admin.site.register(Descuento)
