from django.shortcuts import get_object_or_404
from OhMyDog.modelos.publicaciones.adopciones import Adopcion, UsuarioInteresaAdopcion
from OhMyDog.modelos.clientes.clientes import Cliente
from OhMyDog.modelos.publicaciones.busquedas import Busqueda, UsuarioTieneInformacionBusqueda
from OhMyDog.modelos.tamaniosPerros.tamaniosPerros import TamanioPerro
from OhMyDog.modelos.etapaVidaPerro.etapaVidaPerro import EtapaVidaPerro
from OhMyDog.modelos.publicaciones.paseadores_cuidadores import PaseadorCuidador


"""
        ADOPCIONES
"""


def filtrar_adopciones_por_cliente(cliente):
    return Adopcion.objects.filter(cliente=cliente)


def buscar_adopcion_por_nombre_y_cliente(cliente, nombre):
    try:
        return Adopcion.objects.get(cliente=cliente, nombre=nombre)
    except:
        return None


def agregar_adopcion(cliente, nombre, descripcion, tamanio_perro_id, etapa_vida_perro_id, sexo, castrado):
    tamanio_perro = TamanioPerro.objects.get(id=tamanio_perro_id)
    etapa_vida_perro = EtapaVidaPerro.objects.get(id=etapa_vida_perro_id)
    adopcion = Adopcion(
        cliente=cliente,
        nombre=nombre,
        descripcion=descripcion,
        tamanio_perro=tamanio_perro,
        etapa_vida_perro=etapa_vida_perro,
        sexo=sexo,
        castrado=castrado,
    )
    adopcion.save()
    return adopcion


def listar_todas_adopciones():
    return Adopcion.objects.all()


def listar_adopciones_no_mias(cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return Adopcion.objects.exclude(cliente=cliente)


def adoptar(adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)
    adopcion.adoptado = True
    adopcion.save()


def eliminar_publicacion_adopcion(adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)
    adopcion.delete()

def usuario_tiene_interes_adopcion(adopcion, cliente):
    try:
        return UsuarioInteresaAdopcion.objects.get(adopcion=adopcion, cliente=cliente)
    except UsuarioInteresaAdopcion.DoesNotExist:
        return None
    
def agregar_usuario_interesa(adopcion_id, cliente):
    adopcion = Adopcion.objects.get(id = adopcion_id)
    usuario_interesa_adopcion = UsuarioInteresaAdopcion (adopcion = adopcion,cliente=cliente)
    usuario_interesa_adopcion.save()
"""
        BUSQUEDAS
"""


def agregar_busqueda(cliente, nombre, descripcion, zona, foto):
    busqueda = Busqueda(
        cliente=cliente,
        nombre=nombre,
        descripcion=descripcion,
        zona=zona,
        foto=foto,
    )
    busqueda.save()
    return busqueda


def filtrar_busquedas_por_cliente(cliente):
    return Busqueda.objects.filter(cliente=cliente)


def listar_busquedas_por_zona(zona):
    return Busqueda.objects.filter(zona__icontains=zona)


def listar_busquedas_no_mias_y_por_zona(cliente_id, zona):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return Busqueda.objects.filter(zona__icontains=zona).exclude(cliente=cliente)


def eliminar_publicacion_busqueda(busqueda_id):
    busqueda = get_object_or_404(Busqueda, id=busqueda_id)
    busqueda.delete()


def se_encontro(busqueda_id):
    busqueda = get_object_or_404(Busqueda, id=busqueda_id)
    busqueda.encontrado = True
    busqueda.save()


def buscar_busqueda_por_nombre_archivo_y_cliente(cliente, nombre_archivo):
    try:
        return Busqueda.objects.get(cliente=cliente, foto__contains=nombre_archivo)
    except:
        return None

def usuario_tiene_informacion_busqueda (busqueda, cliente):
    try:
        return UsuarioTieneInformacionBusqueda.objects.get(busqueda= busqueda, cliente=cliente)
    except UsuarioTieneInformacionBusqueda.DoesNotExist:
        return None
    
def agregar_usuario_tiene_informacion_busqueda (busquedaId, cliente):
    busqueda = Busqueda.objects.get(id = busquedaId)
    usuario_busqueda = UsuarioTieneInformacionBusqueda(busqueda=busqueda, cliente= cliente)
    usuario_busqueda.save()

"""
        PASEADORES | Cuidadores
"""


def todos_los_paseadores():
    return PaseadorCuidador.objects.filter(tipo="P")


def todos_los_cuidadores():
    return PaseadorCuidador.objects.filter(tipo="C")


def agregar_paseador_cuidador(nombre, email, latitud, longitud, franja_horaria, tipo):
    paseador_cuidador = PaseadorCuidador(
        nombre=nombre, email=email, latitud=latitud, longitud=longitud, franja_horaria=franja_horaria, tipo=tipo
    )
    paseador_cuidador.save()
    return


def buscar_paseador_cuidador_por_email(email):
    try:
        return PaseadorCuidador.objects.get(email=email)
    except:
        return None


def existe_paseador_cuidador_mail(email):
    try:
        paseador_cuidador = PaseadorCuidador.objects.get(email=email)
        return True
    except:
        return False


def eliminar_paseador_cuidador(paseador_cuidador_id):
    paseador_cuidador = get_object_or_404(PaseadorCuidador, id=paseador_cuidador_id)
    paseador_cuidador.delete()
