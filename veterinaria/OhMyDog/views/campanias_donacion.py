from django.shortcuts import render, redirect
from django.contrib import messages
from OhMyDog.modelos.publicaciones import (
    crear_campania,
    listar_campanias_de_donaciones_actualizadas,
    terminar_campania,
    obtener_campania_por_id,
    actualizar_fecha_fin_campania,
    existe_donacion_nombre,
)

from OhMyDog.views.utils import agregar_mensaje_error
from datetime import datetime, date, timedelta


def agregar_campania_donacion(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        objetivo = request.POST.get("objetivo")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        monto = request.POST.get("monto")
        if fecha_fin <= fecha_inicio:
            agregar_mensaje_error(request, f"La fecha de fin no puede ser anterior o igual a la fecha de inicio.")
            return redirect("agregar_campania_donacion")

        if existe_donacion_nombre(nombre):
            agregar_mensaje_error(request, f"Campaña con nombre: {nombre}, ya creada.")
            return redirect("agregar_campania_donacion")

        crear_campania(nombre, objetivo, monto, fecha_inicio, fecha_fin)
        messages.success(request, "Campaña agregada con exito.")
        return redirect("home")
    else:
        mañana = date.today() + timedelta(days=1)
        context = {
            "mañana": mañana.strftime("%Y-%m-%d"),
        }
        return render(request, "agregar_campania_donacion.html", context)


def listar_campanias_de_donaciones(request):
    return render(
        request, "listar_campanias_de_donaciones.html", {"campanias": listar_campanias_de_donaciones_actualizadas()}
    )


def terminar_campania_donacion(request, campania_id):
    terminar_campania(campania_id)
    return redirect("listar_campanias_de_donaciones")


def modificar_fecha_fin_campania(request):
    campania_id = request.POST.get("campania_id")
    nueva_fecha_fin_str = request.POST.get("nueva_fecha_fin")
    nueva_fecha_fin = datetime.datetime.strptime(nueva_fecha_fin_str, "%Y-%m-%d").date()
    campania = obtener_campania_por_id(campania_id)
    if nueva_fecha_fin <= campania.fecha_inicio:
        agregar_mensaje_error(request, f"La fecha de fin no puede ser anterior o igual a la fecha de inicio.")
        return redirect("listar_campanias_de_donaciones")

    actualizar_fecha_fin_campania(campania_id, nueva_fecha_fin)
    messages.success(request, "Fecha de fin de la campaña modificada con éxito.")
    return redirect("listar_campanias_de_donaciones")
