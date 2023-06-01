from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from OhMyDog.modelos.clientes import (
    listar_clientes_habilitados,
    Cliente,
    deshabilitar_cliente,
    filtrar_clientes_email,
)
from OhMyDog.modelos.perros import (
    buscar_perros_por_dueño,
    buscar_perro_por_nombre,
    registrar_perro,
    Perro,
    deshabilitar_perro,
)
from OhMyDog.views.auth import user_passes_test, superuser_check
from django.contrib import messages
from OhMyDog.modelos.turnos import filtrar_turnos_por_cliente


def buscar_clientes_email(request):
    email = request.GET.get("email", "")
    clientes = filtrar_clientes_email(email)
    return render(request, "listado_clientes.html", {"clientes": clientes})


def todos_los_clientes(request):
    clientes = listar_clientes_habilitados()
    return render(request, "listado_clientes.html", {"clientes": clientes})


@login_required
def mis_datos(request):
    cliente = request.user.cliente

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        telefono = request.POST.get("telefono")

        # Actualizar los datos del cliente
        cliente.nombre = nombre
        cliente.telefono = telefono
        cliente.save()

        return redirect("mis_datos")

    return render(request, "mis_datos.html", {"cliente": request.user.cliente})


@user_passes_test(superuser_check)
def datos_de_un_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, "datos_de_un_cliente.html", {"cliente": cliente})


@user_passes_test(superuser_check)
def listado_de_perros_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    perros = buscar_perros_por_dueño(cliente)
    return render(request, "listado_de_perros_cliente.html", {"perros": perros})


@user_passes_test(superuser_check)
def agregar_perro(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        nombre = request.POST.get("nombre_perro")
        perro = buscar_perro_por_nombre(nombre, cliente)
        if nombre and perro is None:
            raza = request.POST.get("raza")
            peso = request.POST.get("peso")
            sexo = request.POST.get("sexo")
            fecha_de_nacimiento = request.POST.get("fecha_de_nacimiento")
            descripcion = request.POST.get("descripcion")
            print(nombre, raza, peso, sexo, fecha_de_nacimiento, descripcion)
            registrar_perro(
                cliente, nombre, raza, peso, descripcion, fecha_de_nacimiento, sexo
            )
            messages.success(request, "Perro registrado con exito.")
        else:
            messages.error(request, f"Perro {nombre} ya registrado.")
    else:
        messages.error(request, f"Perro  ya existente.")
    return render(request, "agregar_perro.html", {"cliente_id": cliente_id})


@user_passes_test(superuser_check)
def borrar_perro(request, perro_id):
    deshabilitar_perro(perro_id)
    return redirect("clientes")


@user_passes_test(superuser_check)
def borrar_cliente(request, cliente_id):
    deshabilitar_cliente(cliente_id)
    return redirect("clientes")


@login_required
def mis_perros(request):
    cliente = request.user.cliente
    perros = buscar_perros_por_dueño(cliente)
    return render(request, "mis_perros.html", {"perros": perros})


@login_required
def mis_turnos(request):
    cliente = request.user.cliente
    turnos = filtrar_turnos_por_cliente(cliente)
    return render(request, "mis_turnos.html", {"turnos": turnos})


@user_passes_test(superuser_check)
def datos_de_un_perro(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    peso = request.POST.get("peso")
    if request.method == "POST" and peso:
        descripcion = request.POST.get("descripcion")

        # Actualizar los datos del perro
        perro.peso = peso
        perro.descripcion = descripcion
        perro.save()

    return render(request, "datos_de_un_perro.html", {"perro": perro})


@login_required
def datos_de_mi_perro(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    return render(request, "datos_de_mi_perro.html", {"perro": perro})
