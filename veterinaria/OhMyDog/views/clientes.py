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
from OhMyDog.modelos.tamaniosPerros.tamaniosPerros import TamanioPerro
from OhMyDog.modelos.etapaVidaPerro.etapaVidaPerro import EtapaVidaPerro
from OhMyDog.modelos.publicaciones.adopciones import Adopcion
from OhMyDog.modelos.publicaciones import (
    filtrar_adopciones_por_cliente, agregar_adopcion, buscar_adopcion_por_nombre_y_cliente,
    listar_adopciones
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


@login_required
def agregar_publicacion_adopcion(request):
    tamanios_perro = TamanioPerro.objects.all()
    etapas_vida_perro = EtapaVidaPerro.objects.all()
    cliente = request.user.cliente
    context = {"tamanios": tamanios_perro, "etapas": etapas_vida_perro}
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        tamanio_perro_id = request.POST.get("tamanio_perro_id")
        etapa_vida_perro_id = request.POST.get("etapa_vida_perro_id")
        sexo = request.POST.get("sexo")
        castrado = request.POST.get("castrado")
        
        publicacion = buscar_adopcion_por_nombre_y_cliente(cliente, nombre)
        
        if publicacion is None:
            agregar_adopcion(
               cliente, nombre, descripcion, tamanio_perro_id, etapa_vida_perro_id, sexo, castrado
            )
            messages.success(request, "Publicacion agregada con exito.")
            return redirect("mis_adopciones")
        else:
            agregar_mensaje_error(request, f"Publicacion con nombre: {nombre}, ya publicada.")
            return redirect("agregar_publicacion_adopcion")
    else:
        return render(
            request,
            "agregar_publicacion_adopcion.html", context
        )

@login_required
def listar_publicaciones_de_adopciones(request):
    adopciones = listar_adopciones()
    return render(request, "listar_publicaciones_de_adopciones.html", {"adopciones": adopciones})
    
@login_required
def mis_adopciones(request):
    cliente = request.user.cliente
    adopciones = filtrar_adopciones_por_cliente(cliente)
    return render(request, "mis_adopciones.html", {"adopciones": adopciones})    