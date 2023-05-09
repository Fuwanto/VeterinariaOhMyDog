from OhMyDog.modelos.clientes.clientes import Cliente
from django.db.models.query_utils import * #  incluye funciones útiles para consultas de bases de datos en Django.


def agregar_cliente(nombre, email, telefono, contraseña):
    cliente = Cliente(
        nombre=nombre, email=email, telefono=telefono, contraseña=contraseña
    )
    cliente.save()
    return cliente

def comprobar_que_no_exista(email):
    return Cliente.objects.get(email=email)# si no existe retorna None

def borrar_cliente():
    pass


def modificar_cliente():
    pass


def buscar_cliente_por():
    pass


def listar_clientes():
    return Cliente.objects.all()
