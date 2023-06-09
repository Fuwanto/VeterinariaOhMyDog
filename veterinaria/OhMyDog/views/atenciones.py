from django.shortcuts import render, redirect, get_object_or_404
from OhMyDog.modelos.perros import buscar_perro_por_id
from OhMyDog.modelos.atenciones import (
    agregar_atencion_clinica_init,
    agregar_consulta_init,
    agregar_desparacitacion_init,
    agregar_castracion_init,
    agregar_vacunacion_init,
)
from datetime import datetime, date
from OhMyDog.modelos.tiposDeDosisVacunacion.tiposDeDosisVacunacion import (
    TipoDeDosisVacunacion,
)
from django.contrib import messages
from OhMyDog.modelos.atenciones.atenciones import Atencion

def agregar_atencion_clinica(request):
    perro = None
    perro_id = None
    if request.method == "GET":
        perro_id = request.GET.get("perro")
        perro = buscar_perro_por_id(perro_id)
    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        observacion = request.POST.get("observacion")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        agregar_atencion_clinica_init(perro, fecha, observacion)
        messages.success(request, f"Atencion clinica registrada con exito. ")

    context = {"perro": perro}
    return render(request, "agregar_atencion_clinica.html", context)


def agregar_consulta(request):
    perro = None
    perro_id = None
    if request.method == "GET":
        perro_id = request.GET.get("perro")
        perro = buscar_perro_por_id(perro_id)
    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        observacion = request.POST.get("observacion")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        agregar_consulta_init(perro, fecha, observacion)
        messages.success(request, f"Consulta registrada con exito. ")

    context = {"perro": perro}
    return render(request, "agregar_consulta.html", context)


def agregar_desparacitacion(request):
    perro = None
    perro_id = None
    if request.method == "GET":
        perro_id = request.GET.get("perro")
        perro = buscar_perro_por_id(perro_id)
    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        parasito = request.POST.get("parasito")
        farmaco = request.POST.get("farmaco")
        dosis = request.POST.get("dosis")
        observacion = request.POST.get("observacion")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        agregar_desparacitacion_init(perro, fecha, parasito, farmaco, dosis, observacion)
        messages.success(request, f"Desparacitacion registrada con exito. ")

    context = {"perro": perro}
    return render(request, "agregar_desparacitacion.html", context)


def agregar_castracion(request):
    perro = None
    perro_id = None
    if request.method == "GET":
        perro_id = request.GET.get("perro")
        perro = buscar_perro_por_id(perro_id)
    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        observacion = request.POST.get("observacion")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        agregar_castracion_init(perro, fecha, observacion)
        messages.success(request, f"Castracion registrada con exito. ")

    context = {"perro": perro}
    return render(request, "agregar_castracion.html", context)


def agregar_vacunacion(request):
    perro = None
    perro_id = None
    tipo_dosis = TipoDeDosisVacunacion.objects.all()
    if request.method == "GET":
        perro_id = request.GET.get("perro")
        perro = buscar_perro_por_id(perro_id)
    if request.method == "POST":
        fecha = request.POST.get("fecha_de_atencion")
        observacion = request.POST.get("observacion")
        dosis = request.POST.get("dosis")
        vacuna = request.POST.get("vacuna")
        perro_id = request.POST.get("perro")
        perro = buscar_perro_por_id(perro_id)
        agregar_vacunacion_init(perro, fecha, vacuna, dosis, observacion)
        messages.success(request, f"Vacunacion registrada con exito. ")

    context = {"perro": perro, "tipo_dosis": tipo_dosis}
    return render(request, "agregar_vacunacion.html", context)

