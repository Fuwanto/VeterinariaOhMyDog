from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from OhMyDog.modelos.clientes import (
    listar_clientes,
    Cliente,
    deshabilitar_cliente,
    perros_cliente,
    perros_habilitados_cliente,
    buscar_clientes_contienen_mail,
)
from OhMyDog.modelos.perros import (
    buscar_perro_por_nombre_y_dueño,
    registrar_perro,
    Perro,
    deshabilitar_perro,
)
from OhMyDog.views.auth import user_passes_test, superuser_check
from django.contrib import messages
from OhMyDog.modelos.turnos import filtrar_turnos_por_cliente
from datetime import date
from decimal import Decimal
from OhMyDog.models import modificar_mail
from OhMyDog.views.utils import agregar_mensaje_error


def buscar_clientes(request):
    email = request.GET.get("email", "")
    clientes = buscar_clientes_contienen_mail(email)
    return render(request, "listado_clientes.html", {"clientes": clientes})


def todos_los_clientes(request):
    clientes = listar_clientes()
    return render(request, "listado_clientes.html", {"clientes": clientes})


@login_required
def mis_datos(request):
    cliente = request.user.cliente
    if request.method == "POST":
        email = request.POST.get("email")
        nombre = request.POST.get("nombre")
        telefono = request.POST.get("telefono")
        if cliente.email == email:
            cliente.nombre = nombre
            cliente.telefono = telefono
            cliente.save()
            messages.success(request, f"Datos modificados correctamente")
            return redirect("mis_datos")
        else:
            try:
                cliente = Cliente.objects.get(email=email)
                agregar_mensaje_error(
                    request, "El mail ingresado ya se encuentra registrado."
                )
                return redirect("mis_datos")
            except cliente.DoesNotExist:
                modificar_mail(email, request.user.cliente)
                cliente.nombre = nombre
                cliente.telefono = telefono
                cliente.email = email
                cliente.save()
                messages.success(request, f"Datos modificados correctamente")
                return redirect("mis_datos")

    return render(request, "mis_datos.html", {"cliente": request.user.cliente})


@user_passes_test(superuser_check)
def datos_de_un_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, "datos_de_un_cliente.html", {"cliente": cliente})


@user_passes_test(superuser_check)
def listado_de_perros_cliente(request, cliente_id):
    perros = perros_cliente(cliente_id)
    return render(request, "listado_de_perros_cliente.html", {"perros": perros})


@user_passes_test(superuser_check)
def agregar_perro(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == "POST":
        nombre = request.POST.get("nombre_perro")
        raza = request.POST.get("raza")
        peso = request.POST.get("peso")
        peso = Decimal(peso).quantize(Decimal("0.00"))
        sexo = request.POST.get("sexo")
        fecha_de_nacimiento = request.POST.get("fecha_de_nacimiento")
        descripcion = request.POST.get("descripcion")

        perro = buscar_perro_por_nombre_y_dueño(nombre, cliente)

        if perro is None:
            registrar_perro(
                cliente, nombre, raza, peso, descripcion, fecha_de_nacimiento, sexo
            )
            messages.success(request, "Perro registrado con exito.")
            return redirect("home")
        else:
            agregar_mensaje_error(request, f"Perro {nombre} ya registrado.")
            return redirect(f"/clientes/{cliente.id}/agregar_perro")
    else:
        return render(
            request,
            "agregar_perro.html",
            {"cliente_id": cliente_id, "hoy": date.today().isoformat()},
        )


@user_passes_test(superuser_check)
def borrar_perro(request, perro_id):
    deshabilitar_perro(perro_id)
    messages.success(request, "Perro eliminado con exito.")
    return redirect("clientes")


@user_passes_test(superuser_check)
def borrar_cliente(request, cliente_id):
    deshabilitar_cliente(cliente_id)
    messages.success(request, "Cliente eliminado con exito")
    return redirect("clientes")


@login_required
def mis_perros(request):
    perros = perros_habilitados_cliente(request.user.cliente.id)
    return render(request, "mis_perros.html", {"perros": perros})


@login_required
def mis_turnos(request):
    cliente = request.user.cliente
    turnos = filtrar_turnos_por_cliente(cliente)
    return render(request, "mis_turnos.html", {"turnos": turnos})


@login_required
def datos_de_mi_perro(request, perro_id):
    perro = get_object_or_404(Perro, id=perro_id)
    return render(request, "datos_de_mi_perro.html", {"perro": perro})
