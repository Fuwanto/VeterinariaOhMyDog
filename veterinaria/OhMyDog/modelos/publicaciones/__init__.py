from django.shortcuts import get_object_or_404
from OhMyDog.modelos.publicaciones.adopciones import Adopcion
from OhMyDog.modelos.publicaciones.busquedas import Busqueda
from OhMyDog.modelos.tamaniosPerros.tamaniosPerros import TamanioPerro
from OhMyDog.modelos.etapaVidaPerro.etapaVidaPerro import EtapaVidaPerro

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


def listar_adopciones():
    return Adopcion.objects.all()


def adoptar(adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)
    adopcion.adoptado = True
    adopcion.save()


def eliminar_publicacion_adopcion(adopcion_id):
    adopcion = get_object_or_404(Adopcion, id=adopcion_id)
    adopcion.delete()


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


def listar_busquedas():
    return Busqueda.objects.all()


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
