from OhMyDog.modelos.publicaciones.adopciones import Adopcion
from OhMyDog.modelos.tamaniosPerros.tamaniosPerros import TamanioPerro
from OhMyDog.modelos.etapaVidaPerro.etapaVidaPerro import EtapaVidaPerro


def filtrar_adopciones_por_cliente(cliente):
    return Adopcion.objects.filter(cliente = cliente)

def buscar_adopcion_por_nombre_y_cliente(cliente, nombre):
    try:
        return Adopcion.objects.get(cliente=cliente, nombre=nombre)
    except:
        return None

def agregar_adopcion(cliente, nombre, descripcion, tamanio_perro_id, etapa_vida_perro_id, sexo, castrado):
    tamanio_perro = TamanioPerro.objects.get(id = tamanio_perro_id)
    etapa_vida_perro = EtapaVidaPerro.objects.get(id = etapa_vida_perro_id)
    adopcion = Adopcion(
        cliente=cliente,
        nombre=nombre,
        descripcion=descripcion,
        tamanio_perro=tamanio_perro,
        etapa_vida_perro=etapa_vida_perro,
        sexo=sexo,
        castrado=castrado
    )
    adopcion.save()
    return adopcion

def listar_adopciones():
    return Adopcion.objects.all()