from django.db.models.query_utils import *  #  incluye funciones útiles para consultas de bases de datos en Django.

from OhMyDog.modelos.clientes.clientes import Cliente


def agregar_cliente(nombre, email, telefono):
    cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
    cliente.save()
    return cliente


def buscar_cliente_por_mail(email):
    try:
        return Cliente.objects.get(email=email)
    except:
        return None


def borrar_cliente():
    pass


def modificar_cliente():
    pass


def buscar_cliente_por():
    pass


def listar_clientes():
    return Cliente.objects.all()
