from django.db.models.query_utils import *  #  incluye funciones útiles para consultas de bases de datos en Django.

from OhMyDog.modelos.perros.perros import Perro


def registrar_perro(dueño, nombre, raza, peso, descripcion, fecha_de_nacimiento, sexo):
    perro = Perro(
        dueño=dueño,
        nombre=nombre,
        raza=raza,
        peso=peso,
        descripcion=descripcion,
        fecha_de_nacimiento=fecha_de_nacimiento,
        sexo=sexo,
    )
    perro.save()
    return perro


def buscar_perros_por_dueño(dueño):
    return Perro.objects.filter(dueño=dueño, habilitado=True)


def buscar_perro_por_nombre(nombre, cliente):
    try:
        return buscar_perros_por_dueño(cliente)
    except:
        return None


def deshabilitar_perro(id):
    perro = Perro.objects.get(id=id)
    perro.habilitado = False
    perro.save()
    return perro
