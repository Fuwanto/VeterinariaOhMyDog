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


def buscar_cliente_por_id(id):
    return Cliente.objects.get(id=id)


def buscar_clientes_contienen_mail(email):
    return Cliente.objects.filter(email__icontains=email)


def deshabilitar_cliente(id):
    cliente = Cliente.objects.get(id=id)
    cliente.habilitado = False
    cliente.usuario.habilitado = False
    cliente.usuario.save()
    cliente.save()
    return cliente


def listar_clientes_habilitados():
    return Cliente.objects.filter(habilitado=True)


def listar_clientes():
    return Cliente.objects.all()


def listar_perros_cliente(cliente):
    return buscar_perros_por_dueño(cliente)


def perros_cliente(id):
    cliente = Cliente.objects.get(id=id)
    return cliente.perros.all()


def perros_habilitados_cliente(id):
    cliente = Cliente.objects.get(id=id)
    return cliente.perros.filter(habilitado=True)


def cliente_tiene_perro(cliente_id, nombre_perro):
    cliente = buscar_cliente_por_id(cliente_id)
    return cliente.perros.filter(nombre=nombre_perro).exists()
