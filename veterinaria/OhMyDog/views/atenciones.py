from django.shortcuts import render, redirect
from OhMyDog.modelos.perros import buscar_perro_por_id
from OhMyDog.modelos.atenciones import (
    crear_atencion_clinica,
    crear_consulta,
    crear_desparasitacion,
    crear_castracion,
    crear_vacunacion,
    buscar_atencion_por_id,
    buscar_vacunacion_por_atencion_id,
    buscar_desparasitacion_por_atencion_id,
)
from django.contrib import messages
from datetime import date
from decimal import Decimal
from OhMyDog.modelos.turnos import solicitar_turno_siguiente_vacunacion
from OhMyDog.modelos.publicaciones import utilizar_descuento


def crear_contexto(perro_id):
    return {"perro": buscar_perro_por_id(perro_id), "hoy": date.today().strftime("%Y-%m-%d")}


def agregar_atencion_clinica(request):
    if request.method == "GET":
        context = crear_contexto(request.GET.get("perro"))
        return render(request, "agregar_atencion_clinica.html", context)

    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        observacion = request.POST.get("observacion")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        crear_atencion_clinica(perro, fecha, observacion)
        utilizar_descuento(perro.dueño.email)
        messages.success(request, f"Atencion clinica registrada con exito. ")
        return redirect("home")


def agregar_consulta(request):
    if request.method == "GET":
        context = crear_contexto(request.GET.get("perro"))
        return render(request, "agregar_consulta.html", context)

    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        observacion = request.POST.get("observacion")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        crear_consulta(perro, fecha, observacion)
        utilizar_descuento(perro.dueño.email)
        messages.success(request, f"Consulta registrada con exito. ")
        return redirect("home")


def agregar_desparasitacion(request):
    if request.method == "GET":
        context = crear_contexto(request.GET.get("perro"))
        return render(request, "agregar_desparasitacion.html", context)

    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        diagnostico = request.POST.get("diagnostico")
        farmaco = request.POST.get("farmaco")
        fabricante = request.POST.get("fabricante")
        num_serie = request.POST.get("serie")
        num_lote = request.POST.get("lote")
        dosis = request.POST.get("dosis")
        observacion = request.POST.get("observacion")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        crear_desparasitacion(perro, fecha, diagnostico, farmaco, fabricante, num_serie, num_lote, dosis, observacion)
        utilizar_descuento(perro.dueño.email)
        messages.success(request, f"Desparasitación registrada con exito. ")
        return redirect("home")


def agregar_castracion(request):
    if request.method == "GET":
        context = crear_contexto(request.GET.get("perro"))
        return render(request, "agregar_castracion.html", context)

    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        observacion = request.POST.get("observacion")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        crear_castracion(perro, fecha, observacion)
        utilizar_descuento(perro.dueño.email)
        messages.success(request, f"Castracion registrada con exito. ")
        return redirect("home")


def agregar_vacunacion(request):
    if request.method == "GET":
        context = crear_contexto(request.GET.get("perro"))
        return render(request, "agregar_vacunacion.html", context)

    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        vacuna = request.POST.get("vacuna")
        fabricante = request.POST.get("fabricante")
        num_serie = request.POST.get("serie")
        num_lote = request.POST.get("lote")
        dosis = request.POST.get("dosis")
        dosis = Decimal(dosis).quantize(Decimal("0.00"))
        observaciones = request.POST.get("observaciones")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        solicitar_turno_siguiente_vacunacion(perro, vacuna, fecha)
        utilizar_descuento(perro.dueño.email)
        crear_vacunacion(perro, fecha, vacuna, fabricante, num_serie, num_lote, dosis, observaciones)
        messages.success(request, f"Vacunacion registrada con exito. ")
        return redirect("home")


def mostrar_datos_atencion(request):
    atencion_id = request.POST.get("atencion_id")
    observaciones = request.POST.get("observaciones")
    atencion = buscar_atencion_por_id(atencion_id)
    vacunacion = buscar_vacunacion_por_atencion_id(atencion_id)
    desparasitacion = buscar_desparasitacion_por_atencion_id(atencion_id)
    if observaciones is not None:
        atencion.observacion = observaciones
        atencion.save()
    context = {
        "atencion": atencion,
        "vacunacion": vacunacion,
        "desparasitacion": desparasitacion,
    }
    return render(request, f"{atencion.url_mostrar_datos}.html", context)
