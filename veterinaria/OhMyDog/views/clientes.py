from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from OhMyDog.modelos.clientes import listar_clientes


def todos_los_clientes(request):
    clientes = listar_clientes()
    return render(request, "test.html", {"clientes": clientes})

@login_required
def mis_datos(request):
    return render(request, "mis_datos.html", {"cliente": request.user.cliente})

@login_required
def mis_perros(request):
    return render(request, "mis_perros.html", {"cliente": request.user.cliente})

@login_required
def mis_turnos(request):
    return render(request, "mis_turnos.html", {"cliente": request.user.cliente})