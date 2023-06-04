from django.db.models.query_utils import *  #  incluye funciones útiles para consultas de bases de datos en Django.

from OhMyDog.modelos.clientes.clientes import Cliente
from OhMyDog.modelos.perros import buscar_perros_por_dueño


def agregar_cliente(nombre, email, telefono):
    cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
    cliente.save()
    return cliente


def buscar_cliente_por_mail(email):
    try:
        return Cliente.objects.get(email=email)
    except:
        return None


def deshabilitar_cliente(id):
    cliente = Cliente.objects.get(id=id)
    cliente.habilitado = False
    cliente.save()
    return cliente


def modificar_cliente():
    pass


def buscar_cliente_por():
    pass


def listar_clientes_habilitados():
    return Cliente.objects.filter(habilitado=True)


def listar_clientes():
    return Cliente.objects.all()


def listar_perros_cliente(cliente):
    return buscar_perros_por_dueño(cliente)


def perros_cliente(id):
    cliente = Cliente.objects.get(id=id)
    return cliente.perros.all()
