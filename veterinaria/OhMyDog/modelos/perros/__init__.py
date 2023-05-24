from django.db.models.query_utils import *  #  incluye funciones útiles para consultas de bases de datos en Django.

from OhMyDog.modelos.perros.perros import Perro


def registrar_perro(dueño, nombre, raza, peso, descripcion, fecha_de_nacimiento, sexo):
    perro = Perro(dueño=dueño, nombre=nombre, raza=raza, peso=peso, descripcion=descripcion, 
                  fecha_de_nacimiento=fecha_de_nacimiento, sexo=sexo)
    perro.save()
    return perro


def buscar_perros_por_dueño(dueño):
    return Perro.objects.filter(dueño=dueño)

def buscar_perro_por_nombre(nombre, cliente):
    try:
        perros = buscar_perros_por_dueño(cliente)
        return perros.objects.filter(nombre__icontains=nombre)
    except:
        return None