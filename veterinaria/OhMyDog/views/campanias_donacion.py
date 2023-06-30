from django.shortcuts import render, redirect
from django.contrib import messages
from OhMyDog.modelos.publicaciones import (
    buscar_campania_por_nombre,
    crear_campania,
    listar_campanias_de_donaciones_todas,
    terminar_campania
)

from OhMyDog.views.utils import agregar_mensaje_error
from datetime import datetime, date, timedelta

def agregar_campania_donacion(request):
    hoy = date.today()
    hoy = hoy + timedelta(days=1)
    context = {
        "min": hoy.strftime("%Y-%m-%d"),
    }
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        objetivo = request.POST.get("objetivo")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        monto = request.POST.get("monto")
        if fecha_fin <= fecha_inicio:
            agregar_mensaje_error(request, f"La fecha de fin no puede ser anterior o igual a la fecha de inicio.")
            return render(request, "agregar_campania_donacion.html")

        if buscar_campania_por_nombre(nombre) is None:
            crear_campania(nombre, objetivo, monto, fecha_inicio, fecha_fin)
            messages.success(request, "Campaña agregada con exito.")
            return redirect("home")
        else:
            agregar_mensaje_error(request, f"Campaña con nombre: {nombre}, ya creada.")
    return render(request, "agregar_campania_donacion.html", context)


def listar_campanias_de_donaciones(request):
    campanias = listar_campanias_de_donaciones_todas()
    hoy = date.today()
    hoy = hoy + timedelta(days=1)
    for campania in campanias:
        campania.progreso = (campania.monto_recaudado / campania.monto_objetivo) * 100
        if (campania.fecha_fin <= hoy):
            campania.activa = False
    context = {
        "campanias": campanias,
        "hoy": hoy,
    }
    return render(request, "listar_campanias_de_donaciones.html", context)

def terminar_campania_donacion (request, campania_id):
    print(campania_id)
    terminar_campania(campania_id)
    return redirect("listar_campanias_de_donaciones")