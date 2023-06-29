from django.shortcuts import render, redirect
from django.contrib import messages
from OhMyDog.modelos.publicaciones import (
    buscar_campania_por_nombre,
    crear_campania,
    listar_campanias_de_donaciones_todas,
)

from OhMyDog.views.utils import agregar_mensaje_error


def agregar_campania_donacion(request):
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
    return render(request, "agregar_campania_donacion.html")


def listar_campanias_de_donaciones(request):
    campanias = listar_campanias_de_donaciones_todas()
    for campania in campanias:
        campania.progreso = (campania.monto_recaudado / campania.monto_objetivo) * 100
    return render(request, "listar_campanias_de_donaciones.html", {"campanias": campanias})
