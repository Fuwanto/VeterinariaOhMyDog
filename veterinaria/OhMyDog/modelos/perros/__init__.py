from django.db.models.query_utils import *  #  incluye funciones útiles para consultas de bases de datos en Django.
from OhMyDog.modelos.perros.perros import Perro
from django.shortcuts import get_object_or_404
from OhMyDog.modelos.clientes.clientes import Cliente


def registrar_perro(dueño_id, nombre, raza, peso, descripcion, fecha_de_nacimiento, sexo):
    dueño = get_object_or_404(Cliente, id=dueño_id)
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
    return Perro.objects.filter(dueño=dueño)


def buscar_perro_por_nombre_y_dueño(nombre, dueño):
    try:
        return Perro.objects.get(nombre=nombre, dueño=dueño, habilitado=True)
    except:
        return None


def buscar_perros_por_dueño_habilitados(dueño):
    return Perro.objects.filter(dueño=dueño, habilitado=True)


def buscar_perro_por_id(id):
    perro = Perro.objects.get(id=id)
    return perro


def deshabilitar_perro(id):
    perro = Perro.objects.get(id=id)
    perro.habilitado = False
    perro.save()
    return perro


def modificar_tiene_castracion(id):
    perro = Perro.objects.get(id=id)
    perro.tiene_castracion = True
    perro.save()
    return perro


def modificar_datos(id, peso, descripcion):
    perro = Perro.objects.get(id=id)
    perro.peso = peso
    perro.descripcion = descripcion
    perro.save()
    return perro
