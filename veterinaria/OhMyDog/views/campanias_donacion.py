from django.shortcuts import render, redirect
from django.contrib import messages
from OhMyDog.modelos.publicaciones import (
    buscar_campania_por_nombre,
    crear_campania,
)

from OhMyDog.views.utils import agregar_mensaje_error
def agregar_campania_donacion(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        objetivo = request.POST.get("objetivo")
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        if buscar_campania_por_nombre (nombre) is None:
            crear_campania(nombre, objetivo, fecha_inicio, fecha_fin)
            messages.success(request, "Campaña agregada con exito.")
            return redirect("mis_adopciones")
        else:
            agregar_mensaje_error(request, f"Campaña con nombre: {nombre}, ya creada.")
    return render (request, "agregar_campania_donacion.html")