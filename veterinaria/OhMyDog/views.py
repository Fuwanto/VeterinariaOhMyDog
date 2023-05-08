from django.shortcuts import render

from .modelos.clientes import agregar_cliente
from .modelos.clientes import listar_clientes


def home(request):
    nombre = "nombre"
    email = "email@gmail.com"
    telefono = "telefono"
    contraseña = "contraseña"
    agregar_cliente(nombre, email, telefono, contraseña)

    return render(request, "home.html")


def test_view(request):
    clientes = listar_clientes()
    return render(request, "test.html", {"clientes": clientes})
