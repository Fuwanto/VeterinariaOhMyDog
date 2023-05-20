from django.shortcuts import render

from OhMyDog.modelos.clientes import listar_clientes


def todos_los_clientes(request):
    clientes = listar_clientes()
    return render(request, "test.html", {"clientes": clientes})
