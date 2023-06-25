from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from OhMyDog.modelos.clientes import (
    deshabilitar_cliente,
    perros_cliente,
    perros_habilitados_cliente,
    buscar_clientes_contienen_mail,
    buscar_cliente_por_mail,
    buscar_cliente_por_id,
    cliente_tiene_perro,
)
from OhMyDog.modelos.perros import (
    registrar_perro as agregar_perro,
    deshabilitar_perro,
    buscar_perro_por_id,
)
from OhMyDog.views.auth import user_passes_test, superuser_check
from django.contrib import messages
from OhMyDog.modelos.turnos import filtrar_turnos_por_cliente
from datetime import date
from decimal import Decimal
from OhMyDog.models import modificar_mail
from OhMyDog.views.utils import agregar_mensaje_error


def listar_clientes(request):
    email = request.GET.get("email", "")
    clientes = buscar_clientes_contienen_mail(email)
    return render(request, "listado_clientes.html", {"clientes": clientes, "email": email})


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
            cliente = buscar_cliente_por_mail(email)
            if cliente is not None:
                agregar_mensaje_error(request, "El mail ingresado ya se encuentra registrado.")
                return redirect("mis_datos")
            else:
                cliente = request.user.cliente
                modificar_mail(email, cliente)
                cliente.nombre = nombre
                cliente.telefono = telefono
                cliente.email = email
                cliente.save()
                messages.success(request, f"Datos modificados correctamente")
                return redirect("mis_datos")

    return render(request, "mis_datos.html", {"cliente": request.user.cliente})


@user_passes_test(superuser_check)
def datos_de_un_cliente(request, cliente_id):
    cliente = buscar_cliente_por_id(cliente_id)
    return render(request, "datos_de_un_cliente.html", {"cliente": cliente})


@user_passes_test(superuser_check)
def listar_perros_cliente(request, cliente_id):
    perros = perros_cliente(cliente_id)
    return render(request, "listado_de_perros_cliente.html", {"perros": perros})


@user_passes_test(superuser_check)
def registrar_perro(request, cliente_id):
    if request.method == "POST":
        nombre = request.POST.get("nombre_perro")
        raza = request.POST.get("raza")
        peso = request.POST.get("peso")
        peso = Decimal(peso).quantize(Decimal("0.00"))
        sexo = request.POST.get("sexo")
        fecha_de_nacimiento = request.POST.get("fecha_de_nacimiento")
        descripcion = request.POST.get("descripcion")

        if not cliente_tiene_perro(cliente_id, nombre):
            agregar_perro(cliente_id, nombre, raza, peso, descripcion, fecha_de_nacimiento, sexo)
            messages.success(request, "Perro registrado con exito.")
            return redirect("home")
        else:
            agregar_mensaje_error(request, f"El cliente ya tiene un perro llamado {nombre}")
            return redirect(f"/clientes/{cliente_id}/registrar_perro")
    else:
        return render(
            request,
            "agregar_perro.html",
            {"cliente_id": cliente_id, "hoy": date.today().isoformat()},
        )


@user_passes_test(superuser_check)
def borrar_perro(request, perro_id):
    deshabilitar_perro(perro_id)
    messages.success(request, "Perro deshabilitado con éxito.")
    return redirect("clientes")


@user_passes_test(superuser_check)
def borrar_cliente(request, cliente_id):
    deshabilitar_cliente(cliente_id)
    messages.success(request, "Cliente deshabilitado con éxito.")
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
    perro = buscar_perro_por_id(perro_id)
    return render(request, "datos_de_mi_perro.html", {"perro": perro})
