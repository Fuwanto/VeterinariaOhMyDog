from django.db.models.query_utils import *  #  incluye funciones útiles para consultas de bases de datos en Django.
from django.shortcuts import render, redirect, get_object_or_404
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


def buscar_perro_por_nombre(nombre, dueño):
    try:
        return Perro.objects.get(nombre=nombre, dueño=dueño)
    except:
        return None


def buscar_perro_por_id(perro_id):
    print("Como un camion", perro_id)
    return get_object_or_404(Perro, id=perro_id)


def deshabilitar_perro(id):
    perro = Perro.objects.get(id=id)
    perro.habilitado = False
    perro.save()
    return perro
